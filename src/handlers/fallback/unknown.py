# src/handlers/unknown.py
from telegram import Update
from telegram.ext import CallbackContext


async def unknown_handle_command(update: Update, context: CallbackContext) -> None:
    """Handles unknown commands gracefully."""
    await update.message.reply_text("Oops, I didn't understand that command! Use /help for available commands.")
