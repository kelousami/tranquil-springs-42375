from flask import Flask
application = Flask(__name__)

import logging
logging.basicConfig(level=logging.DEBUG)

@application.route('/')
def hello():
    logging.info("Saying hello")
    return "Hello World!"

@application.route('/<name>')
def hello_name(name):
    logging.info("Saying hello to {}".format(name))
    return "Hello {}!".format(name)

if __name__ == '__main__':
    application.run()
