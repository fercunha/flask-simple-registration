import os
from flask import Flask, render_template, request
import mydb
import datetime

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
        if request.form.get("username"):
            username = request.form.get("username")
            return render_template("register.html", name=username)
        else:
            return render_template("register.html")
    else:
        #Gets form information
        name = request.form.get("name")
        lastname = request.form.get("lastname")
        username = request.form.get("username")
        # checkusername = mydb.db.execute("SELECT * FROM users").fetchone()
        password = request.form.get("password")
        try:
            registration_date = datetime.datetime.now()
            print(registration_date)
            mydb.db.execute("INSERT INTO users (name, lastname, username, password, registration_date) VALUES (:name, :lastname, :username, :password, :registration_date)",
                {"name": name, "lastname": lastname, "username": username, "password": password, "registration_date": str(registration_date)})
            mydb.db.commit()
            message = "User " + username + " registered successfully!"
            return render_template("success.html", message=message)
        except:
            return render_template("error.html", message='Registration failed.'), 400

if __name__ == "__main__":
    main()
