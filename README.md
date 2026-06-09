# RetailIQ - Customer Intelligence Platform

A full-stack customer intelligence platform that enables organizations to collect, analyze, and visualize customer data to gain actionable business insights.

## Features

* Customer data management
* Data upload and processing
* Interactive analytics dashboard
* Customer segmentation
* Trend analysis and reporting
* Secure authentication and authorization
* Responsive web interface
* RESTful API backend

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* Python
* Flask/FastAPI
* PostgreSQL

### DevOps & Deployment

* Docker
* Kubernetes
* GitHub

## Project Structure

```text
Customer-Intelligence-Platform/
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   └── ...
├── backend/
│   ├── api/
│   ├── models/
│   ├── services/
│   └── ...
├── k8s/
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   └── ...
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Customer-Intelligence-Platform
```

### Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend

npm install
```

## Running the Application

### Start Backend

```bash
cd backend

python app.py
```

### Start Frontend

```bash
cd frontend

npm run dev
```

Frontend:

```text
http://localhost:3000
```

Backend:

```text
http://localhost:5000
```

## Docker

Build and run containers:

```bash
docker compose up --build
```

## Kubernetes

Apply Kubernetes resources:

```bash
kubectl apply -f k8s/
```

## Future Enhancements

* Machine learning-based customer insights
* Predictive analytics
* Real-time data streaming
* Advanced reporting and exports
* Role-based access control

## Contributors

* Tirthankar Ghosh

## License

This project is intended for educational and development purposes.
