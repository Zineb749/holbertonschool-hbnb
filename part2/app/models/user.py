import uuid

class User:
    def __init__(self, first_name, last_name, email, password):
        self.id = str(uuid.uuid4())  # Génère un id unique pour chaque utilisateur
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
