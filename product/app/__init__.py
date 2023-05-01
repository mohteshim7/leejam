from http import HTTPStatus
import logging
import sys

from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
# from databases import Database
# from core.config import config
from core.exceptions import CustomException
from core.fastapi.dependencies import Logging
import time
import os

logger = logging.getLogger("app_initialize")
logger.setLevel(level=logging.INFO)
# rate limit
# from core.fastapi.middlewares.limiter import set_limiter_state

# application routers
from app.views import categories_app, product_app, cart_app

global db


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routers(app: FastAPI) -> None:
    app.include_router(categories_app, tags=["categories"])
    app.include_router(product_app, tags=["product"])
    app.include_router(cart_app, tags=["carts"])


def init_listeners(app: FastAPI) -> None:
    # Exception handler
    @app.exception_handler(CustomException)
    async def custom_exception_haRateLimitExceededndler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def on_auth_error(request: Request, exc: Exception):
    status_code, error_code, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message

    return JSONResponse(
        status_code=status_code, content={
            "error_code": error_code, "message": message},
    )


def init_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    pass


def create_app() -> FastAPI:
    app = FastAPI(
        title="PRODUCT MANAGER",
        description="PRODUCT MANAGER  is a service which is able to manage PRODUCT purchange adding point deleting add all of Client Customers ZAPS LOYALTY SYSTEM",
        version="1.0.0",
        dependencies=[Depends(Logging)],
    )
    init_middleware(app=app)
    init_routers(app=app)
    init_cors(app=app)
    init_listeners(app=app)
    return app


log = logging.getLogger(__name__)

app = create_app()