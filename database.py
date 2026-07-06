import hashlib
import mysql.connector
from datetime import datetime, date
import random

# ── Edit these to match your MySQL setup ─────────────────────────────────────
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "behaviorguard1"
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# ── User operations ───────────────────────────────────────────────────────────

def get_user_by_username(username: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM users WHERE username = %s",
        (username.lower().strip(),)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def authenticate(username: str, password: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM users WHERE username = %s AND password_hash = %s",
        (username.lower().strip(), hash_password(password))
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def register_user(username: str, password: str, full_name: str, email: str, phone: str, account_type: str, transaction_pin: str):
    """
    Register a new user with complete details including transaction PIN
    """
    if not username or not password:
        return False, "Username and password are required."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    if len(transaction_pin) != 4 or not transaction_pin.isdigit():
        return False, "Transaction PIN must be a 4-digit number."

    conn = get_connection()
    cursor = conn.cursor()
    try:
        account_number = str(random.randint(4000000000000000, 4999999999999999))
        
        cursor.execute("""
            INSERT INTO users
            (
                username,
                password_hash,
                full_name,
                account_number,
                account_type,
                balance,
                email,
                phone,
                transaction_pin,
                created_at
            )
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            username.lower().strip(),
            hash_password(password),
            full_name.title(),
            account_number,
            account_type,
            100000.00,
            email.lower().strip(),
            phone,
            hash_password(transaction_pin),  # Store PIN hashed
            datetime.now()
        ))
        conn.commit()
        return True, "Account created successfully."
    except mysql.connector.IntegrityError as e:
        if "username" in str(e):
            return False, "Username already exists."
        elif "account_number" in str(e):
            return False, "Account number generation failed. Please try again."
        else:
            return False, "Registration failed. Please try again."
    finally:
        cursor.close()
        conn.close()


def verify_transaction_pin(user_id: int, pin: str) -> bool:
    """
    Verify if the provided transaction PIN matches the stored PIN
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT transaction_pin FROM users WHERE id = %s",
        (user_id,)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if result and result["transaction_pin"]:
        return result["transaction_pin"] == hash_password(pin)
    return False


# ── Session logging ───────────────────────────────────────────────────────────

def log_session(user_id: int, event_count: int,
                risk_score: float, decision: str,
                ip_address: str = "", latency_ms: float = 0):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO login_sessions
           (user_id, timestamp, event_count, risk_score, decision, ip_address, latency_ms)
           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (user_id, datetime.now(), event_count,
         risk_score, decision, ip_address, latency_ms)
    )
    conn.commit()
    cursor.close()
    conn.close()


def get_recent_sessions(user_id: int, limit: int = 10):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """SELECT timestamp, risk_score, decision, event_count, latency_ms
           FROM login_sessions WHERE user_id = %s
           ORDER BY timestamp DESC LIMIT %s""",
        (user_id, limit)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_all_sessions(limit: int = 50):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """SELECT ls.timestamp, u.username, ls.risk_score,
                  ls.decision, ls.event_count, ls.latency_ms
           FROM login_sessions ls
           JOIN users u ON ls.user_id = u.id
           ORDER BY ls.timestamp DESC LIMIT %s""",
        (limit,)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_stats():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT
          COUNT(*) as total,
          SUM(decision = 'allow')  as allowed,
          SUM(decision = 'otp')    as otp,
          SUM(decision = 'block')  as blocked,
          AVG(NULLIF(risk_score,-1)) as avg_score
        FROM login_sessions
    """)
    stats = cursor.fetchone()
    cursor.close()
    conn.close()
    return stats or {}


# ── Dashboard Statistics ─────────────────────────────────────────────────────

def get_dashboard_stats():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    today = date.today().strftime('%Y-%m-%d')
    
    cursor.execute("""
        SELECT 
            COUNT(*) as total_transfers,
            SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) as successful,
            SUM(CASE WHEN status = 'DURESS_BLOCKED' THEN 1 ELSE 0 END) as blocked
        FROM transactions
        WHERE DATE(created_at) = %s
    """, (today,))
    tx_stats = cursor.fetchone()
    
    cursor.execute("""
        SELECT AVG(risk_score) as avg_risk
        FROM login_sessions
        WHERE risk_score >= 0
    """)
    risk_stats = cursor.fetchone()
    
    cursor.execute("""
        SELECT COUNT(*) as duress_today
        FROM transactions
        WHERE status = 'DURESS_BLOCKED'
        AND DATE(created_at) = %s
    """, (today,))
    duress_stats = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return {
        'total_transfers': tx_stats['total_transfers'] or 0,
        'successful': tx_stats['successful'] or 0,
        'blocked': tx_stats['blocked'] or 0,
        'avg_risk': round(risk_stats['avg_risk'], 1) if risk_stats['avg_risk'] else '--',
        'duress_today': duress_stats['duress_today'] or 0
    }


# ── Helper function ──────────────────────────────────────────────────────────

def get_user(user_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT *
        FROM users
        WHERE id = %s
    """, (user_id,))

    user = cur.fetchone()

    cur.close()
    conn.close()

    return user


