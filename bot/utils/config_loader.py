# bot/utils/config_loader.py
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

    @classmethod
    def validate(cls):
        """Ensure all required environment variables are set."""
        if not cls.TELEGRAM_BOT_TOKEN:
            raise ValueError("Missing environment variable: TELEGRAM_BOT_TOKEN")
        
        if cls.DATABASE_TYPE not in ("sqlite", "postgres"):
            raise ValueError("DATABASE_TYPE must be either 'sqlite' or 'postgres'.")

        if cls.DATABASE_TYPE == "postgres" and not cls.DATABASE_URL:
            raise ValueError("Missing DATABASE_URL for PostgreSQL.")


# Validate the config on import
Config.validate()
