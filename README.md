# Auto Scaler Dashboard (Basic Metrics Export)

This project sets up a basic monitoring dashboard using **Prometheus**, **Node.js**, and **Docker Compose**.

The system includes:
- A `node-api` server exposing a `/metrics` endpoint
- Prometheus scraping metrics from the `node-api`
- Node Exporter for host-level metrics

## 🔧 Stack

- Node.js
- Express.js
- Prometheus
- Docker + Docker Compose

## 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/srishti-coder/auto-scaler-dashboard.git
cd auto-scaler-dashboard

# Start all services
docker compose up --build
