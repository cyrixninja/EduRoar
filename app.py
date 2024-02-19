# Importing Libraries
from flask import Flask, render_template, request, redirect , session
import generate as gen
import firebase_admin
from firebase_admin import credentials, auth , db
from flask import url_for
import json

#Initializing the Firebase Admin SDK with the service account credentials
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred , {
    'databaseURL': 'Your databaseURL'
})

# Creating a Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=["GET",'POST'])
def index():
    print("Hello World !")
    return render_template('index.html', **locals())

@app.route('/create', methods=["GET",'POST'])
def create():
    uid = session.get('uid')
    if uid is None:
        return redirect(url_for('signin'))
    user = auth.get_user(uid)
    name = user.display_name

    if request.method == 'POST':
        topic = request.form['topic']
        difficulty = request.form['difficulty']
        level = request.form['level']
        content = gen.generate_content(topic,difficulty,level)
        content_dict = json.loads(content)

        try:
            content_dict = json.loads(content)
            ref = db.reference('/')
            data = (topic + "  "  + difficulty  + "  "   + level)
            user_ref = ref.child(uid).child(data)
            user_ref.push(content_dict)
        except json.JSONDecodeError:
            return redirect(url_for('create'))

    return render_template('create.html', **locals())

@app.route('/register', methods=["GET",'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user(
                display_name = name,
                email=email,
                password=password
            )
            return redirect(url_for('signin'))
        except Exception as e:
            return {'error': str(e)}, 400
    return render_template('register.html', **locals())

@app.route('/signin', methods=["GET",'POST'])
def signin():
    uid = session.get('uid')
    if uid is not None:
        return redirect(url_for('create'))
    else :  
        if request.method == 'POST':
            id_token = request.json['idToken']
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            session['uid'] = uid
            return redirect(url_for('signin'))

    return render_template('signin.html')



@app.route('/learn', methods=["GET",'POST'])
def learn():
    uid = session.get('uid')
    msg = ""
    if uid is None:
        return redirect(url_for('signin'))
    else :
        user = auth.get_user(uid)
        name = user.display_name
        ref = db.reference('/')
        user_data = ref.child(uid).get()
        quizzes = user_data
    return render_template('learn.html', **locals())


@app.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    uid = session.get('uid')
    ref = db.reference(uid)
    ref.delete()
    return redirect(url_for('learn'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)