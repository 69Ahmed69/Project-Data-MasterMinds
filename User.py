import sqlite3
import bcrypt
from PyQt6.QtWidgets import QMessageBox
class User:
    def __init__(self, name, password, access):
        self.name = name
        self.password = password
        self.access = access

    def __str__(self):
        return f"Name: {self.name}, Password: {self.password}, Access: {self.access}"

    def set_access(self, new_access):
        self.access = new_access

    @staticmethod
    def create_database():
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (name TEXT PRIMARY KEY, password TEXT, access INTEGER)''')
        conn.commit()
        conn.close()

    @staticmethod
    def register_user(name, password, access):
        if access > 4 or access < 0:
            QMessageBox.critical(None, 'Wrong value Error', 'Access right should be between 0 and 4.')
            return
        if len(password) < 8:
            QMessageBox.critical(None, 'Weak password Error', 'Password should have at least 8 characters.')
            return
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users WHERE name = ?", (name,))
        existing_user = cursor.fetchone()
        if existing_user:
            QMessageBox.critical(None, 'Username already exists.', 'Please enter a unique username and try again.')
            conn.close()
            return
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (name, password, access) VALUES (?, ?, ?)", (name, hashed_password, access))
        conn.commit()
        conn.close()
    
    @staticmethod
    def verify_password(username, password):
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password, access FROM users WHERE name = ?", (username,))
        user_info = cursor.fetchone()
        conn.close()

        if user_info is None:
            return None

        hashed_password, access = user_info

        # Check if the provided password matches the hashed password
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return access
        else:
            return None


    @staticmethod
    def delete_user(name):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('user_database.db')
            cursor = conn.cursor()

            cursor.execute("DELETE FROM users WHERE name = ?", (name,))
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def user_exists(name):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('user_database.db')
            cursor = conn.cursor()

            # Check if the username exists
            cursor.execute("SELECT name FROM users WHERE name = ?", (name,))
            existing_user = cursor.fetchone()
            if not existing_user:
                return False
            else:
                return True
        finally:
            conn.close()
    
    @staticmethod
    def get_access_right(name):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('user_database.db')
            cursor = conn.cursor()

            # Check if the username exists
            cursor.execute("SELECT name, access FROM users WHERE name = ?", (name,))
            user = cursor.fetchone()
            if user:
                return user[1]  # Access right is at index 1 in the tuple
            else:
                return None  # User not found
        finally:
            conn.close()
    
    @staticmethod
    def modify_user(username, new_username, new_access):
        # Connect to the SQLite database
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()

        # Check if the username exists
        cursor.execute("SELECT name FROM users WHERE name = ?", (username,))
        existing_user = cursor.fetchone()
        if not existing_user:
            QMessageBox.critical(None, 'User not found', 'The specified user does not exist.')
            conn.close()
            return

        # Update the username and access right
        cursor.execute("UPDATE users SET name = ?, access = ? WHERE name = ?", (new_username, new_access, username))
        conn.commit()
        conn.close()
        QMessageBox.information(None, 'User modified', f'The user {username} has been modified successfully.')
