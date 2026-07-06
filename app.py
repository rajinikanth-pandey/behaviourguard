from flask import (Flask, render_template, request, redirect,
                   url_for, session, flash, jsonify, Response)
from flask_cors import CORS
import requests
import json
from datetime import datetime, date
import cv2
import time
import math
import base64
import numpy as np
import joblib
import mediapipe as mp
from collections import deque
import database as db

app = Flask(__name__)
app.secret_key = "behaviorguard-secret-change-in-production"
CORS(app)

# Admin password for admin panel
ADMIN_PASSWORD = "admin@123"

print("Loading models...")

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(
    model_asset_path="face_landmarker.task"
)

options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_faces=1,
    output_face_blendshapes=True,
    output_facial_transformation_matrixes=True,
)

detector = vision.FaceLandmarker.create_from_options(options)

# Load XGBoost model
try:
    model = joblib.load("eye_state_xgb.pkl")
    print("✓ XGBoost model loaded successfully!")
except:
    print("⚠️ XGBoost model not found. Using fallback.")
    model = None


# =====================================================
# Constants
# =====================================================

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
EYE_POINTS = LEFT_EYE + RIGHT_EYE
WINK_THRESHOLD = 0.23
TRIPLE_BLINK_WINDOW = 2.0

# =====================================================
# Global State
# =====================================================

blink_count = 0
eye_closed = False
blink_times = deque()
sequence_state = "NONE"
closed_start = None
duress_flag = False
last_gesture = "NONE"


# =====================================================
# Helper Functions
# =====================================================

