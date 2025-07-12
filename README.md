# ⚙️ Auto Scaler Dashboard (Basic Metrics Export)

This project sets up a minimal monitoring setup using **Node.js**, **Prometheus**, **Node Exporter**, and **Docker Compose**.  
It is designed to expose basic CPU/Memory metrics which can be scraped and visualized via Prometheus.

---

## 📦 Tech Stack

- Node.js + Express.js
- Prometheus
- Node Exporter
- Docker & Docker Compose

---
## 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/srishti-coder/auto-scaler-dashboard.git
cd auto-scaler-dashboard

# Start all services
docker compose up --build

```
---

## 📦 Final Output

Node API metrics: [http://localhost:3000/metrics](http://localhost:3000/metrics)

### 📸 Metrics Output Screenshot

![Metrics JSON Output](SS1.<img width="1358" height="218" alt="SS1" src="https://github.com/user-attachments/assets/9b50a3c6-f1e2-4b41-8215-4872cb0edbda" />
png)

### 📸 Prometheus Target Screenshot

![Prometheus Scraping Screenshot](ss2.png)<img width="687" height="403" alt="ss2" src="https://github.com/user-attachments/assets/52f1f853-0093-4819-9c72-5a70ac7362ac" />


