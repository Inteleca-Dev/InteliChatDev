'''
This file handles user related operations.
'''
import getpass
import bcrypt
class User:
    def __init__(self, db):
        self.db = db
    def login(self):
        # Get user credentials and authenticate
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")  # Use getpass to hide password input
        # Authenticate user
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', username)
        user = cursor.fetchone()
        if user:
            # Hash the entered password with the stored salt
            hashed_password = bcrypt.hashpw(password.encode(), user[2].encode())
            # Check if the hashed password matches the stored hash
            if bcrypt.checkpw(hashed_password, user[1].encode()):
                self.user_id = user[0]
                return True
        return False