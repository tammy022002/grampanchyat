from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.api import api_router
from app.core.config import settings
from app.core.exceptions import setup_exception_handlers
from app.core.middleware import AuditMiddleware

# Imports for routers will go here as we build them

def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Setup global exceptions
    setup_exception_handlers(app)

    # Add Custom Middlewares
    app.add_middleware(AuditMiddleware)

    # Instrument for Prometheus
    Instrumentator().instrument(app).expose(app)

    @app.get("/health", tags=["System"])
    def health_check():
        return {"status": "ok", "environment": settings.ENVIRONMENT}
        
    app.include_router(api_router, prefix=settings.API_V1_STR)
    
    return app

app = get_application()
