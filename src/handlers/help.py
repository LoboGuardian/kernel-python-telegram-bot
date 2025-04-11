# src/handlers/help.py
from telegram import Update
from telegram.ext import CallbackContext

async def help_command(update: Update, context: CallbackContext) -> None:
    """Displays a list of available commands."""
    commands_info = [
        ("/start", "Starts interaction with the bot."),
        ("/help", "Displays this help message."),
    ]
    commands_list = "\n".join([f"{cmd}: {desc}" for cmd, desc in commands_info])

    help_message = f"Here’s a list of commands:\n\n{commands_list}\n\nUse /help to see this list anytime."
    await update.message.reply_text(help_message)
