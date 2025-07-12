import time
import requests
import subprocess

PROMETHEUS_URL = "http://prometheus:9090/api/v1/query"
CPU_THRESHOLD = 0.7
MAX_CONTAINERS = 5
existing = 1

def get_cpu_load():
    try:
        result = requests.get(PROMETHEUS_URL, params={"query": "avg(rate(node_load1[1m]))"}).json()
        value = float(result['data']['result'][0]['value'][1])
        return value
    except Exception as e:
        print("Error fetching CPU load:", e)
        return 0

def scale_container():
    global existing
    if existing >= MAX_CONTAINERS:
        print("Max containers running. No scaling.")
        return
    name = f"stress-sim-{existing}"
    cmd = ["docker", "run", "-d", "--name", name, "stress-sim"]
    subprocess.run(cmd)
    print(f"[+] Scaled: Started {name}")
    existing += 1

if __name__ == "__main__":
    print("AutoScaler started...")
    while True:
        cpu = get_cpu_load()
        print(f"[METRIC] CPU Load: {cpu}")
        if cpu > CPU_THRESHOLD:
            print("[!] High CPU Load Detected")
            scale_container()
        time.sleep(10)
