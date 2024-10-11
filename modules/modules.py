# modules.py

"""

This module serves as an aggregator for various command modules used
by the Telegram bot. It imports commands from several submodules,
centralizing their access in a single place. This design promotes
modularity and simplifies the management of commands.

Modules Imported:
-----------------
1. main_command: Contains basic commands and logging configuration.
   - start_command: Handles the '/start' command.
   - help_command: Provides help to users.
   - configure_logging: Configures logging for the bot.
   - unknown_handle_command: Manages unknown commands from users.
   - error_handler_command: Handles errors that may occur.

Logging Configuration:
-----------------------
The logging configuration for the bot is initialized at the end of this
module. By default, debug logging is set to False, but this can be
adjusted based on the environment (development or production).

"""

from modules.main_command import (
    start_command,
    help_command,
    configure_logging,
    unknown_handle_command,
    error_handler_command,
)

# Call the logging configuration here if you want logging to be configured for all module functions
configure_logging(debug=False)  # Adjust debug based on your environment
