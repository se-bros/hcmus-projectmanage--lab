"""Domain exceptions shared across modules — nhiều AC trong backlog yêu cầu
"trả lỗi rõ ràng" khi input/state không hợp lệ; raise các exception này trong
service/router thay vì tự trả JSONResponse rải rác mỗi nơi một kiểu.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    """Base cho mọi lỗi nghiệp vụ có thể trả thẳng cho client."""

    status_code = 400

    def __init__(self, detail: str) -> None:
        self.detail = detail
        super().__init__(detail)


class NotFoundError(AppError):
    status_code = 404


class ValidationError(AppError):
    status_code = 422


class ConflictError(AppError):
    status_code = 409


class UnauthorizedError(AppError):
    status_code = 401


class ForbiddenError(AppError):
    status_code = 403


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppError)
    async def handle_app_error(request: Request, exc: AppError) -> JSONResponse:
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
