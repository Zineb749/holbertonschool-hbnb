import uuid

class Place:
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None):
        self.id = str(uuid.uuid4())  # Génère un id unique pour chaque place
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities if amenities is not None else []  # Liste vide par défaut si aucune amenity n'est donnée

    def __repr__(self):
        return f"<Place(title={self.title}, id={self.id})>"
