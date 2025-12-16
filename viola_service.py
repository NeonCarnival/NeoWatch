import time
import os
import subprocess
from plyer import notification
from path_config import VIOLA_LOG_PATH

def send_update(msg):
    try:
        notification.notify(title="NeoWatch - Viola", message=msg, app_name="NeoWatch")
    except:
        print(msg)

def monitor_loop():
    send_update("Viola Überwachung gestartet")
    last_mod = 0
    
    # Pfad zum Mesh-Skript (basierend auf deinen Funden)
    mesh_script = "/data/data/com.termux/files/home/vision_p2p/scripts/build_final.sh"

    while True:
        try:
            if os.path.exists(VIOLA_LOG_PATH):
                current_mod = os.path.getmtime(VIOLA_LOG_PATH)
                if current_mod > last_mod:
                    last_mod = current_mod
                    with open(VIOLA_LOG_PATH, 'r') as f:
                        content = f.read()
                        if "FAILOVER" in content:
                            send_update("Failover erkannt! Starte Mesh...")
                            subprocess.Popen(["bash", mesh_script])
            time.sleep(10)
        except Exception as e:
            time.sleep(30)

if __name__ == "__main__":
    monitor_loop()
