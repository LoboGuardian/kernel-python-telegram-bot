# 🚀 Deployment Guide

This guide explains how to deploy the bot on **VPS, Docker, or Cloud Services**.


This guide covers deploying your application on a Linux VPS, with instructions for common package managers: APT, Pacman, and DNF.


## Deploying on a VPS (Linux)

### 1. Install Essential Tools

#### Common Requirements

Regardless of the distribution, we'll need Python and Poetry.

- APT (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install python3-pip
pip install poetry
```

- Pacman (Arch Linux/Manjaro)

```bash
sudo pacman -Syu python python-pip
pip install poetry
```

- DNF (Fedora/CentOS/RHEL)

```bash
sudo dnf update -y
sudo dnf install python3 python3-pip
pip3 install poetry
```

### 2. Clone the repo:

```bash
git clone https://github.com/LoboGuardian/kernel-telegram-bot.git
cd kernel-telegram-bot
```

### 3. Set up environment variables (```.env```).

### 4. Run the bot:

```bash
poetry run python src/main.py
```

## Deploying with Docker (Coming Soon)

A Dockerfile will be added to support containerization.

