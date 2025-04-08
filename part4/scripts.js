// Extraire l'ID du lieu à partir de l'URL
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id'); // Extrait le paramètre `id`
}

// Vérifier si l'utilisateur est authentifié
function checkAuthentication() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
        addReviewSection.style.display = 'none';
    } else {
        addReviewSection.style.display = 'block';
        return token;
    }
}

// Récupérer les détails du lieu
async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`https://your-api-url/places/${placeId}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const place = await response.json();
            displayPlaceDetails(place);
        } else {
            console.error('Erreur lors de la récupération des détails du lieu.');
        }
    } catch (error) {
        console.error('Erreur réseau :', error);
    }
}

// Afficher les détails du lieu
function displayPlaceDetails(place) {
    const placeDetails = document.getElementById('place-details');
    placeDetails.innerHTML = `
        <h1>${place.name}</h1>
        <p>Description : ${place.description}</p>
        <p>Prix par nuit : ${place.price}€</p>
        <p>Équipements : ${place.amenities.join(', ')}</p>
    `;

    // Afficher les avis
    const reviewsContainer = document.getElementById('reviews-container');
    place.reviews.forEach(review => {
        const reviewCard = document.createElement('div');
        reviewCard.classList.add('review-card');
        reviewCard.innerHTML = `
            <p>Commentaire : ${review.text}</p>
            <p>Note : ${'⭐'.repeat(review.rating)}</p>
            <p>Utilisateur : ${review.user}</p>
        `;
        reviewsContainer.appendChild(reviewCard);
    });
}

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    const placeId = getPlaceIdFromURL();
    const token = checkAuthentication();
    if (token) fetchPlaceDetails(token, placeId);
});
