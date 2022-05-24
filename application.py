from distutils.log import debug
from email.mime import application
from flask import Flask

application = Flask(__name__)
app = application

@app.route('/')
def test_world():
    return 'test is working'

if __name__ == "__main__":
    app.run(debug=True)