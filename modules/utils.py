import json, bcrypt, platform, os
from datetime import datetime

def get_device():
    return platform.node() or "UnknownDevice"

def now_str():
    return datetime.now().isoformat()

def load_json(path):
    if not os.path.exists(path): return []
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def hash_pw(pw):
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()

def verify_pw(pw, hashed):
    return bcrypt.checkpw(pw.encode(), hashed.encode())
