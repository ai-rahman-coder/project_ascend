from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.ai_exceptions import ProviderUnavailableError

def provider_unavailable_handler(request: Request, exc: ProviderUnavailableError):
    return JSONResponse(
        status_code=503,
        content={
            "error": "AI_PROVIDER_UNAVAILABLE",
            "message": str(exc)
        }
    )


def unauthorized_access_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=401,
        content={
            "error": "UNAUTHORIZED_ACCESS",
            "message": str(exc)
        }
    )