# tests/test_database.py
import pytest
from ..services.database import DatabaseFactory
from ..utils.config_loader import Config

@pytest.fixture
def db():
    """Create a database instance for testing."""
    db_instance = DatabaseFactory.get_database()
    db_instance.initialize_database()
    yield db_instance  # Provide database instance for tests
    db_instance.close()  # Cleanup after test

def test_add_user(db):
    """Test user insertion into the database."""
    db.add_user("123456", "test_user")
    users = db.get_all_users()
    assert any(user["telegram_id"] == "123456" for user in users)

def test_duplicate_user(db):
    """Test that duplicate users are not inserted."""
    db.add_user("789012", "test_user_2")
    db.add_user("789012", "test_user_2")  # Insert same user again
    users = [user["telegram_id"] for user in db.get_all_users()]
    assert users.count("789012") == 1  # Should only be one instance

def test_database_type():
    """Ensure correct database type is used."""
    assert Config.DATABASE_TYPE in ["sqlite", "postgres"]
