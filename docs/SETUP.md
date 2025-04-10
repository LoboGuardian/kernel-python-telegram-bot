# ⚙️ Setup Guide

This guide explains how to set up and run the bot.

## 1. Install Dependencies
Ensure **Poetry** is installed:
```bash
pip install poetry
poetry install
```

## 2. Configure .env
Create a .env file:

```ini
# TOKEN
TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
# Add Telegram user IDs separated by commas
AUTHORIZED_USERS=12345678,98765432

# Change as needed
# LOG_LEVEL=DEBUG # Shows detailed information for debugging.
# LOG_LEVEL=INFO # Shows general information about program operation.
LOG_LEVEL=WARNING # Shows warnings about potential problems.
# LOG_LEVEL=ERROR # Shows errors that prevent correct operation.

DEBUG_MODE=False

# Options: DATABASE_TYPE sqlite or postgres

# If using SQLite:
DATABASE_TYPE=sqlite

# If using PostgreSQL: (Upcoming)
# DATABASE_TYPE=postgres  

# Only required if using PostgreSQL
# DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase

DATABASE_FILE=bot_database.db
```

## 3. Run the Bot

- Using Polling (Default):

```bash
poetry run python bot/main.py
```

- Using Webhooks **(coming soon)**:

```bash
poetry run python bot/main.py --webhook
```

- Using the run.sh Script**
    - Make sure run.sh is executable:

```bash
chmod +x run.sh
./run.sh
```