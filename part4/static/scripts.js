// Écouteur d'événement pour la soumission du formulaire de connexion
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form'); // Sélectionne le formulaire de connexion
    const errorMessage = document.getElementById('error-message'); // Zone pour afficher les erreurs

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Empêche le comportement par défaut du formulaire

            // Récupère les valeurs du formulaire
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                // Requête AJAX pour le point de terminaison `/login`
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json' // Type de contenu JSON
                    },
                    body: JSON.stringify({ email, password }) // Corps de la requête
                });

                if (response.ok) {
                    const data = await response.json(); // Récupération de la réponse en JSON

                    // Stocker le jeton JWT dans un cookie
                    document.cookie = `token=${data.access_token}; path=/`;

                    // Rediriger vers la page principale
                    window.location.href = '/index.html';
                } else {
                    // Affiche un message d'erreur si les identifiants sont invalides
                    errorMessage.textContent = "Échec de la connexion. Veuillez vérifier vos identifiants.";
                }
            } catch (error) {
                console.error('Erreur réseau ou serveur :', error);
                errorMessage.textContent = "Une erreur est survenue. Veuillez réessayer.";
            }
        });
    }
});