def euclidean(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def eye_aspect_ratio(landmarks, eye):
    p1 = landmarks[eye[0]]
    p2 = landmarks[eye[1]]
    p3 = landmarks[eye[2]]
    p4 = landmarks[eye[3]]
    p5 = landmarks[eye[4]]
    p6 = landmarks[eye[5]]

    vertical1 = euclidean(p2, p6)
    vertical2 = euclidean(p3, p5)
    horizontal = euclidean(p1, p4)

    return (vertical1 + vertical2) / (2.0 * horizontal)

def extract_features(landmarks):
    features = []
    for idx in EYE_POINTS:
        lm = landmarks[idx]
        features.extend([lm.x, lm.y, lm.z])
    
    leftEAR = eye_aspect_ratio(landmarks, LEFT_EYE)
    rightEAR = eye_aspect_ratio(landmarks, RIGHT_EYE)
    avgEAR = (leftEAR + rightEAR) / 2
    features.extend([leftEAR, rightEAR, avgEAR])
    
    return features, leftEAR, rightEAR, avgEAR

def detect_gesture(frame):
    global blink_count, eye_closed, blink_times, sequence_state
    global closed_start, duress_flag, last_gesture

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    
    timestamp_ms = int(time.perf_counter() * 1000) % 1000000
    
    result = detector.detect_for_video(mp_image, timestamp_ms)
    
    gesture = "NORMAL"
    detected_gesture = "NORMAL"
    eye_state = 0
    confidence = 0.0

    if len(result.face_landmarks) > 0:
        landmarks = result.face_landmarks[0]
        
        features, leftEAR, rightEAR, avgEAR = extract_features(landmarks)
        
        if model is not None:
            features_np = np.asarray(features, dtype=np.float32).reshape(1, -1)
            eye_state = model.predict(features_np)[0]
            prob = model.predict_proba(features_np)[0]
            confidence = max(prob)
        
        if leftEAR < WINK_THRESHOLD and rightEAR > WINK_THRESHOLD:
            gesture = "LEFT_WINK"
        elif rightEAR < WINK_THRESHOLD and leftEAR > WINK_THRESHOLD:
            gesture = "RIGHT_WINK"

        if eye_state == 1:
            if closed_start is None:
                closed_start = time.perf_counter()
        else:
            if closed_start is not None:
                duration = time.perf_counter() - closed_start
                if duration > 2:
                    gesture = "LONG_BLINK"
                closed_start = None

        if eye_state == 1:
            if not eye_closed:
                eye_closed = True
        else:
            if eye_closed:
                blink_count += 1
                eye_closed = False
                current_time = time.perf_counter()
                blink_times.append(current_time)
                
                while blink_times and current_time - blink_times[0] > TRIPLE_BLINK_WINDOW:
                    blink_times.popleft()
                
                if len(blink_times) >= 3:
                    detected_gesture = "TRIPLE_BLINK"
                    blink_times.clear()
                else:
                    detected_gesture = gesture

        if gesture == "LEFT_WINK":
            if sequence_state == "RIGHT":
                gesture = "RIGHT_LEFT_WINK"
                sequence_state = "NONE"
            else:
                sequence_state = "LEFT"
        elif gesture == "RIGHT_WINK":
            if sequence_state == "LEFT":
                gesture = "LEFT_RIGHT_WINK"
                sequence_state = "NONE"
            else:
                sequence_state = "RIGHT"

        if detected_gesture != "TRIPLE_BLINK":
            detected_gesture = gesture

        if detected_gesture != "NORMAL":
            last_gesture = detected_gesture

    return {
        'gesture': detected_gesture,
        'duress': duress_flag,
    }

# =====================================================
# Video Streaming
# =====================================================

def generate_video_frames():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Cannot open webcam")
        return
    
    print("✅ Webcam opened successfully")
    
    while True:
        success, frame = cap.read()
        if not success:
            break
        
        detect_gesture(frame)
        
        ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    
    cap.release()

# =====================================================
# Webcam Routes
# =====================================================

@app.route("/video_feed")
def video_feed():
    return Response(
        generate_video_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

@app.route("/verify")
def verify():
    if "user_id" not in session:
        return redirect(url_for("index"))
    
    if "transaction" not in session:
        flash("No pending transaction to verify.", "warning")
        return redirect(url_for("home"))
    
    verification_method = session.get("verification_method", "face_transaction")
    
    return render_template("verify.html", verification_method=verification_method)

# =====================================================
# API Routes
# =====================================================

@app.route("/api/status")
def get_status():
    if "user_id" not in session:
        return jsonify({
            "success": False,
            "message": "Please log in first."
        }), 401
    
    has_gesture = last_gesture != "NONE"
    
    return jsonify({
        'gesture': last_gesture,
        'duress': duress_flag,
        'has_gesture': has_gesture,
        'is_registered': True
    })

@app.route("/api/verify", methods=['POST'])
def verify_transaction():
    global duress_flag, last_gesture
    
    if "user_id" not in session:
        return jsonify({
            "success": False,
            "message": "Please log in first.",
            "redirect": "/login"
        }), 401
    
    tx = session.get("transaction")
    
    if not tx:
        return jsonify({
            "success": False,
            "message": "No pending transaction found.",
            "redirect": "/home"
        }), 400
    
    verification_method = session.get("verification_method", "face_transaction")
    
    # PIN Transaction - Just process normally
    if verification_method == "pin_transaction":
        print(f"🔑 PIN Transaction - Processing normally")
        return process_transaction(tx, duress=False)
    
    # Face Transaction - PIN already verified, now check gesture
    print(f"👤 Face Transaction - PIN verified, checking gesture")
    
    if last_gesture != "NONE":
        duress_flag = True
        print(f"🔴 DURESS DETECTED! Gesture: {last_gesture}")
        print(f"  User: {session.get('username')}")
        print(f"  ⚠️ Transaction BLOCKED in backend")
        print(f"  ✅ User sees SUCCESS message")
        print("-" * 40)
        
        last_gesture = "NONE"
        
        # Block in backend
        tx_id = db.block_transaction(session["user_id"], tx)
        
        session.pop("transaction", None)
        session.pop("verification_method", None)
        session["last_transaction"] = tx
        session["last_transaction_id"] = tx_id
        session["is_duress"] = True
        
        return jsonify({
            "success": True,
            "duress": True,
            "blocked": True,
            "redirect": "/success",
            "message": "Transaction processed successfully"
        })
    else:
        duress_flag = False
        print(f"✅ No duress detected for user {session.get('username')}")
        return process_transaction(tx, duress=False)

def process_transaction(tx, duress):
    if duress:
        tx_id = db.block_transaction(session["user_id"], tx)
        session.pop("transaction", None)
        session.pop("verification_method", None)
        session["last_transaction"] = tx
        session["last_transaction_id"] = tx_id
        session["is_duress"] = True
        return jsonify({
            "success": True,
            "duress": True,
            "blocked": True,
            "redirect": "/success"
        })
    else:
        balance_updated = db.deduct_balance(session["user_id"], tx["amount"])
        if balance_updated:
            tx_id = db.create_transaction(session["user_id"], tx)
            print(f"✅ Transaction SUCCESS for user {session.get('username')}")
            
            session["last_transaction"] = tx
            session["last_transaction_id"] = tx_id
            session["transaction_status"] = "success"
            session["is_duress"] = False
            session.pop("transaction", None)
            session.pop("verification_method", None)
            
            return jsonify({
                "success": True,
                "duress": False,
                "blocked": False,
                "redirect": "/success"
            })
        else:
            print(f"❌ Balance update failed for user {session.get('username')}")
            return jsonify({
                "success": False,
                "message": "Insufficient balance",
                "redirect": "/home"
            }), 400

@app.route("/api/reset")
def reset():
    global duress_flag, last_gesture
    
    if "user_id" not in session:
        return jsonify({
            "success": False,
            "message": "Please log in first."
        }), 401
    
    duress_flag = False
    last_gesture = "NONE"
    return jsonify({'success': True})

# =====================================================
# Success & Failed Pages
# =====================================================

@app.route("/success")
def success():
    if "user_id" not in session:
        return redirect(url_for("index"))
    
    tx = session.get("last_transaction")
    tx_id = session.get("last_transaction_id")
    is_duress = session.get("is_duress", False)
    
    if not tx:
        flash("No transaction to display.", "warning")
        return redirect(url_for("home"))
    
    user = db.get_user(session["user_id"])
    
    ref = f"BG{datetime.now().strftime('%Y%m%d')}{str(tx_id or '0000').zfill(4)}"
    
    session.pop("last_transaction", None)
    session.pop("last_transaction_id", None)
    session.pop("is_duress", None)
    
    return render_template("success.html", 
                         transaction=tx, 
                         user=user,
                         datetime=datetime,
                         reference=ref,
                         is_blocked=False,
                         is_duress=is_duress)

@app.route("/failed")
def failed():
    if "user_id" not in session:
        return redirect(url_for("index"))
    
    tx = session.get("last_transaction")
    tx_id = session.get("last_transaction_id")
    
    if not tx:
        flash("No transaction to display.", "warning")
        return redirect(url_for("home"))
    
    user = db.get_user(session["user_id"])
    
    ref = f"BG{datetime.now().strftime('%Y%m%d')}{str(tx_id or '0000').zfill(4)}"
    
    session.pop("last_transaction", None)
    session.pop("last_transaction_id", None)
    
    return render_template("failed.html", 
                         transaction=tx, 
                         user=user,
                         datetime=datetime,
                         reference=ref)

# =====================================================
# Live Alerts API
# =====================================================

@app.route("/api/live-alerts")
def live_alerts():
    alerts = db.get_active_alerts()
    return jsonify(alerts)

@app.route("/api/duress-history")
def duress_history():
    history = db.get_duress_history(20)
    return jsonify(history)

@app.route("/api/dashboard-stats")
def dashboard_stats():
    stats = db.get_dashboard_stats()
    return jsonify(stats)

# =====================================================
# Admin Routes with Password Protection
# =====================================================

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if session.get("admin_authenticated"):
        return render_template("admin.html")
    
    if request.method == "POST":
        password = request.form.get("password", "").strip()
        if password == ADMIN_PASSWORD:
            session["admin_authenticated"] = True
            return redirect(url_for("admin"))
        else:
            flash("Incorrect admin password.", "error")
            return render_template("admin_login.html")
    
    return render_template("admin_login.html")

@app.route("/admin-logout")
def admin_logout():
    session.pop("admin_authenticated", None)
    flash("Logged out of admin panel.", "info")
    return redirect(url_for("home"))

# =====================================================
# Risk API Configuration
# =====================================================

RISK_API_URL = "http://localhost:8000/api/score-session"
DEMO_OTP = "123456"

ALLOW_MAX = 45
OTP_MAX = 60

def call_risk_api(user, events):
    try:
        payload = {
            "user_id": user["username"],
            "session_id": f"web-{datetime.now().timestamp()}",
            "platform": "web",
            "trust_phase": 4,
            "events": events
        }
        resp = requests.post(RISK_API_URL, json=payload, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            score = data["risk_score"]
            decision = decide(score)
            return score, decision, data.get("factors", {}), data.get("latency_ms", 0)
    except Exception as e:
        print(f"  Risk API offline: {e}")

    return -1, "allow", {"note": "Risk API offline — defaulting to allow"}, 0

def decide(score: int) -> str:
    if score < 0:
        return "allow"
    if score <= ALLOW_MAX:
        return "allow"
    if score <= OTP_MAX:
        return "otp"
    return "block"

def _grant_access(user, risk_score, factors, latency_ms):
    session["user_id"] = user["id"]
    session["username"] = user["username"]
    session["risk_score"] = risk_score
    session["factors"] = factors
    session["latency_ms"] = latency_ms

# =====================================================
# Main Routes
# =====================================================

@app.route("/", methods=["GET"])
def index():
    if "user_id" in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()
    events = json.loads(request.form.get("events", "[]"))

    user = db.authenticate(username, password)

    if not user:
        exists = db.get_user_by_username(username)
        if not exists:
            flash("Username not found. Please check your username or register.", "error")
        else:
            flash("Incorrect password. Please try again.", "error")
        return redirect(url_for("index"))

    risk_score, decision, factors, latency_ms = call_risk_api(user, events)

    db.log_session(
        user_id=user["id"],
        event_count=len(events),
        risk_score=risk_score,
        decision=decision,
        ip_address=request.remote_addr,
        latency_ms=latency_ms
    )

    if decision == "block":
        return render_template("blocked.html",
                               username=user["username"],
                               risk_score=risk_score,
                               factors=factors)

    if decision == "otp":
        session["pending_user_id"] = user["id"]
        session["pending_username"] = user["username"]
        session["pending_risk_score"] = risk_score
        session["pending_factors"] = factors
        return render_template("otp.html",
                               risk_score=risk_score,
                               factors=factors)

    _grant_access(user, risk_score, factors, latency_ms)
    return redirect(url_for("home"))

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    entered = request.form.get("otp", "").strip()
    user_id = session.get("pending_user_id")
    username = session.get("pending_username")
    risk_score = session.get("pending_risk_score", -1)
    factors = session.get("pending_factors", {})

    if not user_id:
        return redirect(url_for("index"))

    if entered == DEMO_OTP:
        for k in ["pending_user_id", "pending_username",
                  "pending_risk_score", "pending_factors"]:
            session.pop(k, None)
        session["user_id"] = user_id
        session["username"] = username
        session["risk_score"] = risk_score
        session["factors"] = factors
        session["latency_ms"] = 0
        flash("✓ Identity verified successfully.", "success")
        return redirect(url_for("home"))
    else:
        flash("Incorrect OTP. Please try again.", "error")
        return render_template("otp.html",
                               risk_score=risk_score,
                               factors=factors)

@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect(url_for("index"))

    user = db.get_user(session["user_id"])
    risk_score = session.get("risk_score", -1)
    factors = session.get("factors", {})
    latency_ms = session.get("latency_ms", 0)
    history = db.get_recent_sessions(session["user_id"], limit=8)
    transactions = db.get_transactions(session["user_id"], limit=10)

    if risk_score < 0:
        color, label = "#1156AE", "No score (API offline)"
    elif risk_score <= ALLOW_MAX:
        color, label = "#007A52", f"Low risk — access granted"
    elif risk_score <= OTP_MAX:
        color, label = "#B45309", f"Medium risk — OTP verified"
    else:
        color, label = "#C0392B", f"High risk"

    return render_template(
        "home.html",
        user=user,
        risk_score=risk_score,
        color=color,
        label=label,
        factors=factors,
        latency_ms=latency_ms,
        history=history,
        transactions=transactions,
        allow_max=ALLOW_MAX,
        otp_max=OTP_MAX
    )

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        confirm_password = request.form.get("confirm_password", "").strip()
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        account_type = request.form.get("account_type", "Savings")
        transaction_pin = request.form.get("transaction_pin", "").strip()

        # Validation
        if not full_name:
            flash("Please enter your full name.", "error")
            return render_template("register.html")
        
        if not email or "@" not in email:
            flash("Please enter a valid email address.", "error")
            return render_template("register.html")
        
        if not phone or len(phone) != 10 or not phone.isdigit():
            flash("Please enter a valid 10-digit phone number.", "error")
            return render_template("register.html")

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("register.html")
        
        if len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
            return render_template("register.html")
        
        if len(transaction_pin) != 4 or not transaction_pin.isdigit():
            flash("Transaction PIN must be a 4-digit number.", "error")
            return render_template("register.html")

        ok, msg = db.register_user(username, password, full_name, email, phone, account_type, transaction_pin)
        if ok:
            flash("Account created! You can now log in.", "success")
            return redirect(url_for("index"))
        else:
            flash(msg, "error")

    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("index"))
    sessions = db.get_all_sessions(limit=50)
    stats = db.get_stats()
    return render_template("dashboard.html",
                           sessions=sessions,
                           stats=stats,
                           allow_max=ALLOW_MAX,
                           otp_max=OTP_MAX)

@app.route("/api/live-stats")
def live_stats():
    if "user_id" not in session:
        return jsonify({"error": "not authenticated"}), 401
    sessions = db.get_all_sessions(limit=20)
    stats = db.get_stats()
    for s in sessions:
        if hasattr(s.get("timestamp"), "isoformat"):
            s["timestamp"] = s["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"sessions": sessions, "stats": stats})

@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    if "user_id" not in session:
        return redirect(url_for("index"))

    user = db.get_user(session["user_id"])

    if request.method == "POST":
        recipient = request.form.get("recipient_name", "").strip()
        account = request.form.get("account_number", "").strip()
        confirm = request.form.get("confirm_account", "").strip()
        ifsc = request.form.get("ifsc_code", "").strip().upper()
        amount = float(request.form.get("amount", 0))
        purpose = request.form.get("purpose", "")
        pin = request.form.get("pin", "")
        verification_method = request.form.get("verification_method", "face_transaction")

        if not recipient:
            flash("Please enter the recipient's name.", "error")
            return render_template("transfer.html", user=user)

        if not account or len(account) != 16 or not account.isdigit():
            flash("Please enter a valid 16-digit account number.", "error")
            return render_template("transfer.html", user=user)

        if account != confirm:
            flash("Account numbers do not match.", "error")
            return render_template("transfer.html", user=user)

        if not ifsc or len(ifsc) != 11:
            flash("Please enter a valid 11-character IFSC code.", "error")
            return render_template("transfer.html", user=user)

        if amount <= 0:
            flash("Enter a valid amount.", "error")
            return render_template("transfer.html", user=user)

        if amount > float(user["balance"]):
            flash(f"Insufficient balance. Available: ₹{float(user['balance']):.2f}", "error")
            return render_template("transfer.html", user=user)

        if not purpose or purpose == "":
            flash("Please select a purpose for the transfer.", "error")
            return render_template("transfer.html", user=user)

        # Verify transaction PIN
        if not db.verify_transaction_pin(session["user_id"], pin):
            flash("Invalid Transaction PIN. Please try again.", "error")
            return render_template("transfer.html", user=user)

        session["transaction"] = {
            "recipient": recipient,
            "account": account,
            "ifsc": ifsc,
            "amount": amount,
            "purpose": purpose
        }
        
        session["verification_method"] = verification_method

        if verification_method == "face_transaction":
            flash(f"👤 Face Transaction: PIN verified, now look at camera for face verification.", "info")
        else:
            flash(f"🔑 PIN Transaction: Processing with PIN only.", "info")

        return redirect(url_for("verify"))

    return render_template("transfer.html", user=user)

@app.route("/logout")
def logout():
    global duress_flag, last_gesture
    duress_flag = False
    last_gesture = "NONE"
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))

# =====================================================
# Run Server
# =====================================================

if __name__ == "__main__":
    print()
    print("=" * 54)
    print("  BehaviorGuard AI — Web App")
    print("=" * 54)
    print("  URL          : http://localhost:5000")
    print("  Dashboard    : http://localhost:5000/dashboard")
    print("  Admin        : http://localhost:5000/admin")
    print("  Admin Password: admin@123")
    print("  Demo users   : ganesh / Qwertyuiopas12@")
    print("                 pratik / Test@1234")
    print("                 sohel / Loveishappiness12@")
    print()
    print("  👤 Face Transaction: PIN + Silent Duress")
    print("  🔑 PIN Transaction: PIN only")
    print()
    print("  Risk thresholds:")
    print(f"  0–{ALLOW_MAX}  → ALLOW")
    print(f"  {ALLOW_MAX+1}–{OTP_MAX} → OTP")
    print(f"  {OTP_MAX+1}+    → BLOCK")
    print()
    print("  Risk API: http://localhost:8000")
    print("=" * 54)
    print()
    app.run(debug=True, port=5000, threaded=True)