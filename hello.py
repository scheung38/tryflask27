from flask import Flask
import os
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    port = int(os.environ.get("PORT", 5000))
    APP.run(host='0.0.0.0', port=port)
