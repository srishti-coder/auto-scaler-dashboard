# load.py
import time
import threading

def cpu_stress():
    while True:
        pass  # infinite loop - max CPU use

def start_stress_threads(n):
    threads = []
    for _ in range(n):
        t = threading.Thread(target=cpu_stress)
        t.start()
        threads.append(t)

    print(f"[+] Started {n} CPU stress threads")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[-] Stopping stress test")

if __name__ == "__main__":
    thread_count = 4  # Number of CPU stress threads
    start_stress_threads(thread_count)
