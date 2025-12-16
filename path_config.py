import os
def get_viola_log_path():
    termux_path = "/data/data/com.termux/files/home/viola_logic/logs/daily_log_2025-12-16.jsonl"
    apk_path = "/sdcard/NeoWatch/viola_logs.jsonl"
    return apk_path if os.path.exists(apk_path) else termux_path
VIOLA_LOG_PATH = get_viola_log_path()
