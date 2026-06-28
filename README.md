![CI](https://github.com/tirthankar27/RetailIQ/actions/workflows/ci.yml/badge.svg)

# RetailIQ – AI-Powered Customer Intelligence Platform

RetailIQ is a production-inspired full-stack retail analytics platform that transforms raw retail transaction data into actionable business intelligence. It combines customer analytics, machine learning, cloud-native deployment, infrastructure automation, monitoring, and reporting into a single end-to-end application.

---

# Features

## Business Analytics

* KPI Dashboard (Revenue, Orders, Customers, AOV)
* Revenue Trend Analysis
* Top Customers & Products
* Interactive Data Visualizations
* AI-Generated Business Insights

## Customer Intelligence

* RFM Customer Segmentation
* Logistic Regression Churn Prediction
* Churn Probability & Risk Scoring
* High-Risk Customer Identification

## Data Processing

* CSV & Excel Upload
* Dynamic Column Mapping
* Automated Data Validation
* Data Standardization Pipeline

## Reporting

* Executive PDF Report
* Revenue Trend Charts
* KPI Summary
* Customer & Product Analytics
* Top 10 At-Risk Customers
* Churn Analysis

## DevOps & Infrastructure

* Docker Containerization
* Kubernetes Orchestration
* Terraform Infrastructure Provisioning
* Ansible Deployment Automation
* GitHub Actions CI Pipeline
* Redis Caching
* Prometheus Monitoring
* Grafana Dashboards

---

# Architecture

```text
                           GitHub
                              │
                              ▼
                     GitHub Actions (CI)
                              │
                              ▼
                      Docker Images Build
                              │
               ┌──────────────┴──────────────┐
               ▼                             ▼
          Terraform                    Ansible
   (Network & Volumes)         (Deployment Automation)
               │                             │
               └──────────────┬──────────────┘
                              ▼
                       Docker Compose
                              │
                              ▼
                         Minikube Cluster
                              │
                              ▼
                        Kubernetes Pods
                              │
     ┌───────────────┬────────┴─────────┬──────────────┐
     ▼               ▼                  ▼              ▼
  Next.js        FastAPI             PostgreSQL      Redis
                      │
                      ▼
           Prometheus (/metrics)
                      │
                      ▼
                 Grafana Dashboard
```

---

# Technology Stack

## Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

## Backend

* FastAPI
* SQLAlchemy
* Pandas
* Scikit-learn

## Database

* PostgreSQL
* Redis

## Machine Learning

* Logistic Regression
* RFM Analysis
* Feature Engineering
* Churn Prediction

## DevOps

* Docker
* Kubernetes
* Terraform
* Ansible
* GitHub Actions
* Prometheus
* Grafana

---

# Screenshots

## Dashboard Overview

![Dashboard](screenshots/dashboard.png)

## Dataset Upload

![Upload](screenshots/upload.png)

## Column Mapping

![Mapping](screenshots/mapping.png)

## Revenue Analytics

![Revenue](screenshots/revenue_trend.png)

## Customer & Product Analytics

![Analytics](screenshots/customer_product.png)

## AI Business Insights

![Insights](screenshots/ai_insight.png)

## Customer Churn Prediction

![Churn](screenshots/churn.png)

## Grafana Monitoring

![Grafana](screenshots/grafana.png)

## Prometheus Metrics

![Prometheus](screenshots/prometheus.png)

---

# Deployment Workflow

RetailIQ follows a production-inspired deployment pipeline.

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Docker Image Build
    │
    ▼
Terraform
(Network & Volumes)
    │
    ▼
Ansible Playbook
    │
    ▼
Docker Compose
    │
    ▼
Kubernetes Deployment
    │
    ▼
Health Checks
    │
    ▼
Application Available
```

The Ansible playbook automates:

* Environment validation
* Terraform infrastructure provisioning
* Docker Compose deployment
* Minikube startup
* Kubernetes deployment
* Rollout verification
* Service health checks

---

# Local Development

Clone the repository:

```bash
git clone https://github.com/tirthankar27/RetailIQ.git
cd RetailIQ
```

Deploy the complete stack:

```bash
cd ansible

ansible-playbook -i inventory.ini playbook.yml
```

Application URLs:

```text
Frontend   : http://localhost:3000
Backend    : http://localhost:8000
Prometheus : http://localhost:9090
Grafana    : http://localhost:3001
```

Stop the application:

```bash
docker compose down

minikube stop
```

---

# Monitoring

Prometheus collects:

* API Request Count
* Request Latency
* Dashboard Requests
* Report Downloads
* Dataset Uploads

Grafana visualizes:

* Request Traffic
* API Performance
* Business KPIs
* Application Health

---

# Machine Learning Pipeline

1. Upload retail transaction dataset
2. Standardize dataset
3. Generate RFM metrics
4. Engineer customer features
5. Train Logistic Regression model
6. Predict churn probability
7. Rank high-risk customers
8. Display insights in dashboard and PDF reports

---

# Project Highlights

* 12+ FastAPI REST APIs
* 541K+ Retail Transactions Processed
* 4.3K+ Customers Analyzed
* 70% Churn Prediction Accuracy
* Automated Deployment using Terraform & Ansible
* Kubernetes-Orchestrated Microservices
* Infrastructure as Code
* CI Pipeline with GitHub Actions
* Monitoring using Prometheus & Grafana

---

# Author

**Tirthankar Ghosh**

---

# License

This project is intended for educational and portfolio purposes.
