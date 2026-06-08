# RetailIQ - Customer Intelligence Platform

RetailIQ is a full-stack analytics platform that transforms raw retail transaction datasets into actionable business insights.

Users can upload CSV or Excel datasets, map columns automatically, generate customer segmentation, analyze revenue trends, identify top customers and products, and export executive PDF reports.

---

## Features

### Dataset Upload

* Upload CSV, XLS, and XLSX files
* Automatic file validation
* Dataset preview before processing

### Smart Column Detection

* Automatic schema detection using fuzzy matching
* Detects:

  * Customer ID
  * Transaction Date
  * Quantity
  * Unit Price
  * Product

### Customer Analytics

* RFM-based customer segmentation
* Champions
* Loyal Customers
* Potential Loyalists
* At Risk Customers
* Others

### Business Intelligence Dashboard

* Revenue KPIs
* Order KPIs
* Customer KPIs
* Average Order Value
* Revenue trend visualization
* Customer segmentation charts

### Customer Insights

* Top revenue-generating customers
* Top revenue-generating products
* Automatically generated business insights

### Executive PDF Reports

* KPI summary tables
* Revenue trend charts
* Customer insights
* Product performance
* Executive-ready reporting

---

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS
* Recharts
* Axios

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pandas
* RapidFuzz
* ReportLab
* Matplotlib

---

## Project Structure

```text
Customer-Intelligence-Platform/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database/
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── reports/
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── package.json
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>

cd Customer-Intelligence-Platform
```

---

## Backend Setup

Create virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run development server:

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:3000
```

---

## Workflow

### 1. Upload Dataset

Upload retail transaction data.

### 2. Review Column Mapping

RetailIQ automatically detects:

* Customer ID
* Date
* Quantity
* Price
* Product

Users can adjust mappings manually.

### 3. Generate Dashboard

The platform computes:

* Revenue
* Orders
* Customers
* Average Order Value
* Segments
* Top Customers
* Top Products

### 4. Download Report

Generate an executive PDF report containing:

* KPI Summary
* Revenue Trend
* Business Insights
* Top Customers
* Top Products

---

## Sample Dataset

The project was tested using the UCI Online Retail Dataset.

Columns:

```text
InvoiceNo
StockCode
Description
Quantity
InvoiceDate
UnitPrice
CustomerID
Country
```

---

## Future Enhancements

* Authentication & User Management
* Historical Dashboard Tracking
* Churn Prediction
* Customer Lifetime Value Prediction
* AI Chat Assistant for Dataset Queries
* Multi-Dataset Comparison
* Scheduled Report Generation
* Cloud Deployment

---

## Screenshots

Add screenshots of:

* Upload Page
* Mapping Page
* Analytics Dashboard
* PDF Report

---

## Author

Tirthankar Ghosh

B.Tech, National Institute of Technology Sikkim

Customer Intelligence Platform built using FastAPI, PostgreSQL, Next.js, and Tailwind CSS.
