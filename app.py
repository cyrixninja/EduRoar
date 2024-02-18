# Importing Libraries
from flask import Flask, render_template, request
import generate as gen
import jsonify 
#import firebase_admin
#from firebase_admin import credentials, auth

# Initializing the Firebase Admin SDK with the service account credentials
#cred = credentials.Certificate("key.json")
#firebase_admin.initialize_app(cred)


# Creating a Flask app
app = Flask(__name__)

@app.route('/', methods=["GET",'POST'])
def index():
    print("Hello")
    return render_template('index.html', **locals())

@app.route('/learn', methods=["GET",'POST'])
def learn():
    print("Hello")
    return render_template('learn.html', **locals())

@app.route('/register', methods=["GET",'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        print(name)
        print(email)
        print(password)
    return render_template('register.html', **locals())

@app.route('/signin', methods=["GET",'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email)
        print(password)
    return render_template('signin.html', **locals())

# Defining the route for the home page
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)