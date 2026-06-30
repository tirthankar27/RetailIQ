# RetailIQ – AI-Powered Customer Intelligence Platform

RetailIQ is a production-inspired full-stack retail analytics platform that transforms raw retail transaction data into actionable business intelligence. It combines customer analytics, machine learning, cloud-native deployment, infrastructure automation, monitoring, and reporting into a single end-to-end application.

---

# Features

## Business Analytics

- KPI Dashboard (Revenue, Orders, Customers, AOV)
- Revenue Trend Analysis
- Top Customers & Products
- Interactive Data Visualizations
- AI-Generated Business Insights

## Customer Intelligence

- RFM Customer Segmentation
- Logistic Regression Churn Prediction
- Churn Probability & Risk Scoring
- High-Risk Customer Identification

## Data Processing

- CSV & Excel Upload
- Dynamic Column Mapping
- Automated Data Validation
- Data Standardization Pipeline

## Reporting

- Executive PDF Report
- Revenue Trend Charts
- KPI Summary
- Customer & Product Analytics
- Top 10 At-Risk Customers
- Churn Analysis

## DevOps & Infrastructure

- Docker Containerization
- Kubernetes Orchestration
- Terraform Infrastructure Provisioning
- Ansible Deployment Automation
- Jenkins Continuous Integration
- Redis Caching
- Prometheus Monitoring
- Grafana Dashboards

---

# Architecture

```text
                           GitHub
                              │
                              ▼
                        Jenkins (CI)
                              │
                              ▼
                     Code Verification
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

- Next.js
- React
- TypeScript
- Tailwind CSS

## Backend

- FastAPI
- SQLAlchemy
- Pandas
- Scikit-learn

## Database

- PostgreSQL
- Redis

## Machine Learning

- Logistic Regression
- RFM Analysis
- Feature Engineering
- Churn Prediction

## DevOps

- Docker
- Kubernetes
- Terraform
- Ansible
- Jenkins
- Prometheus
- Grafana

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

# CI/CD Pipeline

RetailIQ follows a production-inspired CI/CD workflow.

### Continuous Integration (Jenkins)

Jenkins automatically validates every code change by performing:

- Environment verification
- Backend dependency installation
- Backend syntax validation
- Frontend dependency installation
- ESLint checks
- Production build verification

### Continuous Deployment (Ansible)

After successful CI validation, Ansible automates deployment by:

- Environment validation
- Terraform infrastructure provisioning
- Docker Compose deployment
- Kubernetes deployment
- Rollout verification
- Service health checks

---

# Deployment Workflow

```text
Developer
    │
    ▼
Git Push
    │
    ▼
Jenkins (CI)
    │
    ▼
Code Verification
    │
    ▼
Ansible Playbook
    │
    ├── Environment Checks
    ├── Terraform Infrastructure
    ├── Docker Compose Deployment
    ├── Kubernetes Deployment
    ├── Rollout Verification
    └── Health Checks
    │
    ▼
Application Available
```

---

# Local Development

Clone the repository:

```bash
git clone https://github.com/tirthankar27/RetailIQ.git
cd RetailIQ
```

Provision infrastructure:

```bash
cd terraform

terraform init
terraform apply
```

Deploy the complete application:

```bash
cd ../ansible

ansible-playbook -i inventory.ini playbook.yml
```

Run the Jenkins server:

```bash
docker compose up -d jenkins
```

Open Jenkins:

```text
http://localhost:8080
```

Application URLs:

```text
Frontend    : http://localhost:3000
Backend     : http://localhost:8000
API Docs    : http://localhost:8000/docs
Prometheus  : http://localhost:9090
Grafana     : http://localhost:3001
Jenkins     : http://localhost:8080
```

Stop the application:

```bash
docker compose down

minikube stop
```

---

# Monitoring

Prometheus collects:

- API Request Count
- Request Latency
- Dashboard Requests
- Report Downloads
- Dataset Uploads

Grafana visualizes:

- Request Traffic
- API Performance
- Business KPIs
- Application Health

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

- 12+ FastAPI REST APIs
- 541K+ Retail Transactions Processed
- 4.3K+ Customers Analyzed
- 70% Churn Prediction Accuracy
- Automated Infrastructure using Terraform
- Automated Deployment using Ansible
- Kubernetes-Orchestrated Microservices
- Infrastructure as Code (IaC)
- Continuous Integration using Jenkins
- Monitoring using Prometheus & Grafana

---

# Project Structure

```text
RetailIQ
│
├── backend/
├── frontend/
├── ansible/
│   ├── inventory.ini
│   ├── playbook.yml
│   └── roles/
├── terraform/
├── jenkins/
├── k8s/
├── monitoring/
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

---

# Author

**Tirthankar Ghosh**

B.Tech Computer Science & Engineering  
National Institute of Technology Sikkim

---

# License

This project is intended for educational and portfolio purposes.