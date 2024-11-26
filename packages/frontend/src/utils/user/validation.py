import re

class Validation():
    """
    This is a class that contains methods to validate user input.
    """
    def __init__(self) -> None:
        pass
    
    def is_valid_email(self, email: str) -> bool:
        pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    def is_valid_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        
        if not re.search("[@_!#$%^&*()<>?/\|}{~:]", password):
            return False
        
        return True