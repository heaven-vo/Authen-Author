import os
import json

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def ensure_file(path, default_data):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default_data, f, indent=2)

def setup_environment():
    ensure_dir("data")
    ensure_file("data/users.json", {})
    ensure_file("data/login_log.json", [])
    ensure_file("data/device_history.json", [])