// Fonction pour extraire l'ID du lieu à partir de l'URL
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id'); // Extrait le paramètre `id`
}

// Fonction pour récupérer les cookies
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Fonction pour vérifier si l'utilisateur est authentifié
function checkAuthentication() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
        if (addReviewSection) {
            addReviewSection.style.display = 'none';
        }
        return null;
    } else {
        if (addReviewSection) {
            addReviewSection.style.display = 'block';
        }
        return token;
    }
}

// Fonction pour récupérer les détails du lieu
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

// Fonction pour afficher les détails du lieu
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
    reviewsContainer.innerHTML = ''; // Vider avant d'ajouter des avis
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

// Fonction pour gérer la soumission du formulaire de connexion
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Empêche la soumission classique

            // Récupérer les données du formulaire
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            // Appeler la fonction pour effectuer la connexion
            await loginUser(email, password);
        });
    }

    // Initialisation pour les détails du lieu
    const placeId = getPlaceIdFromURL();
    const token = checkAuthentication();
    if (placeId && token) {
        fetchPlaceDetails(token, placeId);
    }
});

// Fonction pour gérer la connexion
async function loginUser(email, password) {
    try {
        const response = await fetch('https://your-api-url/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Indique que les données envoyées sont au format JSON
            },
            body: JSON.stringify({ email, password }) // Corps de la requête contenant l'email et le mot de passe
        });

        if (response.ok) {
            const data = await response.json(); // Récupérer les données de l'API

            // Stocker le JWT dans un cookie
            document.cookie = `token=${data.access_token}; path=/`;

            // Rediriger vers la page principale
            window.location.href = 'index.html';
        } else {
            // Afficher un message d'erreur si la connexion échoue
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = 'Connexion échouée : Identifiants invalides.';
        }
    } catch (error) {
        console.error('Erreur réseau :', error);
        alert('Une erreur est survenue. Veuillez réessayer.');
    }
}
