from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/sayHello')
def sayHello():
    return "I said Hello!"

if __name__ == '__main__':
    app.run()
