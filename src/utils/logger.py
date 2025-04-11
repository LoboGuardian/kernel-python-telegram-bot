# src/utils/logger.py
import logging
import warnings
from utils.config_loader import Config
from telegram.warnings import PTBDeprecationWarning

def configure_logging(log_filename="telegram_bot.log"):
    """Configures logging for the bot using the specified LOG_LEVEL."""

    # Convert LOG_LEVEL string to logging level
    log_level = getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler(),
        ],
    )

    # Configure logging for specific libraries
    logging.getLogger('httpx').setLevel(logging.WARNING)
    logging.getLogger('apscheduler').setLevel(logging.WARNING)
    # Telegram API logs
    logging.getLogger('telegram').setLevel(logging.WARNING)

    # Optional: Handle warnings (Uncomment if needed)
    warnings.filterwarnings("error", category=PTBDeprecationWarning)

    # Log at multiple levels
    # If LOG_LEVEL=DEBUG, you should see all messages.
    logging.debug(f"Logging configured. Level: {Config.LOG_LEVEL}")
    
    # If LOG_LEVEL=INFO, you should see INFO, WARNING, and ERROR.
    logging.info(f"Logging configured. Level: {Config.LOG_LEVEL}")
    
    # If LOG_LEVEL=WARNING, you should see WARNING and ERROR.
    logging.warning(f"Logging configured. Level: {Config.LOG_LEVEL}")
    
    # If LOG_LEVEL=ERROR, you should only see ERROR.
    logging.error(f"Logging configured. Level: {Config.LOG_LEVEL}")
