import getpass
from datetime import datetime, timedelta
from modules.utils import hash_pw, verify_pw, save_json, now_str, get_device
from modules.password_policy import is_weak, password_expired, reused
from modules.device_tracker import check_device
from modules.logger import log_login, lockouts, attempts, MAX_ATTEMPTS, LOCK_DURATION

USER_DB = "data/users.json"

def force_password_change(users, username):
    while True:
        new_pw = getpass.getpass("New password: ")
        if is_weak(new_pw):
            print("⚠️ Weak password.")
            continue
        hash_new = hash_pw(new_pw)
        history = users[username].get("history", [])
        if reused(hash_new, history):
            print("⛔ Recently used password.")
            continue

        users[username]["password"] = hash_new
        users[username]["last_changed"] = now_str()
        users[username]["must_change"] = False
        users[username]["history"] = history[-2:] + [hash_new]
        save_json(USER_DB, users)
        print("✅ Password updated.")
        break

def login(users):
    username = input("Username: ")
    user = users.get(username)
    if not user:
        print("❌ User not found."); return

    if username in lockouts:
        if datetime.now() < lockouts[username]:
            print("⛔ Account temporarily locked.")
            return
        else:
            del lockouts[username]; attempts[username] = 0

    pw = getpass.getpass("Password: ")
    if verify_pw(pw, user["password"]):
        attempts[username] = 0
        log_login(username, "SUCCESS", user["role"])
        check_device(username)

        if user.get("must_change") or password_expired(user):
            print("🔁 You must change your password.")
            force_password_change(users, username)
        print(f"✅ Welcome, {username}. Role: {user['role']}")
    else:
        attempts[username] = attempts.get(username, 0) + 1
        log_login(username, "FAIL", user["role"])
        print("❌ Wrong password.")
        if attempts[username] >= MAX_ATTEMPTS:
            lockouts[username] = datetime.now() + LOCK_DURATION
            print("🔒 Too many failed attempts. Locked temporarily.")

def register(users):
    username = input("New username: ")
    if username in users:
        print("⚠️ Already exists."); return

    while True:
        pw = getpass.getpass("New password: ")
        if is_weak(pw): print("⚠️ Weak password."); continue
        confirm = getpass.getpass("Confirm password: ")
        if pw != confirm: print("❌ Mismatch."); continue
        break

    role = input("Role (Admin/User/Guest): ")
    h = hash_pw(pw)
    users[username] = {
        "password": h,
        "role": role,
        "last_changed": now_str(),
        "must_change": True,
        "history": [h]
    }
    save_json(USER_DB, users)
    print("✅ User created.")
