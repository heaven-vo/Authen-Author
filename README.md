# Secure CLI Login System

A authentication system built in Python to simulate secure user login workflows including authentication, role-based access control, password security policies, account lockout, anomaly detection, and detailed login logging. Ideal for cybersecurity beginners to practice core IAM and defense concepts.

---

##  Features

- User authentication with bcrypt password hashing
- Role-based authorization (Admin / User / Guest)
- Password strength enforcement (length, complexity, common password blocklist)
- Forced password changes (first-time login or every 90 days)
- Password history (prevent reuse of last 3 passwords)
- Lock account after multiple failed login attempts (with auto unlock)
- Anomaly detection: alerts when login occurs from an unfamiliar device within 10 minutes
- Logging: JSON-based login records including time, device, result, and user role
- Modular architecture for reusability and scalability
- Setup script auto-creates necessary folders/files on first run

---

##  Project Structure

  ├── main.py
  
  ├── modules/
  
  │   ├── auth.py
  
  │   ├── password_policy.py
  
  │   ├── logger.py
  
  │   ├── device_tracker.py
  
  │   └── utils.py
  
  ├── data/
  
  │   ├── users.json   
  
  │   ├── login_log.json 
  
  │   └── device_history.json     


## Usage Flow
- Register a new user with strong password
- Login with CLI prompt
- If logging in from new device → receive warning
- If password is expired or first-time login → system forces update
- After 3 failed attempts → account temporarily locked
- All activities logged into JSON log file

## Security Concepts Practiced
- Authentication	           ||     Username + bcrypt password
- Authorization (RBAC)	     ||     Roles: Admin, User, Guest
- Password Policy	           ||     Strength enforcement, expiry, reuse tracking
- Lockout Mechanism	         ||     Lock after X failures, auto reset after 5 min
- Anomaly Detection	         ||     Alerts on rapid multi-device login attempts
- Logging & Audit Trail	     ||     JSON logs with full metadata

## Author
Heaven Vo Entry Level CyberSecurity

