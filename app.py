from flask import Flask,render_template
import datetime
app = Flask(__name__) 

@app.route("/")         #default page -> https://127.0.0.1:5000/
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/<string:name>")     #http://127.0.0.1:5000/ravjot
def hello(name):
    return f"<h1>Hello, {name}</h1>!"

@app.route("/year")
def year():
    now=datetime.datetime.now()
    new_year = now.month== 1 and now.day==1
    return render_template("index.html",new_year=new_year)