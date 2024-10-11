#!/bin/env python
#-*-coding:UTF-8-*-
# main.py
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

# Define the version in a variable
VERSION = "Kernel-2024.10.1"

# Third-party libraries
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    filters)

# Local imports
from config.auth import TOKEN
from modules.modules import *

# List of command strings
COMMANDS = [
    "/start", "/help"
]

# Main function to start the bot
def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    # Register command handlers
    for command in COMMANDS:
        app.add_handler(CommandHandler(command[1:], globals().get(f"{command[1:]}_command")))

    # Error handler
    app.add_handler(MessageHandler(filters.COMMAND, unknown_handle_command))
    app.add_error_handler(error_handler_command)

    # Start polling
    app.run_polling()

if __name__ == '__main__':
    main()
