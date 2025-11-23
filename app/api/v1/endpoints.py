# -*- coding: utf-8 -*-
"""API v1 endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "Service is running"
    }


@router.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to Simple RAG API",
        "version": "0.1.0",
        "docs": "/docs"
    }
