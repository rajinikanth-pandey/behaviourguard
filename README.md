<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>BehaviorGuard AI – Technical Report & README</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: #f8f9fc;
            color: #1a202c;
            line-height: 1.7;
            padding: 40px 20px;
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            background: #ffffff;
            padding: 50px 60px;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.06);
        }

        /* === Header === */
        .header {
            text-align: center;
            padding-bottom: 30px;
            border-bottom: 2px solid #e9edf4;
            margin-bottom: 30px;
        }

        .header h1 {
            font-size: 38px;
            font-weight: 800;
            color: #0d2137;
            letter-spacing: -0.5px;
        }

        .header h1 span {
            color: #1a6bff;
        }

        .header .subtitle {
            font-size: 18px;
            color: #4a5568;
            margin-top: 8px;
        }

        .header .org {
            font-size: 14px;
            color: #718096;
            margin-top: 4px;
        }

        .badge-group {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 10px;
            margin-top: 14px;
        }

        .badge {
            display: inline-block;
            background: #eef2f7;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            color: #2d3748;
        }

        .badge.blue {
            background: #dbeafe;
            color: #1a6bff;
        }

        .badge.green {
            background: #d1fae5;
            color: #065f46;
        }

        .badge.orange {
            background: #fef3c7;
            color: #92400e;
        }

        .badge.purple {
            background: #ede9fe;
            color: #5b21b6;
        }

        .badge.red {
            background: #fee2e2;
            color: #991b1b;
        }

        /* === Sections === */
        section {
            margin-bottom: 40px;
        }

        h2 {
            font-size: 26px;
            font-weight: 700;
            color: #0d2137;
            margin-bottom: 16px;
            padding-bottom: 8px;
            border-bottom: 3px solid #1a6bff;
            display: inline-block;
        }

        h3 {
            font-size: 20px;
            font-weight: 600;
            color: #1a365d;
            margin-top: 24px;
            margin-bottom: 10px;
        }

        h4 {
            font-size: 17px;
            font-weight: 600;
            color: #2d3748;
            margin-top: 18px;
            margin-bottom: 6px;
        }

        p {
            color: #2d3748;
            margin-bottom: 12px;
            font-size: 15px;
        }

        ul,
        ol {
            padding-left: 24px;
            margin-bottom: 14px;
        }

        li {
            margin-bottom: 6px;
            font-size: 15px;
            color: #2d3748;
        }

        /* === Tables === */
        .table-wrap {
            overflow-x: auto;
            margin: 16px 0 20px;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }

        thead {
            background: #f7fafc;
        }

        th {
            padding: 12px 16px;
            text-align: left;
            font-weight: 600;
            color: #1a202c;
            border-bottom: 2px solid #e2e8f0;
        }

        td {
            padding: 10px 16px;
            border-bottom: 1px solid #edf2f7;
            color: #2d3748;
        }

        tr:last-child td {
            border-bottom: none;
        }

        .table-wrap code {
            background: #edf2f7;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 13px;
            color: #1a202c;
        }

        .status-done {
            color: #38a169;
            font-weight: 600;
        }

        .status-proposed {
            color: #d69e2e;
            font-weight: 600;
        }

        /* === Code Blocks === */
        pre {
            background: #1a202c;
            color: #e2e8f0;
            padding: 18px 22px;
            border-radius: 10px;
            overflow-x: auto;
            font-size: 14px;
            line-height: 1.6;
            margin: 14px 0 18px;
        }

        pre code {
            font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
            color: #e2e8f0;
            background: transparent;
            padding: 0;
        }

        /* === Info Boxes === */
        .info-box {
            background: #f7fafc;
            border-left: 4px solid #1a6bff;
            padding: 16px 20px;
            border-radius: 8px;
            margin: 14px 0;
        }

        .info-box.warning {
            border-left-color: #d69e2e;
            background: #fffbeb;
        }

        .info-box.success {
            border-left-color: #38a169;
            background: #f0fff4;
        }

        .info-box.danger {
            border-left-color: #e53e3e;
            background: #fff5f5;
        }

        /* === Feature Grid === */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin: 16px 0 20px;
        }

        .feature-card {
            background: #f7fafc;
            padding: 16px 18px;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
            transition: 0.2s;
        }

        .feature-card:hover {
            border-color: #1a6bff;
            background: #ebf4ff;
        }

        .feature-card .icon {
            font-size: 28px;
            display: block;
            margin-bottom: 4px;
        }

        .feature-card strong {
            display: block;
            font-size: 15px;
            color: #0d2137;
        }

        .feature-card span {
            font-size: 13px;
            color: #4a5568;
        }

        /* === Architecture Diagram === */
        .arch-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin: 16px 0;
        }

        .arch-box {
            background: #f7fafc;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            padding: 14px 16px;
            text-align: center;
        }

        .arch-box .layer {
            font-weight: 700;
            color: #0d2137;
            font-size: 14px;
        }

        .arch-box .desc {
            font-size: 12px;
            color: #4a5568;
            margin-top: 4px;
        }

        .arch-box.blue {
            border-color: #1a6bff;
            background: #ebf4ff;
        }

        .arch-box.green {
            border-color: #38a169;
            background: #f0fff4;
        }

        .arch-box.orange {
            border-color: #d69e2e;
            background: #fffbeb;
        }

        .arch-box.purple {
            border-color: #5b21b6;
            background: #ede9fe;
        }

        /* === Flow === */
        .flow {
            background: #f7fafc;
            padding: 20px 24px;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
            text-align: center;
            font-size: 14px;
            font-weight: 500;
            color: #2d3748;
            margin: 14px 0 18px;
        }

        .flow .arrow {
            color: #1a6bff;
            font-size: 20px;
            padding: 0 6px;
        }

        .flow .step {
            display: inline-block;
            background: #ffffff;
            padding: 6px 14px;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
            margin: 4px 2px;
        }

        .flow .step.active {
            border-color: #1a6bff;
            background: #ebf4ff;
        }

        /* === Footer === */
        .footer {
            text-align: center;
            border-top: 2px solid #e9edf4;
            padding-top: 30px;
            margin-top: 20px;
            color: #718096;
            font-size: 14px;
        }

        .footer a {
            color: #1a6bff;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }

        /* === Responsive === */
        @media (max-width: 768px) {
            .container {
                padding: 24px 18px;
            }

            .header h1 {
                font-size: 26px;
            }

            h2 {
                font-size: 22px;
            }

            .arch-grid {
                grid-template-columns: 1fr 1fr;
            }

            .feature-grid {
                grid-template-columns: 1fr;
            }

            .flow .step {
                display: block;
                margin: 6px 0;
            }

            .flow .arrow {
                display: block;
                transform: rotate(90deg);
                padding: 4px 0;
            }
        }

        @media (max-width: 480px) {
            .arch-grid {
                grid-template-columns: 1fr;
            }
        }

        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }

        ::-webkit-scrollbar-track {
            background: #edf2f7;
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb {
            background: #cbd5e0;
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #a0aec0;
        }
    </style>
</head>
<body>

    <div class="container">

        <!-- ============================================================ -->
        <!-- HEADER -->
        <!-- ============================================================ -->
        <header class="header">
            <h1>🛡️ BehaviorGuard <span>AI</span></h1>
            <p class="subtitle">Continuous Behavioral Authentication &amp; Silent Duress Detection for Digital Banking</p>
            <p class="org">
                <strong>Team Trust Shield AI</strong> &mdash; National Forensic Sciences University (NFSU) &bull;
                Cyber Security PSBs Hackathon Series 2026 &bull; DFS &amp; IBA &bull; MNNIT Allahabad, Prayagraj
            </p>

            <div class="badge-group">
                <span class="badge blue">🐍 Python</span>
                <span class="badge green">⚡ Flask + FastAPI</span>
                <span class="badge orange">🗄️ MySQL</span>
                <span class="badge purple">🤖 MediaPipe</span>
                <span class="badge">📊 XGBoost</span>
                <span class="badge red">🔐 SHA-256</span>
                <span class="badge">📄 MIT License</span>
            </div>
        </header>

        <!-- ============================================================ -->
        <!-- ABSTRACT -->
        <!-- ============================================================ -->
        <section>
            <h2>📌 Abstract</h2>
            <p>
                <strong>BehaviorGuard AI</strong> is a continuous behavioral authentication layer for digital banking
                that scores every login session in real time using a <strong>31-feature behavioral vector</strong>
                (keystroke dynamics, mouse kinematics, and session-level signals). A two-model ensemble —
                <strong>Isolation Forest (60%)</strong> and an <strong>Autoencoder (40%)</strong> — blends into a
                single <strong>1–100 risk score</strong> in under <strong>50 ms</strong>, driving a four-band
                decision policy: <strong>Allow / OTP Step-Up / Hold / Block</strong>.
            </p>
            <p>
                The system is delivered as a <strong>REST overlay</strong> (Flask web app + FastAPI risk engine + MySQL audit log)
                that requires <strong>no change to core banking infrastructure</strong>, and includes a
                <strong>silent duress-detection channel</strong> for coerced-transaction scenarios using
                <strong>facial gesture recognition</strong> (wink, blink, etc.) — a feature <strong>fully implemented</strong>
                in this version of the system.
            </p>

            <div class="info-box success">
                <strong>🏆 Hackathon Achievement</strong>
                <p style="margin-top:6px;">
                    This project was built for the <strong>Cyber Security PSBs Hackathon Series 2026</strong>,
                    organized by DFS &amp; IBA, hosted at MNNIT Allahabad, Prayagraj. The system demonstrates
                    a complete end-to-end authentication loop — from behavioral event capture to AI-based
                    risk scoring to auditable decision logging — all wired together and runnable in a live demo.
                </p>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- PROBLEM STATEMENT -->
        <!-- ============================================================ -->
        <section>
            <h2>🎯 Problem Statement</h2>
            <p>
                India's digital banking authentication relies on a <strong>single one-time check</strong> at login,
                leaving sessions unverified for their entire duration. This creates four exploitable gaps:
            </p>
            <ul>
                <li><strong>(a) Credential Theft:</strong> Phishing and SIM-swapping bypass OTP entirely once credentials are stolen</li>
                <li><strong>(b) Session Hijacking:</strong> Post-login session hijacking goes undetected because identity is never re-verified mid-session</li>
                <li><strong>(c) Rule Evasion:</strong> Rule-based fraud thresholds are easily evaded by attackers who keep transactions below flagged limits</li>
                <li><strong>(d) Coercion:</strong> There is no invisible alert mechanism for a user being physically coerced into authorizing a transaction</li>
            </ul>

            <div class="info-box warning">
                <strong>⚠️ Today's Banking vs. BehaviorGuard AI</strong>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:10px;">
                    <div style="background:#fee2e2;padding:12px 16px;border-radius:8px;">
                        <strong style="color:#991b1b;">❌ Today's Banking</strong>
                        <ul style="margin-top:6px;font-size:14px;">
                            <li>One-time password check at login only</li>
                            <li>Session never re-verified mid-flow</li>
                            <li>Rule-based thresholds, easily evaded</li>
                            <li>No coercion / duress detection channel</li>
                            <li>Attacker with stolen credentials goes undetected</li>
                        </ul>
                    </div>
                    <div style="background:#d1fae5;padding:12px 16px;border-radius:8px;">
                        <strong style="color:#065f46;">✅ BehaviorGuard AI</strong>
                        <ul style="margin-top:6px;font-size:14px;">
                            <li>Continuous 31-feature behavioral scoring</li>
                            <li>Every event batch scored in real time</li>
                            <li>AI ensemble: Isolation Forest + Autoencoder</li>
                            <li>Silent duress flag (facial gesture trigger)</li>
                            <li>Stolen credentials blocked by behavior mismatch</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- PROPOSED SOLUTION -->
        <!-- ============================================================ -->
        <section>
            <h2>💡 Proposed Solution</h2>
            <p>
                <strong>BehaviorGuard AI</strong> reframes authentication as a <strong>continuous measurement</strong>
                rather than a one-time gate. Instead of asking <em>"was the correct password entered?"</em>, it
                continuously asks <em>"does this session still behave like the account owner?"</em> — scoring every
                batch of interaction events against a model of normal behaviour and reacting the moment that behaviour
                drifts, without ever interrupting a legitimate user who is simply typing and browsing as usual.
            </p>

            <div class="info-box success">
                <strong>🎯 How It Works</strong>
                <p style="margin-top:6px;">
                    The system captures behavioral signals from every page the user touches — keystroke dynamics,
                    mouse velocity, curvature, click timing, and scroll patterns — and turns them into a risk score
                    on every event batch. This allows BehaviorGuard AI to catch a session that starts out looking
                    legitimate but is later taken over by an attacker.
                </p>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- CORE CAPABILITIES -->
        <!-- ============================================================ -->
        <section>
            <h2>⚡ Core Capabilities</h2>

            <div class="feature-grid">
                <div class="feature-card">
                    <span class="icon">📊</span>
                    <strong>Behavioral Signal Capture</strong>
                    <span>31 features from keystroke dynamics, mouse velocity, curvature, click timing and scroll patterns</span>
                </div>
                <div class="feature-card">
                    <span class="icon">🧠</span>
                    <strong>AI Risk Engine</strong>
                    <span>Isolation Forest (60%) + Autoencoder (40%) ensemble. Scores 0–100 in &lt; 50 ms per session</span>
                </div>
                <div class="feature-card">
                    <span class="icon">🎯</span>
                    <strong>4-Band Decision Policy</strong>
                    <span>Allow (0–45) · OTP Step-Up (46–60) · Hold (61–80) · Block (81–100)</span>
                </div>
                <div class="feature-card">
                    <span class="icon">🕵️</span>
                    <strong>Silent Duress Detection</strong>
                    <span>Facial gesture trigger (wink, blink, etc.). Encrypted binary flag — no video stored</span>
                </div>
            </div>

            <p>
                These four capabilities work as a <strong>single continuous loop</strong> rather than four separate checks.
                Behavioral signal capture runs silently in the background of every page, always collecting the raw
                material needed without asking the customer to do anything extra. The AI engine scores on every event
                batch — not just once at login — allowing BehaviorGuard AI to catch both stolen-credential logins
                and session hijacks. The four-band decision policy translates that continuous score into concrete,
                auditable actions: <strong>allow, step up, hold, or block</strong>.
            </p>
        </section>

        <!-- ============================================================ -->
        <!-- SYSTEM ARCHITECTURE -->
        <!-- ============================================================ -->
        <section>
            <h2>🏗️ System Architecture</h2>

            <p>
                BehaviorGuard AI is built as an <strong>overlay</strong>, not a replacement, for an existing banking
                stack. It observes the login flow, computes a risk decision alongside it, and hands control back to
                the bank's own session and OTP machinery.
            </p>

            <div class="arch-grid">
                <div class="arch-box blue">
                    <div class="layer">🌐 Browser Layer</div>
                    <div class="desc">Pure JavaScript event listeners — keydown, keyup, mousemove, click, scroll</div>
                </div>
                <div class="arch-box green">
                    <div class="layer">⚡ Flask Web Layer</div>
                    <div class="desc">Session state, routing, page rendering. Forwards events to risk engine</div>
                </div>
                <div class="arch-box orange">
                    <div class="layer">🧠 FastAPI Risk Engine</div>
                    <div class="desc">Stateless microservice. Loads scaler + Isolation Forest + Autoencoder</div>
                </div>
                <div class="arch-box purple">
                    <div class="layer">🗄️ MySQL Audit Layer</div>
                    <div class="desc">Append-only: every login attempt logged with risk score, decision, IP, latency</div>
                </div>
            </div>

            <p>
                The architecture is deliberately split into <strong>four independent layers</strong> so BehaviorGuard AI
                can sit in front of an existing banking login flow without touching core banking systems. The
                <strong>FastAPI risk engine</strong> is stateless — it reads no database and holds no session — so it
                scales horizontally behind a load balancer just by adding instances. The <strong>MySQL layer</strong>
                is append-only, giving compliance teams a tamper-evident audit trail without adding latency to the
                authentication path.
            </p>
        </section>

        <!-- ============================================================ -->
        <!-- AI RISK ENGINE -->
        <!-- ============================================================ -->
        <section>
            <h2>🧠 AI Risk Engine &amp; Decision Workflow</h2>

            <div class="flow">
                <span class="step">Raw Browser Events</span>
                <span class="arrow">→</span>
                <span class="step active">Extract 31 Features</span>
                <span class="arrow">→</span>
                <span class="step">StandardScaler Normalize</span>
                <br><br>
                <span class="step" style="background:#dbeafe;border-color:#1a6bff;">Isolation Forest (60%)</span>
                <span class="arrow">+</span>
                <span class="step" style="background:#ede9fe;border-color:#5b21b6;">Autoencoder (40%)</span>
                <br>
                <span class="arrow">↓</span><br>
                <span class="step active">Blended Risk Score (1–100)</span>
                <span class="arrow">→</span>
                <span class="step">4-Band Decision Policy</span>
                <br><br>
                <span class="step" style="background:#d1fae5;border-color:#38a169;">✅ Allow (0–45)</span>
                <span class="arrow">|</span>
                <span class="step" style="background:#fef3c7;border-color:#d69e2e;">⚠️ OTP (46–60)</span>
                <span class="arrow">|</span>
                <span class="step" style="background:#fef3c7;border-color:#d69e2e;">⏸️ Hold (61–80)</span>
                <span class="arrow">|</span>
                <span class="step" style="background:#fee2e2;border-color:#991b1b;">🚫 Block (81–100)</span>
            </div>

            <h3>31-Feature Behavioral Vector</h3>
            <ul>
                <li><strong>Keystroke Dynamics:</strong> hold time, latency, typing speed, error rate</li>
                <li><strong>Mouse Kinematics:</strong> velocity, curvature, click timing, scroll patterns</li>
                <li><strong>Session-Level Signals:</strong> idle ratio, event frequency, session duration</li>
            </ul>

            <h3>Ensemble Model</h3>
            <ul>
                <li><strong>Isolation Forest (60% weight):</strong> Isolates points that sit apart from the bulk of normal sessions using random partitioning. Flags anomalies from the very first login with no historical baseline.</li>
                <li><strong>Autoencoder (40% weight):</strong> Learns to reconstruct typical behavioral patterns. Flags sessions where reconstruction error exceeds a 95th-percentile threshold. Sensitive to gradual, mid-session drift (e.g., device changing hands).</li>
            </ul>

            <div class="info-box">
                <strong>🎯 Decision Policy</strong>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px;">
                    <div><strong>0–45:</strong> <span style="color:#38a169;">✅ Allow</span> — Full access</div>
                    <div><strong>46–60:</strong> <span style="color:#d69e2e;">⚠️ OTP Step-Up</span> — Additional verification</div>
                    <div><strong>61–80:</strong> <span style="color:#d69e2e;">⏸️ Hold</span> — Session held for review</div>
                    <div><strong>81–100:</strong> <span style="color:#991b1b;">🚫 Block</span> — Access denied</div>
                </div>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- IMPLEMENTATION STATUS -->
        <!-- ============================================================ -->
        <section>
            <h2>✅ Implementation Status</h2>

            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Feature</th>
                            <th>Code Location</th>
                            <th>What's Implemented</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Behavioral event capture</td>
                            <td><code>login.html JS</code></td>
                            <td>keydown, keyup, mouse move, click, scroll — batched as JSON</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>31-feature extraction</td>
                            <td><code>risk_engine.py</code></td>
                            <td>Hold/latency stats, typing speed, error rate, mouse velocity &amp; curvature, idle ratio, click intervals</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>Isolation Forest scoring</td>
                            <td><code>risk_engine.py</code></td>
                            <td><code>decision_function()</code> → [0,1]; contamination=0.05; 60% ensemble weight</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>Autoencoder scoring</td>
                            <td><code>risk_engine.py</code></td>
                            <td>MAE reconstruction error vs. 95th-percentile threshold; 40% ensemble weight</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>4-band decision policy</td>
                            <td><code>app.py, risk_engine.py</code></td>
                            <td>Allow ≤45 / OTP 46–60 / Hold 61–80 / Block 81–100</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>OTP step-up &amp; block screens</td>
                            <td><code>app.py, otp.html, blocked.html</code></td>
                            <td>Session held pending OTP (demo: 123456); high-risk sessions rendered blocked with score &amp; factors</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>MySQL audit logging</td>
                            <td><code>database.py</code></td>
                            <td>Every session logged: timestamp, user_id, event_count, risk_score, decision, IP, latency_ms</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>Live admin dashboard</td>
                            <td><code>dashboard.html, /api/live-stats</code></td>
                            <td>Auto-refresh every 5s; stats strip + session table with risk bars</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>Silent Duress Detection</td>
                            <td><code>verify.html, app.py</code></td>
                            <td>Facial gesture trigger (wink, blink, etc.) → silently blocks transaction in backend, user sees success</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>Face Transaction Mode</td>
                            <td><code>transfer.html, verify.html</code></td>
                            <td>PIN + Silent Duress: ANY gesture blocks transaction in backend, shows success to user</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>Transaction PIN Verification</td>
                            <td><code>register.html, app.py</code></td>
                            <td>4-digit PIN hashed with SHA-256, verified before every transaction</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>Admin Password Protection</td>
                            <td><code>admin.html, admin_login.html</code></td>
                            <td>Password-protected admin panel with session-based authentication</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                        <tr>
                            <td>Real-time Admin Alerts</td>
                            <td><code>admin.html</code></td>
                            <td>Audio alarm + red blinking alerts for DURESS_BLOCKED transactions</td>
                            <td><span class="status-done">✅ Done</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- TECH STACK -->
        <!-- ============================================================ -->
        <section>
            <h2>💻 Technology Stack</h2>

            <p>
                Each choice favours <strong>simplicity and auditability</strong> over novelty:
                Flask and vanilla JS keep the customer-facing surface easy to review,
                FastAPI gives the risk engine async performance under concurrent scoring,
                and the Autoencoder + Isolation Forest pair (~30 MB combined) is light
                enough for standard servers or later ONNX export to mobile.
            </p>

            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
                <div>
                    <h3>Backend</h3>
                    <ul>
                        <li><strong>Python 3.8+</strong> — Core programming language</li>
                        <li><strong>Flask 2.0+</strong> — Web framework (session, routing)</li>
                        <li><strong>FastAPI</strong> — Stateless risk engine microservice</li>
                        <li><strong>MySQL 8.0+</strong> — Audit database</li>
                        <li><strong>MediaPipe</strong> — Face landmark detection</li>
                        <li><strong>OpenCV</strong> — Video processing</li>
                        <li><strong>XGBoost</strong> — Eye state classification</li>
                        <li><strong>Scikit-learn</strong> — Isolation Forest, StandardScaler</li>
                        <li><strong>TensorFlow / Keras</strong> — Autoencoder</li>
                        <li><strong>NumPy</strong> — Numerical computations</li>
                    </ul>
                </div>
                <div>
                    <h3>Frontend</h3>
                    <ul>
                        <li><strong>HTML5</strong> — Structure</li>
                        <li><strong>CSS3</strong> — Styling</li>
                        <li><strong>Vanilla JavaScript</strong> — Event capture and interactivity</li>
                        <li><strong>Tailwind CSS</strong> — UI framework</li>
                        <li><strong>Material Icons</strong> — Icons</li>
                    </ul>
                    <h3 style="margin-top:16px;">Security</h3>
                    <ul>
                        <li><strong>SHA-256</strong> — Password &amp; PIN hashing</li>
                        <li><strong>Session Management</strong> — User authentication</li>
                        <li><strong>CORS</strong> — Cross-origin requests</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- DEMO CREDENTIALS -->
        <!-- ============================================================ -->
        <section>
            <h2>🔑 Demo Credentials</h2>

            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Username</th>
                            <th>Password</th>
                            <th>Transaction PIN</th>
                            <th>Account Type</th>
                            <th>Balance</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><code>ganesh</code></td>
                            <td><code>Qwertyuiopas12@</code></td>
                            <td><code>1234</code></td>
                            <td>Savings</td>
                            <td>₹245,800.50</td>
                        </tr>
                        <tr>
                            <td><code>pratik</code></td>
                            <td><code>Test@1234</code></td>
                            <td><code>1234</code></td>
                            <td>Savings</td>
                            <td>₹185,420.00</td>
                        </tr>
                        <tr>
                            <td><code>sohel</code></td>
                            <td><code>Loveishappiness12@</code></td>
                            <td><code>1234</code></td>
                            <td>Current</td>
                            <td>₹325,000.00</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="info-box">
                <strong>🔐 Admin Access</strong>
                <p style="margin-top:4px;">
                    URL: <code>/admin</code> &nbsp;|&nbsp; Password: <code>admin@123</code>
                </p>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- INSTALLATION -->
        <!-- ============================================================ -->
        <section>
            <h2>🚀 Installation &amp; Setup</h2>

           
