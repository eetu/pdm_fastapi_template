"""Tests for the root routes."""

import pytest
from fastapi.testclient import TestClient

from ..main import app
from ..models.message import MessageResponse


@pytest.fixture
def client():
    """Create a test client for the FastAPI app.

    Returns:
        TestClient: A FastAPI test client instance.
    """
    return TestClient(app)


def test_root_endpoint(client):
    """Test the root endpoint returns the expected message.

    Args:
        client: The FastAPI test client fixture.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_root_endpoint_message_content(client):
    """Test the root endpoint returns the correct message content.

    Args:
        client: The FastAPI test client fixture.
    """
    response = client.get("/")
    data = response.json()
    assert isinstance(data["message"], str)
    assert len(data["message"]) > 0


def test_root_endpoint_response_validation(client):
    """Test the root endpoint response validates against Pydantic model.

    Args:
        client: The FastAPI test client fixture.
    """
    response = client.get("/")
    assert response.status_code == 200

    # Validate response using Pydantic model
    message_response = MessageResponse(**response.json())
    assert message_response.message
    assert isinstance(message_response.message, str)