# ── Balance operations ────────────────────────────────────────────────────────

def deduct_balance(user_id, amount):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
        result = cur.fetchone()
        if not result:
            cur.close()
            conn.close()
            return False
        
        current_balance = result[0]
        if current_balance < amount:
            cur.close()
            conn.close()
            return False
        
        cur.execute("""
            UPDATE users
            SET balance = balance - %s
            WHERE id = %s
        """, (amount, user_id))
        
        conn.commit()
        cur.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"Error deducting balance: {e}")
        conn.rollback()
        cur.close()
        conn.close()
        return False


# ── Transaction operations ────────────────────────────────────────────────────

def create_transaction(user_id, tx):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO transactions
        (
            user_id,
            recipient_name,
            account_number,
            ifsc_code,
            amount,
            purpose,
            status,
            created_at
        )
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s)
    """,
    (
        user_id,
        tx["recipient"],
        tx["account"],
        tx["ifsc"],
        tx["amount"],
        tx["purpose"],
        "SUCCESS",
        datetime.now()
    ))

    conn.commit()
    cur.close()
    conn.close()
    return cur.lastrowid


def block_transaction(user_id, tx):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO transactions
        (
            user_id,
            recipient_name,
            account_number,
            ifsc_code,
            amount,
            purpose,
            status,
            created_at
        )
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s)
    """,
    (
        user_id,
        tx["recipient"],
        tx["account"],
        tx["ifsc"],
        tx["amount"],
        tx["purpose"],
        "DURESS_BLOCKED",
        datetime.now()
    ))

    conn.commit()
    cur.close()
    conn.close()
    return cur.lastrowid


def get_active_alerts():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT *
        FROM transactions
        WHERE status = 'DURESS_BLOCKED'
        ORDER BY created_at DESC
    """)

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def get_transactions(user_id, limit=20):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT 
            id,
            recipient_name,
            account_number,
            ifsc_code,
            amount,
            purpose,
            status,
            created_at as timestamp
        FROM transactions
        WHERE user_id = %s AND status = 'SUCCESS'
        ORDER BY created_at DESC
        LIMIT %s
    """, (user_id, limit))

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def get_all_transactions(limit=50):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT 
            t.id,
            u.username,
            u.full_name,
            u.email,
            u.phone,
            t.recipient_name,
            t.account_number,
            t.amount,
            t.purpose,
            t.status,
            t.created_at as timestamp
        FROM transactions t
        JOIN users u ON t.user_id = u.id
        ORDER BY t.created_at DESC
        LIMIT %s
    """, (limit,))

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def get_duress_history(limit=20):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT 
            t.id,
            u.username,
            u.full_name,
            t.recipient_name,
            t.account_number,
            t.amount,
            t.purpose,
            t.status,
            t.created_at as timestamp
        FROM transactions t
        JOIN users u ON t.user_id = u.id
        WHERE t.status = 'DURESS_BLOCKED'
        ORDER BY t.created_at DESC
        LIMIT %s
    """, (limit,))

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
