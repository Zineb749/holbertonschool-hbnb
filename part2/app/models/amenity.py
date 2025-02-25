import uuid

class Amenity:
    def __init__(self, name):
        self.id = str(uuid.uuid4())  # Génère un ID unique pour chaque amenity
        self.name = name
