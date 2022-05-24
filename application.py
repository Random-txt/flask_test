from distutils.log import debug
from flask import Flask

application = Flask(__name__)
app = application

@application.route('/')
def test_world():
    return 'test is working'

if __name__ == "__main__":
    app.run(debug=True)