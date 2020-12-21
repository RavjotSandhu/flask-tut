from flask import Flask,render_template

app = Flask(__name__) 

@app.route("/")         #default page -> https://127.0.0.1:5000/
def index():
    return render_template("index.html")

@app.route("/<string:name>")     #http://127.0.0.1:5000/ravjot
def hello(name):
    return f"<h1>Hello, {name}</h1>!"