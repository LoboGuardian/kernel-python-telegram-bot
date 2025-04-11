# src/services/auth.py
"""
auth.py

Handles authentication and permission checks for Telegram bot users.
"""

import os
from telegram import Update
from telegram.ext import CallbackContext

# Load authorized user IDs from environment variables
AUTHORIZED_USERS = os.getenv("AUTHORIZED_USERS", "").split(",")  # List of user IDs

def is_user_authorized(update: Update) -> bool:
    """
    Checks if the user is authorized to use the bot.

    Args:
        update (Update): Telegram update object.

    Returns:
        bool: True if the user is authorized, False otherwise.
    """
    user_id = str(update.effective_user.id)  # Convert to string for comparison
    return user_id in AUTHORIZED_USERS

async def unauthorized_access(update: Update, context: CallbackContext) -> None:
    """
    Sends a message to unauthorized users.

    Args:
        update (Update): Telegram update object.
        context (CallbackContext): Telegram context.
    """
    await update.message.reply_text("🚫 You are not authorized to use this bot.")

