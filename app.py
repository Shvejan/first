from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "hola wrld!"

@app.route("/<string:name>")
def next(name):
    return f"hola ,{name}!"
