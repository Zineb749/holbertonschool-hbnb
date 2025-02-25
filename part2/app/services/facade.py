from app.persistence.repository import InMemoryRepository
from app.models.User import User
from app.models.amenity import Amenity  # Assure-toi d'importer la classe Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Placeholder method for fetching a place by ID

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        return self.user_repo.get_all() 


    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)


    def get_all_amenity(self):
        return self.amenity_repo.get_all()


    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
    
        if 'name' in amenity_data:
            amenity.name = amenity_data['name']
    
        self.amenity_repo.update(amenity)
    
        return amenity

    
    

 
