from flask import Flask, render_template, request

from tables import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/login_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        logins = Users.query.filter_by(username=username).first()
        return render_template('index.html')

    else:
        return render_template('login.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        db.session.add(Users(username=username, password=password))
        db.session.commit()

        user_list = Users.query.all()
        return render_template('users.html', users=user_list)

    else:
        return render_template('signup.html')


@app.route("/users")
def users():
    user_list = Users.query.all()
    return render_template('users.html', users=user_list)