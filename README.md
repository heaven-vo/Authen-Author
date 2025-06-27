# 🔐 Secure CLI Login System — Advanced Cybersecurity Edition

A command-line authentication system built in Python to simulate secure user login workflows including authentication, role-based access control, password security policies, account lockout, anomaly detection, and detailed login logging. Ideal for cybersecurity beginners to practice core IAM and defense concepts.

---

## 📌 Features

- ✅ User authentication with bcrypt password hashing
- 🧑‍💻 Role-based authorization (Admin / User / Guest)
- 🔁 Password strength enforcement (length, complexity, common password blocklist)
- 🔄 Forced password changes (first-time login or every 90 days)
- 🧠 Password history (prevent reuse of last 3 passwords)
- ⛔ Lock account after multiple failed login attempts (with auto unlock)
- 🚨 Anomaly detection: alerts when login occurs from an unfamiliar device within 10 minutes
- 🧾 Logging: JSON-based login records including time, device, result, and user role
- 🛠️ Modular architecture for reusability and scalability
- 📂 Setup script auto-creates necessary folders/files on first run

---

## 🧱 Project Structure

