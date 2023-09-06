from flask import Flask

myapp = Flask(__name__)

@myapp.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    myapp.run(debug=True)
