from flask import Blueprint

authentication = Blueprint('authentication', __name__)

@authentication.route('/login')
def login():
    return "<p>Logged In, Welcome User!</p>"

@authentication.route('/logout')
def logout():
    return "<p>Logged Out :(</p>"

@authentication.route('/sign-up')
def sign_up():
    return "<p>Signed Up, Welcome New User!.</p>"