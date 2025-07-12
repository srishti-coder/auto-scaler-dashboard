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
