from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.upload import router as upload_router
from app.api.analyze import router as analyze_router
from app.api.mapping import router as mapping_router
from app.api.analytics import router as analytics_router
from app.api.rfm import router as rfm_router
from app.api.segments import router as segments_router
from app.api.dashboard import router as dashboard_router
from app.api.revenue import router as revenue_router
from app.api.customer import router as customer_router
from app.api.product import router as product_router
from app.api.insights import router as insights_router
from app.api.report import router as report_router

app = FastAPI(
    title="Customer Intelligence Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    upload_router,
    prefix="/api",
    tags=["Upload"]
)

app.include_router(
    analyze_router,
    prefix="/api"
)

app.include_router(
    mapping_router,
    prefix="/api"
)

app.include_router(
    analytics_router,
    prefix="/api"
)

app.include_router(
    rfm_router,
    prefix="/api"
)

app.include_router(
    segments_router,
    prefix="/api"
)

app.include_router(
    dashboard_router,
    prefix="/api"
)

app.include_router(
    revenue_router,
    prefix="/api"
)

app.include_router(
    customer_router,
    prefix="/api"
)

app.include_router(
    product_router,
    prefix="/api"
)

app.include_router(
    insights_router,
    prefix="/api"
)

app.include_router(
    report_router,
    prefix="/api"
)

@app.get("/")
def home():
    return {
        "message": "API Running"
    }