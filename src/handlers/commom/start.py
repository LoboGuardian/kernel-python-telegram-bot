# src/handlers/start.py
from telegram import Update
from telegram.ext import CallbackContext
from services.database import DatabaseFactory

db = DatabaseFactory.get_database()
db.initialize_database()

GREETING_MESSAGE = "Hello, my name is kernel-python-telegram-bot"


async def start_command(update: Update, context: CallbackContext) -> None:
    """Handles the /start command, greets, and registers users."""
    user = update.effective_user
    db.add_user(str(user.id), user.username, user.full_name)

    greeting = f"{GREETING_MESSAGE}, nice to meet you, {user.full_name}!"
    await update.message.reply_text(greeting)
    await update.message.reply_text("You are now registered in the bot!")


# Authorized
# from services.auth import is_user_authorized, unauthorized_access

# async def start_command(update: Update, context: CallbackContext) -> None:
#     """Handles the /start command and checks user authorization."""
#     if not is_user_authorized(update):
#         await unauthorized_access(update, context)
#         return  # Stop execution if unauthorized

#     await update.message.reply_text("Welcome! You are authorized to use this bot.")


# Database model 1
# from services.database import add_user

# async def start_command(update: Update, context: CallbackContext) -> None:
#     """Handles the /start command and registers users."""
#     user = update.effective_user
#     add_user(str(user.id), user.username)  # Save user to database

#     await update.message.reply_text("You are now registered in the bot!")
