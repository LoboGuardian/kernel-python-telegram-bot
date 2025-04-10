# bot/config.py
from utils.config_loader import Config
from utils.logger import configure_logging

# Initialize logging
configure_logging()

# Load configuration variables
TOKEN = Config.TELEGRAM_BOT_TOKEN
DEBUG_MODE = Config.DEBUG_MODE
LOG_LEVEL = Config.LOG_LEVEL
