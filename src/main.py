"""FastAPI application entry point."""

from fastapi import FastAPI
from .routes.root import router as root_router

app = FastAPI(
    title="PDM FatAPI Template",
    version="0.1.0",
)

app.include_router(root_router)
