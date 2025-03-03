import uuid
from datetime import datetime

class Review:
    def __init__(self, text, user_id, place_id):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.text = text
        self.user_id = user_id
        self.place_id = place_id

    def to_dict(self):
        """Convertit l'objet Review en dictionnaire"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "text": self.text,
            "user_id": self.user_id,
            "place_id": self.place_id
        }

