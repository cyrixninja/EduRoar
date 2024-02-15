# Importing Libraries
import flask as Flask
import generate as gen
import jsonify 
import requests as request 
import firebase_admin
from firebase_admin import credentials, auth

# Initializing the Firebase Admin SDK with the service account credentials
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)


# Creating a Flask app
app = Flask(__name__)

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

# Defining the route for the home page
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)