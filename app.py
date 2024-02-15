# Importing Libraries
import google.generativeai as genai
import flask as Flask

# Selecting the Gemini model
model = genai.GenerativeModel('gemini-pro')

# Creating a Flask app
app = Flask(__name__)


# Defining the route for the home page
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)