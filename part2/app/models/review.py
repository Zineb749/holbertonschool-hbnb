import uuid
from datetime import datetime
from models.user import User
from models.place import Place
""" Class that creates  reviews"""


class Review:
    def __init__(self, text, rating, place, user):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.text = text if text else "No review provided"
        self.rating = max(1, min(5, rating))
        self.place = place if isinstance(place, Place) else None
        self.user = user if isinstance(user, User) else None

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
