from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "hola wrld!"

@app.route("/<string:name>")
def next(name):
    #name = name.capitalize()
    return f"<h1>hola ,{name}!<h1>"
@app.route("/hola/mexi")
def sec():
    #name = name.capitalize()
    return f"<h1>hola hollaoaa!<h1>"
