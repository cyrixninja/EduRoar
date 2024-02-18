# Register route
@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    user = auth.create_user(
        email=email,
        email_verified=False,
        password=password)
    return jsonify({'uid': user.uid}), 200

# Login route
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = auth.get_user_by_email(email)
    if user:
        # Verify the password
        # If it's valid, create a custom token
        custom_token = auth.create_custom_token(user.uid)
        return jsonify({'token': custom_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401