<!-- ========================================================= -->
<!--                    BehaviorGuard AI                        -->
<!-- ========================================================= -->

<div align="center">

<h1>🛡️ BehaviorGuard AI</h1>

<h3>
Continuous Behavioral Authentication & <br>
Silent Duress Detection for Digital Banking
</h3>

<p>

<b>Team Trust Shield AI</b><br>

National Forensic Sciences University (NFSU)<br>

Cyber Security PSBs Hackathon Series 2026<br>

Department of Financial Services (DFS) • Indian Banks' Association (IBA)<br>

MNNIT Allahabad, Prayagraj

</p>

<br>

<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Flask-Web_App-000000?style=for-the-badge&logo=flask">

<img src="https://img.shields.io/badge/FastAPI-Risk_Engine-009688?style=for-the-badge&logo=fastapi">

<img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql">

<img src="https://img.shields.io/badge/TensorFlow-Autoencoder-FF6F00?style=for-the-badge&logo=tensorflow">

<img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge">

<br><br>

<img src="https://img.shields.io/badge/Behavioral%20Authentication-AI-blue?style=flat-square">

<img src="https://img.shields.io/badge/Silent-Duress%20Detection-red?style=flat-square">

<img src="https://img.shields.io/badge/Banking-CyberSecurity-darkgreen?style=flat-square">

<img src="https://img.shields.io/badge/Hackathon-2026-orange?style=flat-square">

</div>

---

# 📌 Abstract

BehaviorGuard AI is an AI-powered **continuous behavioral authentication system** designed for modern digital banking.

Instead of verifying users only once during login, the platform continuously evaluates user behavior throughout the entire banking session using a **31-feature behavioral vector** consisting of:

- ⌨️ Keystroke Dynamics
- 🖱️ Mouse Kinematics
- 📈 Session-Level Behavioural Signals

Every interaction is analyzed in real time by a hybrid AI ensemble consisting of:

<table>
<tr align="center">

<th width="40%">Model</th>
<th width="20%">Weight</th>
<th>Description</th>

</tr>

<tr>

<td><b>Isolation Forest</b></td>
<td align="center"><b>60%</b></td>
<td>Detects anomalous behavioural sessions without requiring previous attack examples.</td>

</tr>

<tr>

<td><b>Autoencoder</b></td>
<td align="center"><b>40%</b></td>
<td>Measures reconstruction error to identify gradual behavioural drift during a live session.</td>

</tr>

</table>

<br>

The combined ensemble generates a **risk score between 1–100 in under 50 milliseconds**, enabling one of four security actions:

<table align="center">

<tr>

<th>Risk Score</th>
<th>Decision</th>

</tr>

<tr>

<td align="center">0–45</td>

<td align="center">✅ Allow</td>

</tr>

<tr>

<td align="center">46–60</td>

<td align="center">🔐 OTP Step-Up</td>

</tr>

<tr>

<td align="center">61–80</td>

<td align="center">⏸ Hold Session</td>

</tr>

<tr>

<td align="center">81–100</td>

<td align="center">🚫 Block Access</td>

</tr>

</table>

<br>

Unlike traditional banking authentication systems, BehaviorGuard AI introduces **Silent Duress Detection**, allowing customers to discreetly signal coercion using facial gestures (wink, blink, etc.) without alerting an attacker.

No modifications to existing banking infrastructure are required because the platform operates as an **overlay architecture** built using:

- Flask Web Layer
- FastAPI Risk Engine
- MySQL Audit Database

---

<div align="center">

## 🏆 Hackathon Achievement

Built for the

### Cyber Security PSBs Hackathon Series 2026

Hosted by

**Department of Financial Services (DFS)**

**Indian Banks' Association (IBA)**

**MNNIT Allahabad**

The project demonstrates a complete production-style authentication pipeline—from behavioural event capture and AI inference to policy enforcement and immutable audit logging.

</div>

---

# 🎯 Problem Statement

Modern banking authentication relies primarily on **one-time verification**, creating significant security gaps once a session begins.

<table>

<tr>

<th width="7%">#</th>

