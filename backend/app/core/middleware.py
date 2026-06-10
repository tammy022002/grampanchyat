from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
import logging
from typing import Callable

logger = logging.getLogger(__name__)

class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()
        
        # Log request basic details
        # For actual entity audit, it should be handled in services/SQLAlchemy events
        # This is for HTTP access audit logging
        client_ip = request.client.host if request.client else "unknown"
        method = request.method
        url = request.url.path
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        status_code = response.status_code
        
        # In a real system, send this to logstash or a fast append-only DB log
        logger.info(
            f"Audit Log: IP: {client_ip} | Method: {method} | "
            f"Path: {url} | Status: {status_code} | Time: {process_time:.4f}s"
        )
        
        return response
