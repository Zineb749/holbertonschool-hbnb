import uuid
from datetime import datetime
from models.user import User
from models.review import Review
from models.amenity import Amenity

""" Class to create a place"""


class Place:
    def __init__(self, title, description, price, latitude, longitude, owner):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.title = title[:100]  # Max length 100
        self.description = description
        self.price = max(0, price)  # Ensure positive price
        self.latitude = max(-90.0, min(90.0, latitude))
        self.longitude = max(-180.0, min(180.0, longitude))
        self.owner = owner if isinstance(owner, User) else None
        self.reviews = []  # One-to-many relationship
        self.amenities = []  # Many-to-many relationship

    def add_review(self, review):
        """Add a review to the place."""
        if isinstance(review, Review):
            self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if isinstance(amenity, Amenity) and amenity not in self.amenities:
            self.amenities.append(amenity)