<th width="28%">Security Gap</th>

<th>Description</th>

</tr>

<tr>

<td align="center">(a)</td>

<td><b>Credential Theft</b></td>

<td>Passwords and OTPs obtained through phishing or SIM swapping provide attackers unrestricted account access.</td>

</tr>

<tr>

<td align="center">(b)</td>

<td><b>Session Hijacking</b></td>

<td>Once authenticated, users are never continuously verified, allowing attackers to take over active sessions unnoticed.</td>

</tr>

<tr>

<td align="center">(c)</td>

<td><b>Rule Evasion</b></td>

<td>Traditional fraud systems depend on static thresholds that attackers can deliberately avoid.</td>

</tr>

<tr>

<td align="center">(d)</td>

<td><b>Physical Coercion</b></td>

<td>Current banking applications provide no invisible method for victims to silently report forced transactions.</td>

</tr>

</table>

---

# 📊 Traditional Banking vs BehaviorGuard AI

<table>

<tr>

<th width="50%">❌ Traditional Authentication</th>

<th width="50%">✅ BehaviorGuard AI</th>

</tr>

<tr>

<td>One-time login authentication</td>

<td>Continuous behavioural verification</td>

</tr>

<tr>

<td>No session monitoring</td>

<td>Real-time behavioural scoring</td>

</tr>

<tr>

<td>Rule-based fraud detection</td>

<td>AI-powered anomaly detection</td>

</tr>

<tr>

<td>No protection after login</td>

<td>Continuous identity validation</td>

</tr>

<tr>

<td>No coercion detection</td>

<td>Silent Duress Detection</td>

</tr>

<tr>

<td>Stolen credentials often succeed</td>

<td>Behaviour mismatch immediately increases risk</td>

</tr>

</table>

---

# 💡 Proposed Solution

BehaviorGuard AI transforms authentication from a **single login event** into a **continuous security process**.

Rather than repeatedly asking:

> **"Was the correct password entered?"**

the system continuously asks:

> **"Is the current session still behaving like the genuine account owner?"**

Every mouse movement, keystroke, click, scroll event and typing rhythm contributes to a continuously updated behavioural profile.

Whenever the behavioural pattern begins to drift away from the legitimate user's baseline, the AI risk engine immediately recalculates the session risk and automatically escalates security without interrupting legitimate users.

This enables detection of:

- Credential Theft
- Session Hijacking
- Account Takeover
- Insider Misuse
- Remote Access Fraud
- Physical Coercion

before financial loss occurs.

---

# ⚡ Core Capabilities

<table>

<tr>

<th width="30%">Capability</th>

<th>Description</th>

</tr>

<tr>

<td><b>🖱️ Behavioural Signal Capture</b></td>

<td>Collects 31 behavioural features including keystroke timing, mouse velocity, curvature, click intervals and scrolling behaviour.</td>

</tr>

<tr>

<td><b>🧠 AI Risk Engine</b></td>

<td>Hybrid AI ensemble combining Isolation Forest (60%) and Autoencoder (40%) to generate behavioural risk scores in under 50 ms.</td>

</tr>

<tr>

<td><b>🛡 Four-Band Decision Policy</b></td>

<td>Automatically classifies every session into Allow, OTP Step-Up, Hold or Block.</td>

</tr>

<tr>

<td><b>👁 Silent Duress Detection</b></td>

<td>Uses facial gesture recognition (wink, blink, etc.) to silently notify administrators while displaying a successful transaction to the attacker.</td>

</tr>

</table>

---

<div align="center">

## 🔄 Continuous Authentication Workflow

```text
User Interaction

       │

       ▼

31 Behavioural Features

       │

       ▼

AI Risk Engine

(Isolation Forest + Autoencoder)

       │

       ▼

Risk Score (1–100)

       │

       ▼

Allow • OTP • Hold • Block

```

</div>

---

<div align="center">

### ⭐ Protecting People, One Transaction at a Time.

</div>

<!-- ========================================================= -->
<!--                PART 2 — SYSTEM ARCHITECTURE               -->
<!-- ========================================================= -->

