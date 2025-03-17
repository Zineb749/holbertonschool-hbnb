from app import db
import uuid
from datetime import datetime
from .base_model import BaseModel

class Amenity(BaseModel):
    """Modèle SQLAlchemy pour un équipement (Amenity)"""
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name: str, description: str = ''):
        self.name = name[:50]  # Assurer une limite de 50 caractères
        self.description = description

    def to_dict(self):
        """Convertir un objet Amenity en dictionnaire"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "name": self.name,
            "description": self.description
        }

    def __repr__(self):
        return f"<Amenity {self.name}>"
