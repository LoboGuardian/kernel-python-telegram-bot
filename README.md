# 🛠️ Kernel Python Telegram Bot
A modular Telegram bot powered by [python-telegram-bot](https://python-telegram-bot.readthedocs.io/).  
This bot is designed for scalability, maintainability, and follows clean architecture principles.

## Features

- Uses **python-telegram-bot** for handling Telegram interactions.
- Structured with **SOLID** principles for modularity.
- **Poetry-based dependency management** (previously Pipenv).
- Built-in **error handling** and **logging**.
- Uses **environment variables** (`.env`) to store sensitive data.

---

## Upcoming Enhancements & Next Steps
We are actively improving the kernel to be more reusable, scalable, and efficient. The following enhancements are planned:

- Short-Term Goals
  - Support for Webhooks: Implement run_webhook() to allow event-driven execution.
  - Testing with SQLite: Create unit tests using pytest for config_loader.py, database.py, and handlers.
  - Verify PostgreSQL Integration: Ensure database compatibility with PostgreSQL.

- Mid-Term Goals
  - Plugin System for Dynamic Modules: Load new commands automatically from src/plugins/.
  - Multi-language Support (i18n): Implement a translation system with JSON-based locales.
  - Message Middleware: Filter messages before they reach command handlers.

- Long-Term Goals
  - Redis Caching for Performance Optimization: Store user sessions in memory for faster responses.
  - External API Integration: Create api_client.py for connecting with third-party services.
  - WebSockets for Real-Time Events: Enable instant notifications and live event handling.
  - Admin Dashboard with FastAPI: Develop an API to manage and monitor the bot remotely.

---

## Installation & Setup

Check ![SETUP.md](docs/SETUP.md)

### **▶ Running the Bot**

You can start the bot in two ways:

#### **1. Using Poetry**

```bash
poetry run python src/main.py
```

#### **2. Using the run.sh Script**

Make sure run.sh is executable:

```bash
chmod +x run.sh
./run.sh
```

#### **3. Using Webhooks (Coming Soon)**

```bash
poetry run python src/main.py --webhook
```

---

## ** Project Structure**

```bash
kernel-telegram-bot/
├── src/                          # Core application logic
│   ├── __init__.py               # Marks the src directory as a package
│   ├── main.py                   # Bot entry point and event loop starter
│   │
│   ├── handlers/                 # Telegram command handlers (organized by category)
│   │   ├── __init__.py           # Initializes the handlers package
│   │   ├── common/                   # General-purpose commands
│   │   │   ├── __init__.py
│   │   │   ├── start.py              # Handles the /start command
│   │   │   ├── help.py               # Provides a list of available commands (/help)
│   │   │   ├── ping.py               # Health check (/ping)
│   │   │   └── about.py              # Shows bot info (/about)
│   │   │
│   │   ├── fun/                      # Fun and entertainment-related commands
│   │   │   ├── __init__.py
│   │   │   ├── joke.py               # Returns a random joke (/joke)
│   │   │   ├── roll.py               # Rolls a dice emoji (/roll)
│   │   │   └── quote.py              # (Optional) Sends a random quote (/quote)
│   │   │
│   │   ├── utility/                  # Utility commands (tools, lookups, etc.)
│   │   │   ├── __init__.py
│   │   │   ├── weather.py            # Fetches weather info for a city (/weather <city>)
│   │   │   ├── currency.py           # Converts currency values (/currency USD EUR 100)
│   │   │   ├── echo.py               # Repeats the user's input (/echo <text>)
│   │   │   └── time.py               # Shows current server time (/time)
│   │   │
│   │   ├── admin/
│   │   │   ├── __init__.py
│   │   │   ├── status.py             # /status - Check bot or system status
│   │   │   ├── ban.py                # /ban <user_id> - Ban a user
│   │   │   ├── unban.py              # /unban <user_id> - Unban a user
│   │   │   ├── list_groups.py        # /listgroups - List groups where the bot is active
│   │   │   ├── leave_group.py        # /leavegroup <group_id> - Force the bot to leave a group
│   │   │   ├── broadcast.py          # /broadcast <message> - Send message to all groups/channels
│   │   │   ├── admins.py             # /admins - List group/channel admins
│   │   │   ├── promote.py            # /promote <user_id>
│   │   │   ├── demote.py             # /demote <user_id>
│   │   │   ├── mute.py               # /mute <user_id> [duration]
│   │   │   ├── unmute.py             # /unmute <user_id>
│   │   │   ├── warn.py               # /warn <user_id> - Issue warning
│   │   │   ├── kick.py               # /kick <user_id> - Kick user
│   │   │   ├── purge.py              # /purge - Clean messages
│   │   │   ├── set_rules.py          # /setrules <text> - Define rules
│   │   │   ├── rules.py              # /rules - Show current rules
│   │   │   └── pin_message.py        # /pin - Pin the replied message (admin only)
│   │   │
│   │   └── fallback/                 # Fallbacks and error handlers
│   │       ├── __init__.py
│   │       ├── unknown.py            # Handles unknown or invalid commands
│   │       └── errors.py             # Global error and exception handling
│   │
│   ├── services/                 # Business logic and backend integrations
│   │   ├── __init__.py           # Initializes the services package
│   │   ├── auth.py               # User authentication and permission checks
│   │   ├── database.py           # Data persistence (supports SQLite & PostgreSQL)
│   │   ├── cache.py              # (Planned) Redis-based caching for performance
│   │   ├── api_client.py         # (Planned) Integration with third-party APIs
│   │
│   ├── utils/                    # Utility modules for shared logic
│   │   ├── __init__.py           # Initializes the utils package
│   │   ├── config_loader.py      # Loads environment variables and settings
│   │   ├── logger.py             # Sets up structured logging for the app
│   │   ├── middleware.py         # (Planned) Preprocessing for messages (e.g., spam filtering)
│   │
│   ├── plugins/                  # (Planned) Dynamic plugin loader for modular extensions
│   ├── locales/                  # (Planned) Internationalization and language packs
│   ├── dashboard/                # (Planned) FastAPI-powered admin panel for bot management
│   ├── config.py                 # Centralized bot configuration and constants
│
├── tests/                        # Automated unit and integration tests
│   ├── test_config.py            # Tests for configuration loading
│   ├── test_database.py          # Tests for data persistence logic
│   ├── test_handlers.py          # Tests for Telegram command responses
│
├── docs/                         # Documentation and guides
│   ├── SETUP.md                  # How to install and configure the bot
│   ├── TESTING.md                # How to write and run tests
│   ├── DEPLOYMENT.md             # Deployment guide and best practices
│
├── .gitignore                    # Specifies intentionally untracked files to ignore in Git
├── .env                          # Environment-specific variables (e.g., API keys, tokens)
├── LICENSE                       # License file for open source usage terms
├── README.md                     # Main project overview and usage documentation
├── CODE_OF_CONDUCT.md            # Guidelines for respectful community behavior
├── AUTHORS.md                    # List of project authors and contributors
├── CONTRIBUTING.md               # Instructions for contributing to the project
├── pyproject.toml                # Project configuration for Poetry (dependencies, metadata)
├── poetry.lock                   # Locked dependency versions for reproducible builds
└── run.sh                        # Shell script to launch the bot with one command
```

---

### **Running Tests

To run unit tests:

```bash
poetry run pytest
```

---

### **Development & Contribution

Fork this repository.

#### Clone your fork:

```bash
git clone https://github.com/LoboGuardian/kernel-telegram-bot.git
```

#### Install dependencies:
```bash
poetry install
```

#### Create a feature branch:
```bash
git checkout -b feature/new-feature
```

#### Make changes and commit:
```bash
git commit -m "Added a new feature"
Push and create a pull request.
```

---

## License

This project is licensed under the [GPL-3.0](LICENSE) License. See the LICENSE file for details.

## Credits & Contact

- Created by [LoboGuardian](https://github.com/LoboGuardian)


---

## Contribution & Future Development
We welcome contributions! Our current focus areas include:

- Expanding testing coverage.

- Optimizing database performance.

- Enhancing real-time event handling with WebSockets.

- If you want to contribute, fork the repo and submit a PR.

Feel free to discuss improvements via GitHub Issues.
