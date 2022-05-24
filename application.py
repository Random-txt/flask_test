from distutils.log import debug
from flask import Flask

application = Flask(__name__)


@application.route('/')
def test_world():
    return 'test is working'

if __name__ == "__main__":
    application.run(debug=True)