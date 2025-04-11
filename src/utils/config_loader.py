# src/utils/config_loader.py
"""
config_loader.py

This module is responsible for loading configuration settings
from environment variables and .env files. It ensures that
all required configurations are available for the bot to function properly.

"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class that loads and validates environment variables."""

    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()  # Ensure uppercase for consistency
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "yes")

    # Database configuration
    DATABASE_TYPE: str = os.getenv("DATABASE_TYPE", "sqlite").lower()
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")  # PostgreSQL URL
    DATABASE_FILE: str = os.getenv("DATABASE_FILE", "bot_database.db")  # SQLite file path

    # Webhook configuration
    USE_WEBHOOK: bool = os.getenv("USE_WEBHOOK", "False").lower() in ("true", "1", "yes")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", "")
    WEBHOOK_PORT: int = int(os.getenv("WEBHOOK_PORT", "8443"))
    WEBHOOK_PATH: str = os.getenv("WEBHOOK_PATH", "/webhook")
    WEBHOOK_HOST: str = os.getenv("WEBHOOK_HOST", "0.0.0.0")

    @classmethod
    def validate(cls):
        """Ensure all required environment variables are set."""
        if not cls.TELEGRAM_BOT_TOKEN:
            raise ValueError("Missing environment variable: TELEGRAM_BOT_TOKEN")
        
        if cls.DATABASE_TYPE not in ("sqlite", "postgres"):
            raise ValueError("DATABASE_TYPE must be either 'sqlite' or 'postgres'.")

        if cls.DATABASE_TYPE == "postgres" and not cls.DATABASE_URL:
            raise ValueError("Missing DATABASE_URL for PostgreSQL.")
        
        if cls.USE_WEBHOOK and not cls.WEBHOOK_URL:
            raise ValueError("Missing WEBHOOK_URL while using webhook mode.")


# Validate the config on import
Config.validate()
