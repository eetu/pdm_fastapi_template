"""Tests for the MessageResponse Pydantic model."""

import pytest
from pydantic import ValidationError

from .message import MessageResponse


def test_message_response_valid():
    """Test that MessageResponse accepts valid data."""
    message = MessageResponse(message="Hello World!")
    assert message.message == "Hello World!"
    assert isinstance(message.message, str)


def test_message_response_empty_string_fails():
    """Test that empty string fails validation due to min_length=1."""
    with pytest.raises(ValidationError):
        MessageResponse(message="")


def test_message_response_missing_field_fails():
    """Test that missing required field raises ValidationError."""
    with pytest.raises(ValidationError):
        MessageResponse()
