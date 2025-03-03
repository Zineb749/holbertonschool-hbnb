import uuid
import re
from datetime import datetime


""" Class to create an User"""


class User:
    def __init__(self, first_name, last_name, email, is_admin=False):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.first_name = first_name[:50]
        self.last_name = last_name[:50]
        self.email = email
        self.is_admin = is_admin

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()


@staticmethod
def validate_name(name, field_name):
        """Ensure name is a non-empty string with max length of 50 characters"""
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"{field_name} cannot be empty.")
        return name[:50]


@staticmethod
    
