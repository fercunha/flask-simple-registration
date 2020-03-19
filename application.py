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

@app.route("/login", methods=["POST"])
def login():
    return 'OK', 200
    
@app.route("/register", methods=["POST", "GET"])
def register():
    """Creates the user"""

    if request.method == "GET":
        if request.form.get("user"):
            name = request.form.get("user")
            return render_template("register.html", name=name)
        else:
            return render_template("register.html")
    else:
        #Gets form information
        if request.form.get("firstName"):
            firstName = request.form.get("firstName")
            print(firstName)
        if request.form.get("lastName"):
            lastName = request.form.get("lastName")
            print(lastName)
        if request.form.get("user"):
            name = request.form.get("user")
            print(name)
        if request.form.get("password"):
            password = request.form.get("password")
            print(password)

        return render_template("success.html")

if __name__ == "__main__":
    main()
