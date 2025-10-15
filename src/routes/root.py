"""Root routes for the FastAPI application."""

from fastapi import APIRouter

from ..settings import settings
from ..models.message import MessageResponse

router = APIRouter()


@router.get("/", response_model=MessageResponse)
async def root() -> MessageResponse:
    """Root endpoint returning a welcome message.

    Returns:
        MessageResponse: A response containing a welcome message.
    """
    return MessageResponse(message=settings.message)