---

# 🏗️ System Architecture

<p align="center">

BehaviorGuard AI is designed as an <b>overlay architecture</b>, allowing deployment alongside existing banking systems without modifying core banking infrastructure.

</p>

<br>

<div align="center">

```text

                    ┌────────────────────────────────────────────┐
                    │          BehaviorGuard AI Platform         │
                    └────────────────────────────────────────────┘

                                   │
                                   ▼

        ┌────────────────────────────────────────────────────────────┐
        │                 🌐 Browser Layer                           │
        │------------------------------------------------------------│
        │ JavaScript Event Listeners                                │
        │ • Key Press / Release                                     │
        │ • Mouse Movement                                          │
        │ • Click Timing                                            │
        │ • Scroll Behaviour                                        │
        │ • Event Serialization                                     │
        └────────────────────────────────────────────────────────────┘
                                   │
                                   ▼

        ┌────────────────────────────────────────────────────────────┐
        │                   ⚡ Flask Web Layer                       │
        │------------------------------------------------------------│
        │ Session Management                                         │
        │ Routing                                                    │
        │ Login Processing                                           │
        │ OTP Verification                                           │
        │ Transaction Handling                                       │
        └────────────────────────────────────────────────────────────┘
                                   │
                                   ▼

        ┌────────────────────────────────────────────────────────────┐
        │                 🧠 FastAPI Risk Engine                     │
        │------------------------------------------------------------│
        │ Feature Extraction                                         │
        │ StandardScaler                                             │
        │ Isolation Forest                                           │
        │ Autoencoder                                                │
        │ Risk Calculation                                           │
        └────────────────────────────────────────────────────────────┘
                                   │
                                   ▼

        ┌────────────────────────────────────────────────────────────┐
        │                 🗄️ MySQL Audit Layer                       │
        │------------------------------------------------------------│
        │ Login Sessions                                             │
        │ Transaction Logs                                           │
        │ Risk Scores                                                │
        │ Audit Trail                                                │
        └────────────────────────────────────────────────────────────┘

```

</div>

---

## 🧩 Architecture Layers

<table>

<tr>

<th width="25%">Layer</th>

<th>Description</th>

</tr>

<tr>

<td><b>🌐 Browser Layer</b></td>

<td>

Captures behavioural signals using lightweight JavaScript event listeners without affecting user experience.

</td>

</tr>

<tr>

<td><b>⚡ Flask Web Layer</b></td>

<td>

Manages authentication, user sessions, routing, OTP verification and communication with the AI Risk Engine.

</td>

</tr>

<tr>

<td><b>🧠 FastAPI Risk Engine</b></td>

<td>

Stateless AI microservice responsible for feature extraction, behavioural scoring and policy decisions.

</td>

</tr>

<tr>

<td><b>🗄️ MySQL Audit Layer</b></td>

<td>

Maintains immutable records of login attempts, risk scores, latency and security decisions.

</td>

</tr>

</table>

---

# 🧠 AI Risk Engine

The BehaviourGuard AI Risk Engine continuously evaluates every active banking session.

Unlike traditional authentication systems, it performs behavioural analysis throughout the session rather than only during login.

The engine combines two complementary anomaly detection models:

<table>

<tr>

<th width="30%">Model</th>

<th width="15%">Weight</th>

<th>Purpose</th>

</tr>

<tr>

<td><b>Isolation Forest</b></td>

<td align="center"><b>60%</b></td>

<td>

Detects abnormal sessions using random partitioning and identifies behavioural outliers immediately.

</td>

</tr>

<tr>

<td><b>Autoencoder</b></td>

<td align="center"><b>40%</b></td>

<td>

Measures reconstruction error to identify gradual behavioural drift and evolving anomalies.

</td>

</tr>

</table>

---

# 📊 AI Decision Workflow

<div align="center">

