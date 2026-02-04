Two-Factor Authentication (OTP-Based)

📌 Overview
This project implements a basic **Two-Factor Authentication (2FA)** system using **One-Time Passwords (OTP)** in Python.

It simulates the real-world authentication flow without relying on external SMS or email services.



🔐 Features
- 6-digit OTP generation
- OTP expiry handling
- Credential verification
- Simulated OTP delivery
- Protection against reuse



⚙️ Tech Stack
- Python
- Random number generation
- Time-based validation

---

🚀 Authentication Flow
1. User enters username and password
2. System generates a one-time password
3. OTP is validated within a time window
4. Authentication succeeds or fails

---

## ▶️ How to Run

```bash
python otp_auth.py
