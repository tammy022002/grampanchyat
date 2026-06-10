from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
import logging

logger = logging.getLogger(__name__)

class BusinessRuleException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class NotFoundException(Exception):
    def __init__(self, message: str = "Resource not found"):
        self.message = message
        self.status_code = 404

def setup_exception_handlers(app: FastAPI):
    
    @app.exception_handler(BusinessRuleException)
    async def business_rule_exception_handler(request: Request, exc: BusinessRuleException):
        logger.warning(f"Business Rule Exception: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"success": False, "message": exc.message, "errors": []}
        )
        
    @app.exception_handler(NotFoundException)
    async def not_found_exception_handler(request: Request, exc: NotFoundException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"success": False, "message": exc.message, "errors": []}
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"success": False, "message": str(exc.detail), "errors": []}
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        errors = [{"field": str(err["loc"][-1]), "msg": err["msg"]} for err in exc.errors()]
        return JSONResponse(
            status_code=422,
            content={"success": False, "message": "Validation error", "errors": errors}
        )
        
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled Exception: {exc}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Internal server error", "errors": []}
        )