```text

Raw Browser Events
        │
        ▼

Feature Extraction
(31 Behavioural Features)

        │
        ▼

StandardScaler
Feature Normalization

        │
        ▼

 ┌────────────────────────────┐
 │    Isolation Forest (60%)  │
 └────────────────────────────┘
              │
              ├──────────────┐
              │              │
              ▼              ▼
        Weighted Risk Fusion
              ▲              ▲
              │              │
 ┌────────────────────────────┐
 │     Autoencoder (40%)      │
 └────────────────────────────┘

              │
              ▼

      Behavioural Risk Score
             (1–100)

              │
              ▼

 ┌────────┬─────────┬────────┬────────┐
 │ Allow  │  OTP    │ Hold   │ Block  │
 └────────┴─────────┴────────┴────────┘

```

</div>

---

# 🎯 31 Behavioural Feature Vector

The AI engine evaluates every session using **31 behavioural features** extracted from user interaction.

<table>

<tr>

<th width="30%">Category</th>

<th>Features</th>

</tr>

<tr>

<td><b>⌨️ Keystroke Dynamics</b></td>

<td>

Hold Time<br>

Flight Time<br>

Typing Speed<br>

Error Rate<br>

Key Latency

</td>

</tr>

<tr>

<td><b>🖱️ Mouse Kinematics</b></td>

<td>

Velocity<br>

Acceleration<br>

Curvature<br>

Movement Distance<br>

Click Timing<br>

Scroll Behaviour

</td>

</tr>

<tr>

<td><b>📈 Session Behaviour</b></td>

<td>

Idle Ratio<br>

Session Duration<br>

Event Frequency<br>

Interaction Density

</td>

</tr>

</table>

---

# ⚖️ Four-Level Decision Policy

<table>

<tr>

<th width="20%">Risk Score</th>

<th width="20%">Decision</th>

<th>System Response</th>

</tr>

<tr>

<td align="center"><b>0 – 45</b></td>

<td align="center">✅ Allow</td>

<td>Grant full access without interruption.</td>

</tr>

<tr>

<td align="center"><b>46 – 60</b></td>

<td align="center">🔐 OTP Step-Up</td>

<td>Require secondary verification before continuing.</td>

</tr>

<tr>

<td align="center"><b>61 – 80</b></td>

<td align="center">⏸ Hold</td>

<td>Temporarily suspend the session for investigation.</td>

</tr>

<tr>

<td align="center"><b>81 – 100</b></td>

<td align="center">🚫 Block</td>

<td>Immediately terminate access and log the incident.</td>

</tr>

</table>

---

# ✅ Implementation Status

<table>

<tr>

<th>Module</th>

<th>Status</th>

</tr>

<tr>

<td>Behavioural Event Capture</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>31 Feature Extraction</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>Isolation Forest Integration</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>Autoencoder Integration</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>Risk Score Generation</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>Decision Policy</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>OTP Step-Up Flow</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>Behaviour-Based Blocking</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>Silent Duress Detection</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>Transaction PIN Verification</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>Admin Dashboard</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>Real-Time Security Alerts</td>

<td>✅ Complete</td>

</tr>

<tr>

<td>MySQL Audit Logging</td>

<td>✅ Complete</td>

</tr>

</table>

---

# 💻 Technology Stack

## Backend

<table>

<tr>

<th>Technology</th>

<th>Purpose</th>

</tr>

<tr><td>Python 3.9+</td><td>Core Programming Language</td></tr>

<tr><td>Flask</td><td>Web Application Framework</td></tr>

<tr><td>FastAPI</td><td>Risk Engine Microservice</td></tr>

<tr><td>MySQL</td><td>Persistent Audit Database</td></tr>

<tr><td>TensorFlow / Keras</td><td>Autoencoder Model</td></tr>

<tr><td>Scikit-learn</td><td>Isolation Forest & StandardScaler</td></tr>

<tr><td>MediaPipe</td><td>Facial Landmark Detection</td></tr>

<tr><td>OpenCV</td><td>Video Processing</td></tr>

<tr><td>XGBoost</td><td>Eye-State Classification</td></tr>

<tr><td>NumPy</td><td>Numerical Computation</td></tr>

</table>

<br>

## Frontend

<table>

<tr>

<th>Technology</th>

<th>Purpose</th>

</tr>

