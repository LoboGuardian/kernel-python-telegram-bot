# modules/main_command.py

"""

This module contains core commands for the Telegram bot, including
greeting the user, providing help, and logging configuration.

Functions:
----------
1. configure_logging:
    Configures logging for the bot, allowing for both debug
    and standard logging levels.

2. start_command:
    Greets the user upon initiating interaction with the bot.

3. help_command:
    Provides a list of available commands and their descriptions.

"""

import logging

# Define your greeting message once for consistency
GREETING_MESSAGE = "Hello, my name is BOT_NAME"

# modules/logging.py
def configure_logging(log_filename="telegram_bot.log", debug=False):
    """Configures logging for the Python Telegram Bot library.

    Args:
        log_filename (str, optional): The filename for the log file. Defaults to "telegram_bot.log".
        debug (bool, optional): Whether to enable debug logging. Defaults to False.
    """

    # Create a logger instance
    logger = logging.getLogger()

    # Set the logging level for the logger
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    # level=logging.INFO,
    # level=logging.WARNING,
    # level=logging.DEBUG,


    # Create a file handler for logging to a specified file
    file_handler = logging.FileHandler(log_filename)

    # Set the logging level for the file handler
    file_handler.setLevel(logging.DEBUG if debug else logging.INFO)

    # Create a console handler for logging to the terminal
    console_handler = logging.StreamHandler()

    # Set the logging level for the console handler
    console_handler.setLevel(logging.DEBUG if debug else logging.INFO)

    # Define the format for log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Apply the formatter to the file handler
    file_handler.setFormatter(formatter)

    # Apply the formatter to the console handler
    console_handler.setFormatter(formatter)

    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Set the logging level for the 'httpx' library specifically
    logging.getLogger('httpx').setLevel(logging.DEBUG if debug else logging.WARNING)

async def start_command(update, context) -> None:
    """Greets the user with a friendly message."""
    user_name = update.effective_user.full_name
    greeting = f"{GREETING_MESSAGE}, nice to meet you, {user_name}!"
    await update.message.reply_text(greeting)

async def help_command(update, context) -> None:
    """Provides a list of commands and their descriptions."""
    commands_info = [
        ("/start", "Starts interaction with the bot."),
        ("/help", "Displays this help message."),
    ]

    commands_list = "\n".join([f"{command}: {description}" for command, description in commands_info])

    help_message = (
        f"{GREETING_MESSAGE}, here’s a list of commands:\n\n"
        f"{commands_list}\n\n"
        "Remember that you can use the /help command to view this list again."
    )

    await update.message.reply_text(help_message)

# modules/error_handler_command.py

"""
error_handler_command.py

This module contains error handling commands to manage unknown
commands and report errors gracefully.

Functions:
----------
1. unknown_handle_command:
    Responds to unknown commands issued by the user.

2. error_handler_command:
    Handles errors gracefully and informs the user.
"""

# Optional: Handle warnings (uncomment if needed)
# import warnings
# from telegram.warnings import PTBDeprecationWarning
# warnings.filterwarnings("error", category=PTBDeprecationWarning)

async def unknown_handle_command(update, context) -> None:
    """Handles unknown commands."""
    await update.message.reply_text(
        "Oops, we didn't understand that command!\n"
        "Remember you can always use the command /help to see what I can do for you!"
    )

async def error_handler_command(update, context) -> None:
    """Fallback error handler."""
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="An error occurred.")

    if isinstance(context.error, AttributeError):
        error_message = "There seems to be a technical issue. Please try again later."
    else:
        error_message = (
            "Oops, an error occurred! \n"
            "We're working on it, don't worry!\n\n"
            "Remember you can always use the command /help to see what I can do for you!"
        )

    await update.message.reply_text(error_message)

# modules/logging.py

"""
logging.py

This module provides logging functionality for the Telegram bot.
It logs updates and messages for easy debugging and monitoring.

Functions:
----------
1. handle_update:
    Handles updates and logs specific types of messages.
"""

def handle_update(update, context):
    """Handles updates and logs specific types of messages."""
    if update.message:
        if update.message.text or update.message.photo or update.callback_query:
            log_message = (
                f"Update type: {type(update.message).__name__}, "
                f"Chat ID: {update.effective_chat.id}, "
                f"User ID: {update.effective_user.id}, "
                f"Text: {getattr(update.message, 'text', 'N/A')}"
            )
            logging.info(log_message)
