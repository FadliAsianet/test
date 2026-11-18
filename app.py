import time
import requests
from datetime import datetime

print("=== Aplikasi Python di Dalam Docker Mulai Berjalan ===", flush=True)

while True:
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = requests.get("https://httpbin.org", timeout=5)
        print(f"[{waktu}] Sukses konek! Status HTTP: {response.status_code}", flush=True)
    except Exception as e:
        print(f"[{waktu}] Gagal konek: {e}", flush=True)
    
    time.sleep(5)