<tr><td>HTML5</td><td>Page Structure</td></tr>

<tr><td>CSS3</td><td>Styling</td></tr>

<tr><td>Vanilla JavaScript</td><td>Behaviour Capture</td></tr>

<tr><td>Tailwind CSS</td><td>Responsive UI</td></tr>

<tr><td>Material Icons</td><td>User Interface Icons</td></tr>

</table>

<br>

## Security

<table>

<tr>

<th>Technology</th>

<th>Purpose</th>

</tr>

<tr>

<td>SHA-256</td>

<td>Password & Transaction PIN Hashing</td>

</tr>

<tr>

<td>Session Management</td>

<td>Secure Authentication</td>

</tr>

<tr>

<td>CORS</td>

<td>Cross-Origin Security</td>

</tr>

</table>

---

<div align="center">

### 🚀 Real-Time Behavioural Intelligence for Secure Digital Banking

</div>

<!-- ========================================================= -->
<!--          PART 3 — INSTALLATION & PROJECT GUIDE            -->
<!-- ========================================================= -->

---

# 🔑 Demo Credentials

<div align="center">

<table>

<tr>
<th>User</th>
<th>Password</th>
<th>Transaction PIN</th>
<th>Account Type</th>
<th>Balance</th>
</tr>

<tr>
<td><b>ganesh</b></td>
<td><code>Qwertyuiopas12@</code></td>
<td><code>1234</code></td>
<td>Savings</td>
<td>₹245,800.50</td>
</tr>

<tr>
<td><b>pratik</b></td>
<td><code>Test@1234</code></td>
<td><code>1234</code></td>
<td>Savings</td>
<td>₹185,420.00</td>
</tr>

<tr>
<td><b>sohel</b></td>
<td><code>Loveishappiness12@</code></td>
<td><code>1234</code></td>
<td>Current</td>
<td>₹325,000.00</td>
</tr>

</table>

</div>

<br>

## 👨‍💻 Admin Access

| Item | Value |
|------|-------|
| URL | `/admin` |
| Password | `admin@123` |

---

# 📁 Project Structure

```text
behaviorguard_final_web/

├── app.py
├── database.py
├── risk_engine.py
├── schema.sql
├── requirements.txt
│
├── models/
│   ├── face_landmarker.task
│   ├── eye_state_xgb.pkl
│   ├── scaler.pkl
│   ├── isolation_forest.pkl
│   └── autoencoder.h5
│
├── static/
│   └── alarm.mp3
│
├── templates/
│   ├── admin.html
│   ├── admin_login.html
│   ├── dashboard.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── transfer.html
│   ├── verify.html
│   ├── success.html
│   ├── failed.html
│   ├── blocked.html
│   └── otp.html
│
└── README.md
```

---

# 🗄️ Database Schema

## 👤 Users Table

<table>

<tr>
<th>Column</th>
<th>Type</th>
<th>Description</th>
</tr>

<tr><td>id</td><td>INT</td><td>Primary Key</td></tr>
<tr><td>username</td><td>VARCHAR(100)</td><td>Unique Username</td></tr>
<tr><td>password_hash</td><td>VARCHAR(64)</td><td>SHA-256 Password Hash</td></tr>
<tr><td>full_name</td><td>VARCHAR(100)</td><td>User Name</td></tr>
<tr><td>account_number</td><td>VARCHAR(20)</td><td>Bank Account Number</td></tr>
<tr><td>account_type</td><td>VARCHAR(30)</td><td>Savings / Current</td></tr>
<tr><td>balance</td><td>DECIMAL</td><td>Current Balance</td></tr>
<tr><td>email</td><td>VARCHAR(100)</td><td>Email Address</td></tr>
<tr><td>phone</td><td>VARCHAR(20)</td><td>Phone Number</td></tr>
<tr><td>transaction_pin</td><td>VARCHAR(64)</td><td>SHA-256 PIN</td></tr>
<tr><td>created_at</td><td>DATETIME</td><td>Creation Timestamp</td></tr>

</table>

---

## 💳 Transactions Table

<table>

