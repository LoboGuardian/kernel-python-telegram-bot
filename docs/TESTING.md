# 🧪 Testing Guide

This guide explains how to run and write tests for the bot.

## 1️⃣ Running Tests

To run all tests:

```bash
poetry run pytest
```

To run a specific test file:

```bash
poetry run pytest tests/test_database.py
```

2️⃣ Writing Tests

- All tests are stored in the ```tests/``` directory.
- Use ```pytest``` for writing tests.
- Mock external services to avoid real API calls.

✅ Example Test (```tests/test_config.py```)

```python
from bot.utils.config_loader import Config

def test_load_config():
    assert Config.LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR"]
```