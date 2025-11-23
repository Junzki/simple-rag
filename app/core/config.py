# -*- coding: utf-8 -*-
"""Application configuration."""

import typing as ty

import os
import pathlib
from pydantic_settings import BaseSettings, SettingsConfigDict

os.environ.setdefault('HF_HUB_OFFLINE', '1')

SOURCE_CODE_DIR = pathlib.Path(__file__).parent.parent
BASE_DIR = SOURCE_CODE_DIR.parent


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application settings
    app_name: str = "simple-rag"
    app_version: str = "0.1.0"
    debug: bool = True

    # Server settings
    host: str = "127.0.0.1"
    port: int = 8000

    # API settings
    api_v1_prefix: str = "/api/v1"

    # CORS settings
    cors_origins: ty.List[str] = ["http://localhost:3000", "http://localhost:8000", "http://localhost:5173"]

    llm_base_url: str = 'https://api.moonshot.cn/v1'
    llm_model: str = 'kimi-k2-turbo-preview'
    llm_token: str = ''
    data_storage_path: str | pathlib.Path  = BASE_DIR / "data_storage"



settings = Settings()
