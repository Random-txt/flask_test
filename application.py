from flask import Flask, request


application = Flask(__name__)

@application.route('/')
def index():
    return "Hello world. Pray that I see this"

if __name__ == '__main__':
    application.run()
    