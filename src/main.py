#!/bin/env python
#-*-coding:UTF-8-*-
# src/main.py
#
# Made by LoboGuardian
# Follow me on https://github.com/LoboGuardian

"""
This is the main entry point for the Telegram bot. It sets up the bot
using the Telegram API and manages command handling.

Version Handling:
-----------------
Defines the version of the bot as a global variable.

Dependencies:
-------------
- Third-party libraries: It's using the Telegram API library to
  handle messages and commands.
- Local imports: Imports configuration and command modules.

Key Functions:
--------------
1. main: Initializes the bot and sets up command handlers.
2. on_startup: Sends a notification when the bot starts.

Global Variables:
-----------------
- VERSION: The version of the bot.
- TOKEN: The API token for authenticating the bot with the Telegram API.
- COMMANDS: A list of commands supported by the bot.

Usage:
------
Run this script to start the bot.
"""
import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
# Third-party libraries
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    filters
)

from config import TOKEN
from handlers.commom import start, help
from handlers.fallback import errors, unknown
from utils.config_loader import Config
from utils.logger import configure_logging

# Initialize logging
configure_logging()

# Reuse TOKEN, DEBUG_MODE, etc.
TOKEN = Config.TELEGRAM_BOT_TOKEN

def register_handlers(app):
    """Register all bot command and message handlers."""
    app.add_handler(CommandHandler("start", start.start_command))
    app.add_handler(CommandHandler("help", help.help_command))

    # Error and unknown command handlers
    app.add_handler(MessageHandler(filters.COMMAND, unknown.unknown_handle_command))
    app.add_error_handler(errors.error_handler_command)

def run_polling():
    """Run bot using polling (development or fallback mode)."""
    app = ApplicationBuilder().token(TOKEN).build()
    register_handlers(app)
    app.run_polling()

def run_webhook():
    """Run bot using webhook (production mode)."""
    app = ApplicationBuilder().token(TOKEN).build()
    register_handlers(app)
    app.run_webhook(
        listen="0.0.0.0",
        url_path="webhook/",
        webhook_url=Config.WEBHOOK_URL,
        port=Config.WEBHOOK_PORT,
    )


def main() -> None:
    """Main entry point to start the bot based on configuration."""
    if Config.USE_WEBHOOK:
        logging.info("Starting bot with Webhook")
        run_webhook()
    else:
        logging.info("Starting bot with Polling")
        run_polling()

if __name__ == "__main__":
    main()