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
