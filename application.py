import os
from flask import Flask, render_template, request
import mydb

mydb.create()

app = Flask(__name__)

def main():
    pass

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return 'OK', 200
    
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

if __name__ == "__main__":
    main()
