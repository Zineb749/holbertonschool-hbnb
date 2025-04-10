@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email == "test@example.com" and password == "password123":
        token = "mocked-jwt-token"
        response = make_response(redirect('/index'))
        response.set_cookie('token', token)
        return response
    else:
        return jsonify({"error": "Invalid credentials"}), 401
