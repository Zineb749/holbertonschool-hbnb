import uuid
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

    def update(self, data):
        """Update the attributes of the object based on the dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