<tr>
<th>Column</th>
<th>Description</th>
</tr>

<tr><td>user_id</td><td>User Reference</td></tr>
<tr><td>recipient_name</td><td>Receiver Name</td></tr>
<tr><td>account_number</td><td>Receiver Account</td></tr>
<tr><td>ifsc_code</td><td>Bank IFSC</td></tr>
<tr><td>amount</td><td>Transfer Amount</td></tr>
<tr><td>purpose</td><td>Purpose</td></tr>
<tr><td>status</td><td>SUCCESS / DURESS_BLOCKED</td></tr>
<tr><td>created_at</td><td>Timestamp</td></tr>

</table>

---

## 🔐 Login Sessions

<table>

<tr>
<th>Column</th>
<th>Description</th>
</tr>

<tr><td>user_id</td><td>User Reference</td></tr>
<tr><td>timestamp</td><td>Login Time</td></tr>
<tr><td>event_count</td><td>Total Behaviour Events</td></tr>
<tr><td>risk_score</td><td>AI Risk Score</td></tr>
<tr><td>decision</td><td>Allow / OTP / Hold / Block</td></tr>
<tr><td>ip_address</td><td>User IP</td></tr>
<tr><td>latency_ms</td><td>Inference Latency</td></tr>

</table>

---

# 🌐 API Endpoints

## Flask Application

<table>

<tr>
<th>Endpoint</th>
<th>Method</th>
<th>Description</th>
</tr>

<tr><td>/</td><td>GET</td><td>Login Page</td></tr>
<tr><td>/login</td><td>POST</td><td>Behaviour Login</td></tr>
<tr><td>/home</td><td>GET</td><td>User Dashboard</td></tr>
<tr><td>/transfer</td><td>GET / POST</td><td>Money Transfer</td></tr>
<tr><td>/verify</td><td>GET</td><td>Face Verification</td></tr>
<tr><td>/video_feed</td><td>GET</td><td>Camera Stream</td></tr>
<tr><td>/dashboard</td><td>GET</td><td>Analytics Dashboard</td></tr>
<tr><td>/admin</td><td>GET / POST</td><td>Admin Panel</td></tr>

</table>

---

## REST API

<table>

<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>

<tr><td>/api/status</td><td>Current Gesture Status</td></tr>
<tr><td>/api/verify</td><td>Verify Transaction</td></tr>
<tr><td>/api/reset</td><td>Reset Duress Flag</td></tr>
<tr><td>/api/live-alerts</td><td>Active Alerts</td></tr>
<tr><td>/api/duress-history</td><td>Alert History</td></tr>
<tr><td>/api/dashboard-stats</td><td>Dashboard Statistics</td></tr>
<tr><td>/api/live-stats</td><td>Real-Time Statistics</td></tr>

</table>

---

## FastAPI Risk Engine

<table>

<tr>
<th>Endpoint</th>
<th>Method</th>
<th>Description</th>
</tr>

<tr><td>/api/score-session</td><td>POST</td><td>Generate Behaviour Risk Score</td></tr>

<tr><td>/health</td><td>GET</td><td>Health Check</td></tr>

</table>

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/behaviorguard-ai.git

cd behaviorguard-ai
```

---

## 2️⃣ Create Virtual Environment

```bash
# Conda
conda create -n behaviorguard python=3.9

conda activate behaviorguard

# OR

python -m venv behaviorguard_env

# Linux / macOS

source behaviorguard_env/bin/activate

# Windows

behaviorguard_env\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create Database

```bash
mysql -u root -p < schema.sql
```

---

## 5️⃣ Configure MySQL

```python
DB_CONFIG = {

    "host":"localhost",

    "user":"root",

    "password":"your_password",

    "database":"behaviorguard1"

}
```

---

## 6️⃣ Add AI Models

