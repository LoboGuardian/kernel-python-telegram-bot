# src/handlers/errors.py
from telegram import Update
from telegram.ext import CallbackContext
import logging


async def error_handler_command(update: Update, context: CallbackContext) -> None:
    """Handles errors gracefully."""
    logging.error(f"Error encountered: {context.error}")
    await update.message.reply_text("An error occurred. Please try again later.")
