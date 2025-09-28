from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("admin"),
    "user": generate_password_hash("user")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username], password):
        return username

@app.route('/')
@auth.login_required
def hello():
    return '<p>Hello, protected World!</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8078)

