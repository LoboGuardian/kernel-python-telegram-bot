# 🚀 Contributing to Kernel Telegram Bot

Thank you for your interest in contributing to this project! 🎉  
This document provides guidelines to **ensure high-quality contributions**.

## How to Contribute

### **1. Fork the Repository**

1. Click on **Fork** at the top right of this repo.

2. Clone your fork:

```bash
git clone https://github.com/LoboGuardian/kernel-telegram-bot.git
```

3. Navigate into the project:

```bash
cd kernel-telegram-bot
```

4. Create a new branch:

```bash
git checkout -b feature/your-feature
```

### **2. Install Dependencies**

Ensure you have **Poetry** installed:

```bash
pip install poetry
poetry install
```

### **3. Make Your Changes**

- Follow PEP8 guidelines for Python code.
- Keep your commits atomic (one logical change per commit).
- Write meaningful commit messages:

```bash
git commit -m "Added support for Webhooks"
```

### **4. Run Tests Before Submitting**

Ensure all tests pass before making a pull request:

```bash
poetry run pytest
```

### **5. Submit a Pull Request**

1. Push your branch:

```bash
git push origin feature/your-feature
```

2. Go to GitHub > Pull Requests > New PR and describe your changes.

### **Code Style Guide**

- Follow Python PEP8 coding style.
- Use type hints (```def my_function(param: str) -> int:```).
- Write docstrings for functions and classes.
- Use meaningful variable names.
- Keep functions and modules small and focused.

### **Need Help?**

Join the discussion in GitHub Issues or start a new one!
We appreciate every contribution, whether small or big. Thank you! 🎉