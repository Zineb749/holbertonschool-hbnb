import uuid
from datetime import datetime

""" Class to create a place"""

class Place:
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.title = title[:100]
        self.description = description
        self.price = max(0, price)
        self.latitude = max(-90.0, min(90.0, latitude))
        self.longitude = max(-180.0, min(180.0, longitude))
        self.owner_id = owner_id
        self.reviews = []
        self.amenities = []

    def to_dict(self):
        """Convertit l'objet Place en dictionnaire."""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "reviews": self.reviews,
            "amenities": self.amenities
        }