Place these files inside the **models/** folder.

```text
face_landmarker.task

eye_state_xgb.pkl

scaler.pkl

isolation_forest.pkl

autoencoder.h5
```

---

## 7️⃣ Run FastAPI Risk Engine

```bash
uvicorn risk_engine:app --reload --host 0.0.0.0 --port 8000
```

---

## 8️⃣ Start Flask Server

```bash
python app.py
```

---

## 9️⃣ Open Application

<table>

<tr>
<th>Service</th>
<th>URL</th>
</tr>

<tr>

<td>User Portal</td>

<td>http://localhost:5000</td>

</tr>

<tr>

<td>Admin Panel</td>

<td>http://localhost:5000/admin</td>

</tr>

<tr>

<td>Dashboard</td>

<td>http://localhost:5000/dashboard</td>

</tr>

<tr>

<td>Risk Engine</td>

<td>http://localhost:8000</td>

</tr>

</table>

---

# 🛠 Troubleshooting

<details>

<summary><b>📷 Camera Not Working</b></summary>

- Check camera permissions

- Verify OpenCV installation

- Change webcam index

</details>

<details>

<summary><b>🗄 Database Connection Error</b></summary>

- Ensure MySQL is running

- Verify credentials

- Import schema.sql

</details>

<details>

<summary><b>🧠 AI Model Loading Error</b></summary>

- Verify all model files exist

- Install dependencies

- Check model paths

</details>

<details>

<summary><b>🔌 Port Already in Use</b></summary>

```python
app.run(port=5001)
```

</details>

---

<div align="center">

## ⚙️ Ready to Launch 🚀

BehaviorGuard AI is now configured and ready for secure behavioural authentication.

</div>

<!-- ========================================================= -->
<!--             PART 4 — FUTURE, LICENSE & CONTACT            -->
<!-- ========================================================= -->

---

# 🔮 Future Scope

<p align="center">

BehaviorGuard AI has been designed with scalability in mind. Future enhancements focus on production-scale deployment, improved model performance, and enterprise integration.

</p>

<table>

<tr>

<th width="30%">Area</th>

<th>Description</th>

</tr>

<tr>

<td><b>🏦 Production Deployment</b></td>

<td>

Validate behavioural thresholds using large-scale real-world banking datasets collected across multiple financial institutions.

</td>

</tr>

<tr>

<td><b>⚡ Kafka Streaming</b></td>

<td>

Replace batched behavioural event collection with Apache Kafka streams for ultra-low latency inference.

</td>

</tr>

<tr>

<td><b>🚀 Redis Caching</b></td>

<td>

Cache behavioural profiles and AI predictions to reduce inference latency during high transaction volumes.

</td>

</tr>

<tr>

<td><b>📱 Mobile SDK</b></td>

<td>

Develop Android and iOS SDKs for UPI, mobile banking, and fintech applications.

</td>

</tr>

<tr>

<td><b>🤖 ONNX Deployment</b></td>

<td>

Export machine learning models to ONNX for lightweight and platform-independent inference.

</td>

</tr>

<tr>

<td><b>🔒 Federated Learning</b></td>

<td>

Enable privacy-preserving behavioural model training without transferring sensitive user data.

</td>

</tr>

<tr>

<td><b>🌍 Multi-Bank Deployment</b></td>

<td>

Support enterprise deployment across multiple banking organizations using centralized risk intelligence.

</td>

</tr>

</table>

---

# 📝 Conclusion

BehaviorGuard AI transforms digital banking authentication from a **single login verification** into a **continuous behavioural security system**.

Unlike conventional authentication solutions, the platform continuously monitors user behaviour throughout the entire banking session using a **31-feature behavioural vector** powered by an AI ensemble consisting of **Isolation Forest** and **Autoencoder** models.

The system provides:

- ✅ Continuous Behavioural Authentication
- ✅ Real-Time AI Risk Scoring
- ✅ Four-Level Decision Policy
- ✅ Behaviour-Based Session Protection
- ✅ Silent Duress Detection
- ✅ Complete Audit Logging
- ✅ Stateless Microservice Architecture

By operating as an overlay architecture, BehaviorGuard AI integrates seamlessly with existing banking infrastructure without requiring modifications to core banking systems.

Its ability to detect behavioural anomalies, session hijacking, credential misuse, and physically coerced transactions makes it a practical next-generation security solution for modern digital banking.

---

<div align="center">

# 🏆 Hackathon Build

This project was developed for the

## Cyber Security PSBs Hackathon Series 2026

Hosted by

**Department of Financial Services (DFS)**

**Indian Banks' Association (IBA)**

**MNNIT Allahabad**

The project demonstrates a complete production-style authentication pipeline:

```text

Behaviour Capture

↓

Feature Engineering

↓

AI Inference

↓

Risk Score Generation

↓

Decision Policy

↓

Immutable Audit Logging

↓

Live Dashboard & Alerts

```

Unlike a prototype, every major module has been fully integrated into a working end-to-end system.

</div>

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve BehaviorGuard AI, please follow these steps.

```bash
Fork the Repository

↓

Create a Feature Branch

git checkout -b feature/my-feature

↓

Commit Changes

git commit -m "Added new feature"

↓

Push Changes

git push origin feature/my-feature

↓

Open a Pull Request
```

---

## Contribution Guidelines

- Follow **PEP-8** coding standards.
- Write meaningful commit messages.
- Add tests for new functionality.
- Update documentation when required.
- Keep pull requests focused and modular.

---

# 📄 License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026

BehaviorGuard AI

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files to deal
in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software.
```

For more information, see the LICENSE file.

---

# 🙏 Acknowledgements

BehaviorGuard AI was made possible through several outstanding open-source technologies.

<table>

<tr>

<th>Technology</th>

<th>Purpose</th>

</tr>

<tr>

<td>🐍 Python</td>

<td>Core Programming Language</td>

</tr>

<tr>

<td>⚡ Flask</td>

<td>Web Framework</td>

</tr>

<tr>

<td>🚀 FastAPI</td>

<td>Risk Engine Microservice</td>

</tr>

<tr>

<td>🤖 TensorFlow</td>

<td>Autoencoder Implementation</td>

</tr>

<tr>

<td>📊 Scikit-learn</td>

<td>Isolation Forest & StandardScaler</td>

</tr>

<tr>

<td>👁 MediaPipe</td>

<td>Face Landmark Detection</td>

</tr>

<tr>

<td>🎥 OpenCV</td>

<td>Video Processing</td>

</tr>

<tr>

<td>🌲 XGBoost</td>

<td>Eye-State Classification</td>

</tr>

<tr>

<td>🗄 MySQL</td>

<td>Persistent Storage</td>

</tr>

<tr>

<td>🎨 Tailwind CSS</td>

<td>User Interface</td>

</tr>

</table>

---

# 📬 Contact

<div align="center">

## 🛡️ Team Trust Shield AI

National Forensic Sciences University (NFSU)

Cyber Security PSBs Hackathon Series 2026

</div>

<br>

<table>

<tr>

<th>Item</th>

<th>Details</th>

</tr>

<tr>

<td>👥 Team</td>

<td>Team Trust Shield AI</td>

</tr>

<tr>

<td>🏛 Organization</td>

<td>National Forensic Sciences University</td>

</tr>

<tr>

<td>📧 Email</td>

<td>your.email@example.com</td>

</tr>

<tr>

<td>🌐 GitHub</td>

<td>https://github.com/yourusername/behaviorguard-ai</td>

</tr>

<tr>

<td>🐞 Issues</td>

<td>https://github.com/yourusername/behaviorguard-ai/issues</td>

</tr>

</table>

---

<div align="center">

# ⭐ Support the Project

If you found this project useful,

please consider giving it a ⭐ on GitHub.

<br><br>

<img src="https://img.shields.io/github/stars/yourusername/behaviorguard-ai?style=social">

<br><br>

<img src="https://img.shields.io/badge/Built%20With-Python-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/Powered%20By-AI-success?style=for-the-badge">

<img src="https://img.shields.io/badge/Cyber%20Security-Digital%20Banking-red?style=for-the-badge">

<br><br>

<h2>🛡️ BehaviorGuard AI</h2>

<h3>Protecting People, One Transaction at a Time.</h3>

<br>

<b>Made with ❤️ by Team Trust Shield AI</b>

</div>
