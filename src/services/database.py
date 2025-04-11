# src/services/database.py
"""
database.py

Handles data storage for the Telegram bot. Supports both SQLite and PostgreSQL.
"""

import os
import sqlite3
# import psycopg2
# from psycopg2.extras import RealDictCursor
from utils.config_loader import Config

class BaseDatabase:
    """Abstract class for database operations."""
    def initialize_database(self):
        raise NotImplementedError

    def add_user(self, telegram_id: str, username: str, fullname: str):
        raise NotImplementedError

    def get_all_users(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class SQLiteDatabase(BaseDatabase):
    """Handles SQLite database operations."""

    def __init__(self):
        """Initialize SQLite connection."""
        self.conn = sqlite3.connect(Config.DATABASE_FILE, check_same_thread=False)

    def initialize_database(self):
        """Creates necessary tables if they don’t exist."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id TEXT UNIQUE,
                username TEXT,
                fullname TEXT
            )
        """)
        self.conn.commit()

    def add_user(self, telegram_id: str, username: str, fullname: str):
        """Inserts a user into the database if not already present."""
        cursor = self.conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (telegram_id, username, fullname) VALUES (?, ?, ?)",
                (telegram_id, username, fullname)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass  # User already exists
        finally:
            cursor.close()

    def get_all_users(self):
        """Retrieves all registered users from the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        return users

    def close(self):
        """Closes the database connection."""
        self.conn.close()


class PostgreSQLDatabase(BaseDatabase):
    """Handles PostgreSQL database operations."""
    
    pass

#     def __init__(self):
#         """Initialize PostgreSQL connection."""
#         self.conn = psycopg2.connect(Config.DATABASE_URL)

#     def initialize_database(self):
#         """Creates necessary tables if they don’t exist."""
#         cursor = self.conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS users (
#                 id SERIAL PRIMARY KEY,
#                 telegram_id TEXT UNIQUE,
#                 username TEXT
#                 username TEXT
#             )
#         """)
#         self.conn.commit()

#     def add_user(self, telegram_id: str, username: str):
#         """Inserts a user into the database if not already present."""
#         cursor = self.conn.cursor()

#         try:
#             cursor.execute(
#                 "INSERT INTO users (telegram_id, username) VALUES (%s, %s)",
#                 (telegram_id, username)
#             )
#             self.conn.commit()
#         except psycopg2.IntegrityError:
#             pass  # User already exists
#         finally:
#             cursor.close()

#     def get_all_users(self):
#         """Retrieves all registered users from the database."""
#         cursor = self.conn.cursor(cursor_factory=RealDictCursor)
#         cursor.execute("SELECT * FROM users")
#         users = cursor.fetchall()
#         cursor.close()
#         return users

#     def close(self):
#         """Closes the database connection."""
#         self.conn.close()


class DatabaseFactory:
    """Factory class to return the correct database instance."""

    @staticmethod
    def get_database():
        if Config.DATABASE_TYPE == "postgres":
            return PostgreSQLDatabase()
        elif Config.DATABASE_TYPE == "sqlite":
            return SQLiteDatabase()
        else:
            raise ValueError("Invalid DATABASE_TYPE. Use 'sqlite' or 'postgres'.")
