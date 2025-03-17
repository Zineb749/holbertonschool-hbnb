from app.persistence.repository import SQLAlchemyRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from datetime import datetime
from app import db  # ✅ Ajout de db pour initialisation

class HBnBFacade:
    def __init__(self):
        self.user_repository = SQLAlchemyRepository(User)
        self.place_repository = SQLAlchemyRepository(Place)
        self.review_repository = SQLAlchemyRepository(Review)
        self.amenity_repository = SQLAlchemyRepository(Amenity)

    ###########################################################################
    # 🧑‍💻 CRUD UTILISATEURS
    ###########################################################################

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repository.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repository.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repository.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repository.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repository.get(user_id)
        if not user:
            return None

        for key, value in user_data.items():
            setattr(user, key, value)

        self.user_repository.update(user)
        return user

    ###########################################################################
    # 🏠 CRUD LIEUX
    ###########################################################################
    @staticmethod
    def create_place(data):
        new_place = Place(
            title=data['title'],
            description=data.get('description', ''),
            price=data['price'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            owner_id=data['owner_id']
        )

        db.session.add(new_place)
        db.session.commit()

        print(f"DEBUG: new_place -> {new_place}")  # 🔍 Vérifier ce que new_place contient
        return new_place 

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def get_all_places(self):
        return self.place_repository.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repository.get(place_id)
        if not place:
            return None

        for key, value in place_data.items():
            setattr(place, key, value)

        self.place_repository.update(place)
        return place

    def delete_place(self, place_id):
        return self.place_repository.delete(place_id)

    ###########################################################################
    # ⭐ CRUD REVIEWS
    ###########################################################################

    def create_user(self, user_data):
        existing_user = self.get_user_by_email(user_data["email"])
        if existing_user:
            return {"error": "Email already exists"}, 400  # ✅ Empêcher l'erreur en base

        user = User(**user_data)
        self.user_repository.add(user)
        db.session.commit()
        db.session.refresh(user)  # ✅ S'assurer que l'ID est bien récupéré

        print(f"✅ User created: {user}")  # 🔍 Vérifier si l'objet est bien créé
        return user

    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def get_reviews_by_place(self, place_id):
        return self.review_repository.get_by_attribute('place_id', place_id)

    def update_review(self, review_id, review_data):
        review = self.review_repository.get(review_id)
        if not review:
            return None

        for key, value in review_data.items():
            setattr(review, key, value)

        self.review_repository.update(review)
        return review

    def delete_review(self, review_id):
        return self.review_repository.delete(review_id)

    ###########################################################################
    # 🏨 CRUD AMENITIES
    ###########################################################################

    def create_amenity(self, data):
        existing_amenity = Amenity.query.filter_by(name=data["name"]).first()
        if existing_amenity:
            raise ValueError("Amenity already exists")

        new_amenity = Amenity(name=data["name"], description=data.get("description", ""))
        db.session.add(new_amenity)
        db.session.commit()
        return new_amenity


    def get_amenity(self, amenity_id):
        return self.amenity_repository.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repository.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repository.get(amenity_id)
        if not amenity:
            return None

        for key, value in amenity_data.items():
            setattr(amenity, key, value)

        self.amenity_repository.update(amenity)
        return amenity

    def delete_amenity(self, amenity_id):
        return self.amenity_repository.delete(amenity_id)
