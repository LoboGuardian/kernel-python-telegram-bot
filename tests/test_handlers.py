# tests/test_handlers.py
import pytest
from telegram import Update, User, Message, Chat
from telegram.ext import CallbackContext
from ..handlers.start import start_command
from ..handlers.help import help_command

@pytest.fixture
def update():
    """Creates a mock Telegram update."""
    user = User(id=123456, is_bot=False, first_name="TestUser")
    chat = Chat(id=987654, type="private")
    message = Message(message_id=1, from_user=user, chat=chat, text="/start", date=None)
    
    mock_update = Update(update_id=1, message=message)
    return mock_update

@pytest.fixture
def context():
    """Creates a mock CallbackContext."""
    return CallbackContext(dispatcher=None)

@pytest.mark.asyncio
async def test_start_command(update, context):
    """Test that the /start command sends a correct message."""
    await start_command(update, context)
    assert update.message.text == "/start"

@pytest.mark.asyncio
async def test_help_command(update, context):
    """Test that the /help command sends a correct response."""
    await help_command(update, context)
    assert "/help" in update.message.text
