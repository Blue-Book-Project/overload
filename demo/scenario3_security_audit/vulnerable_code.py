# User Management System
# WARNING: This code contains critical security vulnerabilities

import sqlite3
import requests

# VULNERABILITY 1: Hardcoded credentials
DATABASE_PASSWORD = "admin123"
SECRET_KEY = "mysecretkey123"
API_KEY = "sk-prod-abc123xyz789"

class UserManager:
    
    def __init__(self):
        # VULNERABILITY 2: No encryption on database connection
        self.db = sqlite3.connect("users.db")
    
    def login(self, username, password):
        cursor = self.db.cursor()
        
        # VULNERABILITY 3: SQL Injection
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        
        return user
    
    def get_user_data(self, user_id):
        cursor = self.db.cursor()
        
        # VULNERABILITY 4: Another SQL Injection
        query = f"SELECT * FROM users WHERE id={user_id}"
        cursor.execute(query)
        
        return cursor.fetchone()
    
    def store_password(self, username, password):
        cursor = self.db.cursor()
        
        # VULNERABILITY 5: Storing plain text passwords
        query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
        cursor.execute(query)
        self.db.commit()
    
    def send_data_to_analytics(self, user_data):
        # VULNERABILITY 6: Sending sensitive data over HTTP not HTTPS
        requests.post(
            "http://analytics.company.com/track",
            json=user_data
        )
    
    def reset_password(self, username, new_password):
        cursor = self.db.cursor()
        
        # VULNERABILITY 7: No authentication check before reset
        query = f"UPDATE users SET password='{new_password}' WHERE username='{username}'"
        cursor.execute(query)
        self.db.commit()
        
        return "Password reset successful"

# VULNERABILITY 8: Debug mode left on in production
DEBUG = True
SHOW_ERRORS = True