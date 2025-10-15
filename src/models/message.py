"""Pydantic models for Message request and response schemas."""

from pydantic import BaseModel, Field


class MessageResponse(BaseModel):
    """Response model for endpoints that return a message.

    Attributes:
        message: The message string to return.
    """

    message: str = Field(..., min_length=1, description="The response message")
