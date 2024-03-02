from flask import Flask
from flask import redirect
from flask import make_response
from flask import abort

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)


# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is %s</p>' % user_agent


# @app.route('/')
# def index():
#     return '<h1>Bad Request<h1>', 400


# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response


# @app.route('/')
# def index():
#     return redirect('https://www.example.com')

def load_user(id):
    pass


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404, message="User not found")
    return 'hello' + user['name']




if __name__ == '__main__':
    app.run(debug=True)
