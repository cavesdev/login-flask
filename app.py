from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

engine = create_engine('postgresql://localhost/login_flask')
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        db.execute('INSERT INTO users (username, password) VALUES (:username, :password)',
                   {'username': username, 'password': password })
        db.commit()
        return render_template('signup.html')
    else:
        return render_template("signup.html")