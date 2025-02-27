import uuid

class Amenity:
    def __init__(self, name,description=''):
        self.id = str(uuid.uuid4())  # Génère un ID unique pour chaque amenity
        self.name = name
        self.description = description