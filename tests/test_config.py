# tests/test_config.py
from ..utils.config_loader import Config


def test_load_config():
    """Ensure LOG_LEVEL is correctly set from environment variables."""
    assert Config.LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR"]


def test_database_type():
    """Ensure DATABASE_TYPE is correctly set."""
    assert Config.DATABASE_TYPE in ["sqlite", "postgres"]


def test_telegram_token():
    """Ensure TELEGRAM_BOT_TOKEN exists."""
    assert isinstance(Config.TELEGRAM_BOT_TOKEN, str) and len(
        Config.TELEGRAM_BOT_TOKEN) > 0
