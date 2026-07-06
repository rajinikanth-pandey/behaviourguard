# 🛡️ BehaviorGuard AI - Silent Duress Detection System

<div align="center">

![BehaviorGuard AI Banner](https://img.shields.io/badge/BehaviorGuard-AI-blue?style=for-the-badge&logo=python)
![Version](https://img.shields.io/badge/version-1.0.0-green?style=flat-square)
![Python](https://img.shields.io/badge/python-3.8+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey?style=flat-square&logo=flask)
![MySQL](https://img.shields.io/badge/mysql-8.0+-orange?style=flat-square&logo=mysql)
![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)

**An intelligent banking security system that protects users during duress situations using facial gesture recognition.**

[Features](#-key-features) • [Demo](#-demo-credentials) • [Installation](#-installation--setup) • [Tech Stack](#-tech-stack) • [Contributing](#-contributing)

</div>

---

## 📌 Overview

**BehaviorGuard AI** is a revolutionary banking security solution that enables customers to **silently alert authorities** during duress situations while appearing to complete transactions normally. By combining **computer vision**, **real-time gesture detection**, and **behavioral risk scoring**, the system provides an invisible layer of security that traditional banking apps lack.

### The Problem It Solves

Traditional banking apps lack a way for customers to discreetly signal when they are under duress (e.g., being forced to make a transaction). If a customer tries to call for help or act suspiciously, the perpetrator may become violent. BehaviorGuard AI solves this by:

- 🔒 **Allowing customers to silently signal distress** using simple gestures (wink, blink, etc.)
- 🎭 **Showing a "Transaction Successful" message** to the perpetrator - they never know an alert was triggered
- 🚨 **Instantly notifying security teams** through a dedicated admin dashboard
- ✅ **Blocking the transaction in the background** while the user appears to complete it

---

## 🎯 Key Features

### 👤 Face Transaction Mode
- User enters transaction PIN first
- Camera opens for facial verification
- **ANY gesture** (wink, blink, head movement) silently blocks the transaction
- User sees a **"Transaction Successful"** message - perpetrator is unaware of the alert

### 🔑 PIN Transaction Mode
- Standard PIN-only verification
- No camera required
- Faster processing for routine transactions

### 🛡️ Security Operations Center (Admin Panel)
- **Password-protected** admin dashboard
- **Real-time duress alerts** with audio alarm
- **Live camera feed** monitoring
- **Alert acknowledgment** system
- Complete transaction history

### 📊 Analytics Dashboard
- Real-time transaction statistics
- Risk score visualization
- User session history
- Duress alert timeline

---

## 🚀 Demo Credentials

### User Accounts

| Username | Password | Transaction PIN | Account Type | Balance |
|----------|----------|-----------------|--------------|---------|
| ganesh | Qwertyuiopas12@ | 1234 | Savings | ₹245,800.50 |
| pratik | Test@1234 | 1234 | Savings | ₹185,420.00 |
| sohel | Loveishappiness12@ | 1234 | Current | ₹325,000.00 |

### Admin Access
- **URL**: `http://localhost:5000/admin`
- **Password**: `admin@123`

---

## 🏗️ System Architecture

### High-Level Flow

```mermaid
graph TD
    A[User Logs In] --> B[Home Dashboard]
    B --> C[Transfer Money]
    C --> D{Choose Method}
    D -->|Face Transaction| E[Enter PIN]
    D -->|PIN Transaction| F[Enter PIN]
    E --> G[Camera Opens]
    G --> H{Any Gesture?}
    H -->|Yes| I[Backend: Block Transaction]
    H -->|No| J[Process Transaction]
    I --> K[User Sees Success ✅]
    J --> K
    I --> L[Admin Alert 🚨]
    L --> M[Security Team Notified]
    K --> N[Transaction Complete]
