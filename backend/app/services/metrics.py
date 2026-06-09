from prometheus_client import (
    Counter,
    Histogram
)

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total API Requests"
)

REQUEST_LATENCY = Histogram(
    "api_request_duration_seconds",
    "API Request Duration"
)

DASHBOARD_REQUESTS = Counter(
    "dashboard_requests_total",
    "Dashboard Requests"
)

REPORT_DOWNLOADS = Counter(
    "report_downloads_total",
    "PDF Downloads"
)

UPLOADS = Counter(
    "uploads_total",
    "Dataset Uploads"
)