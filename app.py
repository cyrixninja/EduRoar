# Importing Libraries
import flask as Flask
import generate as gen


# Creating a Flask app
app = Flask(__name__)


# Defining the route for the home page
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)