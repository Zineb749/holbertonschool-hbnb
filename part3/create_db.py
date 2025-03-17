from app import create_app, db

# Création de l'application Flask
app = create_app()

# Création des tables dans la base de données
with app.app_context():
    db.create_all()
    print("✅ Base de données et tables créées avec succès.")
