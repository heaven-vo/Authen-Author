import json, os
from datetime import datetime
from modules.utils import get_device, now_str, load_json, save_json

DEVICE_DB = "data/device_history.json"

def check_device(username):
    current = get_device()
    now = now_str()
    data = load_json(DEVICE_DB)
    if not isinstance(data, dict):
        data = {}

    history = data.get(username, [])
    if history and history[-1]["device"] != current:
        delta = datetime.now() - datetime.fromisoformat(history[-1]["time"])
        if delta.total_seconds() < 600:
            print("🚨 Suspicious login: new device detected in short time.")

    history.append({"device": current, "time": now})
    data[username] = history[-5:]
    save_json(DEVICE_DB, data)
