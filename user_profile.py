from auth import authenticate_user

class UserProfile:
    """User profile management."""
    
    def __init__(self, username):
        self.username = username
        self.authenticated = False
    
    def login(self, password):
        """Login user with password."""
        self.authenticated = authenticate_user(self.username, password)
        return self.authenticated