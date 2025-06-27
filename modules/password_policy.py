import re
from datetime import datetime, timedelta

COMMON = ["123456", "password", "admin", "qwerty"]

def is_weak(pw):
    return (
        len(pw) < 8 or
        pw.lower() in COMMON or
        not re.search(r'[A-Z]', pw) or
        not re.search(r'[a-z]', pw) or
        not re.search(r'\d', pw) or
        not re.search(r'[\W_]', pw)
    )

def password_expired(user):
    last = user.get("last_changed")
    if not last: return True
    return datetime.now() - datetime.fromisoformat(last) > timedelta(days=90)

def reused(new_hash, history):
    return new_hash in history[-3:] if history else False
