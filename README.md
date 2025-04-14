# 🛠️ Kernel Telegram Bot
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
│── src/                      # Main application logic
│   ├── __init__.py           # Package init file
│   ├── main.py               # Entry point of the bot
│   │
│   ├── handlers/             # Telegram command handlers
│   │   ├── __init__.py       # Package init file
│   │   ├── start.py          # /start command
│   │   ├── help.py           # /help command
│   │   ├── unknown.py        # Unknown command handler
│   │   ├── errors.py         # Error handling
│   │
│   ├── services/             # Business logic (auth, db, etc.)
│   │   ├── __init__.py       # Package init file
│   │   ├── auth.py           # Manages user authentication & permissions.
│   │   ├── database.py       # Handles data storage (SQLite/PostgreSQL).
│   │   ├── cache.py          # (Upcoming) Redis-based caching (for faster performance)
│   │   ├── api_client.py     # (Upcoming) Handles API integrations (with external APIs)
│   │
│   ├── utils/                # Utility functions (config, logging)
│   │   ├── __init__.py       # Package init file
│   │   ├── config_loader.py  # Load config files or .env
│   │   ├── logger.py         # Logging setup
│   │   ├── middleware.py     # (Upcoming) Preprocess messages before reaching handlers (spam filtering, normalization)
│   │
│   ├── plugins/              # (Upcoming) Dynamic plugin modules)
│   ├── locales/              # (Upcoming) Multi-language support
│   ├── dashboard/            # (Upcoming) FastAPI-based admin panel
│   ├── config.py             # Main bot configuration
│
├── tests/                    # Unit and integration tests
│   ├── test_config.py        # Tests for config loader
│   ├── test_database.py      # Tests for database functionality
│   ├── test_handlers.py      # Tests for bot command handlers
│
├── docs/                     # Documentation files
│   ├── SETUP.md              # Setup guide
│   ├── TESTING.md            # Testing guide
│   ├── DEPLOYMENT.md         # Deployment instructions
│
├── .gitignore                # Git ignore rules
├── .env                      # Environment variables
├── LICENSE                   # License file
├── README.md                 # Project documentation
├── CODE_OF_CONDUCT.md        # Code of conduct for contributors
├── AUTHORS.md                # List of contributors
├── CONTRIBUTING.md           # Contribution guidelines
├── pyproject.toml            # Poetry configuration
├── poetry.lock               # Poetry dependencies
└── run.sh                    # Script to run the bot
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
