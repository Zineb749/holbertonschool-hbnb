from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# A mock API endpoint for login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Dummy validation logic
    if email == "test@example.com" and password == "password123":
        # Generate a mock JWT token (normally you'd use a library for this)
        token = "mocked-jwt-token"
        response = make_response(jsonify({"access_token": token}), 200)
        return response
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Serve the HTML login page
@app.route('/login-page', methods=['GET'])
def login_page():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Login</title>
        </head>
        <body>
            <h1>Login Page</h1>
            <form id="login-form">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                <br>
                <button type="submit">Login</button>
            </form>
            <p id="error-message"></p>
            <script src="/static/scripts.js"></script>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
