from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from uuid import UUID
from flask import request, jsonify
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
api = Namespace('reviews', description='Review operations')
facade = HBnBFacade()

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description="La note de l'avis (1 à 5)", min=1, max=5),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Créer un nouvel avis (review)"""
        
        review_data = api.payload  # Récupération des données de la requête

        # ✅ Vérification des champs obligatoires
        required_fields = ["text", "rating", "user_id", "place_id"]
        missing_fields = [field for field in required_fields if field not in review_data]

        if missing_fields:
            return {"error": f"Champs obligatoires manquants: {', '.join(missing_fields)}"}, 400

        # ✅ Vérifier le format des données
        if not isinstance(review_data["text"], str) or not review_data["text"].strip():
            return {"error": "Le champ 'text' doit être une chaîne non vide"}, 400
        
        if not isinstance(review_data["rating"], int) or not (1 <= review_data["rating"] <= 5):
            return {"error": "Le champ 'rating' doit être un entier entre 1 et 5"}, 400

        if not isinstance(review_data["user_id"], str) or not review_data["user_id"].strip():
            return {"error": "Le champ 'user_id' doit être une chaîne valide"}, 400

        if not isinstance(review_data["place_id"], str) or not review_data["place_id"].strip():
            return {"error": "Le champ 'place_id' doit être une chaîne valide"}, 400

        new_review = Review(
            text=review_data["text"],
            rating=review_data["rating"],
            user_id=review_data["user_id"],
            place_id=review_data["place_id"]
        )

        # ✅ Ajouter et sauvegarder
        facade.create_review(new_review)

        # ✅ Retourner l'objet Review sous forme de dictionnaire
        return {
            "id": new_review.id,
            "text": new_review.text,
            "rating": new_review.rating,
            "user_id": new_review.user_id,
            "place_id": new_review.place_id,
            "created_at": new_review.created_at.isoformat(),
            "updated_at": new_review.updated_at.isoformat()
        }, 201



    def get(self):
        reviews = facade.review_repo.get_all()
        if not reviews:
            return {'message': 'No reviews found'}, 404

        review_list = [{
            'id': review.id,
            'text': review.text,
            'user_id': review.user_id,
            'place_id': review.place_id
        } for review in reviews]

        return review_list, 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        return {
            'id': review.id,
            'text': review.text,
            'user_id': review.user_id,
            'place_id': review.place_id
        }, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @api.response(500, 'Internal Server Error')
    def put(self, review_id):
        review_data = api.payload  # JSON reçu de la requête

        review = facade.get_review(review_id)  # Récupération de l'avis en base
        if not review:
            return {'error': 'Review not found'}, 404

        try:
            # Mise à jour des champs seulement si présents dans la requête
            if 'text' in review_data:
                review.text = review_data['text']
            if 'rating' in review_data:
                review.rating = review_data['rating']
            if 'user_id' in review_data:
                review.user_id = review_data['user_id']
            if 'place_id' in review_data:
                review.place_id = review_data['place_id']

            # Sauvegarde des modifications
            facade.update_review(review_id, review)

            return {
                'message': 'Review updated successfully',
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.user_id,
                'place_id': review.place_id
            }, 200
        except Exception as e:
            print(f"Error updating review: {e}")
            return {'message': 'Internal Server Error'}, 500



    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        success = facade.delete_review(review_id)
        if not success:
            return {'error': 'Review not found'}, 404

        return {'message': 'Review deleted successfully'}, 200
    

    
@api.route('/places/<place_id>/reviews')
class PlaceReviews(Resource):
    @api.response(200, 'Reviews retrieved successfully')
    @api.response(404, 'No reviews found for this place')
    def get(self, place_id):
        """Retrieve all reviews for a specific place"""
        print(f"DEBUG: Retrieving reviews for place ID: {place_id}")  # Debug

        reviews = facade.get_reviews_by_place(place_id)  # Utilisation de la méthode existante

        if not reviews:
            return {'message': 'No reviews found for this place'}, 404

        return [
            {
                'id': review.id,
                'text': review.text,
                'rating': review.rating
            } for review in reviews
        ], 200
