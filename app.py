from flask import Flask
app = Flask(__name__)

import logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    logging.info("saying hello")
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    logging.info("saying hello to {}".format(name))
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
