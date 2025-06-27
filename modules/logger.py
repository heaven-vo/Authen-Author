import json
from datetime import datetime, timedelta
from modules.utils import load_json, save_json, now_str, get_device

LOG_DB = "data/login_log.json"
MAX_ATTEMPTS = 3
LOCK_DURATION = timedelta(minutes=5)

lockouts = {}        # username → unlock_time (datetime obj)
attempts = {}        # username → fail count

def log_login(username, status, role="N/A"):
    logs = load_json(LOG_DB) or []
    logs.append({
        "time": now_str(),
        "user": username,
        "device": get_device(),
        "status": status,
        "role": role
    })
    save_json(LOG_DB, logs)
