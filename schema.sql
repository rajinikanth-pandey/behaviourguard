-- =====================================================
-- BehaviorGuard Database Schema (Complete)
-- =====================================================

-- Drop database if exists and create fresh
DROP DATABASE IF EXISTS behaviorguard1;
CREATE DATABASE behaviorguard1;
USE behaviorguard1;

-- =====================================================
-- Table: users (Complete with transaction_pin)
-- =====================================================
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(64) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    account_type VARCHAR(30) DEFAULT 'Savings',
    balance DECIMAL(12,2) DEFAULT 100000.00,
    email VARCHAR(100),
    phone VARCHAR(20),
    transaction_pin VARCHAR(64) DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- Table: login_sessions
-- =====================================================
CREATE TABLE login_sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    event_count INT DEFAULT 0,
    risk_score FLOAT DEFAULT -1,
    decision VARCHAR(20) DEFAULT 'pending',
    ip_address VARCHAR(50) DEFAULT '',
    latency_ms FLOAT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- =====================================================
-- Table: transactions
-- =====================================================
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    recipient_name VARCHAR(100) NOT NULL,
    account_number VARCHAR(30) NOT NULL,
    ifsc_code VARCHAR(20) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    purpose VARCHAR(100),
    status VARCHAR(30) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- =====================================================
-- Insert Demo Users (with transaction_pin = 1234)
-- =====================================================
INSERT INTO users (
    username,
    password_hash,
    full_name,
    account_number,
    account_type,
    balance,
    email,
    phone,
    transaction_pin
) VALUES 
(
    'ganesh',
    SHA2('Qwertyuiopas12@', 256),
    'Ganesh Kumar',
    '4587123412341234',
    'Savings',
    245800.50,
    'ganesh@gmail.com',
    '9876543210',
    SHA2('1234', 256)
),
(
    'pratik',
    SHA2('Test@1234', 256),
    'Pratik Sharma',
    '4587123412341235',
    'Savings',
    185420.00,
    'pratik@gmail.com',
    '9876543211',
    SHA2('1234', 256)
),
(
    'sohel',
    SHA2('Loveishappiness12@', 256),
    'Sohel Khan',
    '4587123412341236',
    'Current',
    325000.00,
    'sohel@gmail.com',
    '9876543212',
    SHA2('1234', 256)
);

-- =====================================================
-- Insert Sample Transactions
-- =====================================================
INSERT INTO transactions (
    user_id,
    recipient_name,
    account_number,
    ifsc_code,
    amount,
    purpose,
    status
) VALUES 
(
    1,
    'John Smith',
    '1234567890123456',
    'SBIN0001234',
    5000.00,
    'Payment',
    'SUCCESS'
),
(
    1,
    'Amazon India',
    '2345678901234567',
    'HDFC0005678',
    1500.00,
    'Bill Payment',
    'SUCCESS'
),
(
    2,
    'Electricity Board',
    '3456789012345678',
    'ICIC0009012',
    3200.00,
    'Bill Payment',
    'SUCCESS'
),
(
    1,
    'Rental Payment',
    '4567890123456789',
    'SBIN0009012',
    25000.00,
    'Rent',
    'SUCCESS'
),
(
    2,
    'Flipkart',
    '5678901234567890',
    'HDFC0001234',
    4500.00,
    'Payment',
    'SUCCESS'
),
(
    3,
    'Swiggy',
    '6789012345678901',
    'ICIC0005678',
    1200.00,
    'Payment',
    'SUCCESS'
),
(
    1,
    'Suspicious Transfer',
    '7890123456789012',
    'SBIN0009999',
    150000.00,
    'Transfer',
    'DURESS_BLOCKED'
);

-- =====================================================
-- Insert Sample Login Sessions
-- =====================================================
INSERT INTO login_sessions (
    user_id,
    timestamp,
    event_count,
    risk_score,
    decision,
    ip_address,
    latency_ms
) VALUES 
(
    1,
    DATE_SUB(NOW(), INTERVAL 1 DAY),
    25,
    12.5,
    'allow',
    '192.168.1.100',
    45.2
),
(
    1,
    DATE_SUB(NOW(), INTERVAL 2 DAY),
    18,
    8.3,
    'allow',
    '192.168.1.100',
    32.1
),
(
    2,
    DATE_SUB(NOW(), INTERVAL 1 DAY),
    32,
    45.8,
    'otp',
    '192.168.1.101',
    67.5
),
(
    3,
    DATE_SUB(NOW(), INTERVAL 3 HOUR),
    42,
    78.2,
    'block',
    '192.168.1.102',
    89.3
);

-- =====================================================
-- Verify All Data
-- =====================================================
SELECT '=== USERS ===' AS '';
SELECT id, username, full_name, account_number, account_type, balance, email, phone, 
       CASE WHEN transaction_pin IS NOT NULL THEN '✅ Set' ELSE '❌ Not Set' END as pin_status
FROM users;

SELECT '=== TRANSACTIONS ===' AS '';
SELECT id, user_id, recipient_name, account_number, amount, purpose, status, created_at 
FROM transactions 
ORDER BY created_at DESC;

SELECT '=== LOGIN SESSIONS ===' AS '';
SELECT id, user_id, timestamp, event_count, risk_score, decision, ip_address, latency_ms 
FROM login_sessions 
ORDER BY timestamp DESC;

-- =====================================================
-- Useful Queries for Admin
-- =====================================================
SELECT '=== USER STATISTICS ===' AS '';
SELECT 
    u.id,
    u.username,
    u.full_name,
    u.balance,
    COUNT(t.id) as total_transactions,
    SUM(CASE WHEN t.status = 'SUCCESS' THEN 1 ELSE 0 END) as successful_txns,
    SUM(CASE WHEN t.status = 'DURESS_BLOCKED' THEN 1 ELSE 0 END) as blocked_txns
FROM users u
LEFT JOIN transactions t ON u.id = t.user_id
GROUP BY u.id, u.username, u.full_name, u.balance;

SELECT '=== ACTIVE DURESS ALERTS ===' AS '';
SELECT 
    t.id,
    u.username,
    u.full_name,
    t.recipient_name,
    t.amount,
    t.purpose,
    t.created_at
FROM transactions t
JOIN users u ON t.user_id = u.id
WHERE t.status = 'DURESS_BLOCKED'
ORDER BY t.created_at DESC;