import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    """Creates the user"""

    if request.method == "GET":
        return render_template("register.html")

    #Gets form information
    if request.form.get("name"):
        name = request.form.get("name")
        print(name)
    else:
        name = None
    if request.form.get("password"):
        password = request.form.get("password")
        print(password)
    
    return render_template("register.html", name=name)
