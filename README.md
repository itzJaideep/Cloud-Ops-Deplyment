# devops-intern-final
DevOps workflow demonstrating Git, Linux scripting, Docker containerization, CI/CD with GitHub Actions, Nomad job deployment, and Grafana Loki monitoring. Includes scripts, configs, and documentation to replicate a complete, automated DevOps pipeline.

=> [![CI Pipeline](https://github.com/itzJaideep/devops-intern-final/actions/workflows/ci.yml/badge.svg)](https://github.com/itzJaideep/devops-intern-final/actions/workflows/ci.yml)

---

# 🚀 2. Cloud-Ops Deploy – README

```md
# ⚙️ Cloud-Ops Deploy – Containerized CI/CD & Orchestration System

## 📌 Overview
Cloud-Ops Deploy is a container-based deployment system that automates application build, deployment, and monitoring using Docker, GitHub Actions, and Nomad.

It ensures consistent deployments and improves reliability by using containerization and orchestration.

---

## ⚙️ Architecture
GitHub Repository → GitHub Actions → Docker Build → Container Registry  
                                          ↓  
                                      Nomad Cluster  
                                          ↓  
                                      Running Containers  
                                          ↓  
                                   Grafana Loki (Logs)  

---

## 🔧 Tech Stack
- Docker (Containerization)
- GitHub Actions (CI/CD)
- Nomad (Orchestration)
- Grafana Loki (Logging)
- Linux

---

## 🔄 CI/CD Workflow
- Trigger: Push to repository  
- Build: Docker image created  
- Deploy: Container scheduled via Nomad  
- Logs: Centralized using Grafana Loki  

---

## 🧪 How to Run
```bash
git clone https://github.com/itzJaideep/Cloud-Ops-Deplyment.git
cd Cloud-Ops-Deplyment

# Build Docker image
docker build -t cloudops-app .

# Run container
docker run -p 8080:8080 cloudops-app
