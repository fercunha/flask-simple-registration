from flask import Flask, render_template, request
import mydb
import datetime
from passlib.hash import sha256_crypt

mydb.create()

app = Flask(__name__)

def main():
    pass

@app.route("/")
def index():
    #TODO If has session, return index.html

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user_infos = mydb.db.execute("SELECT username, password FROM users WHERE username = :username", {"username": username}).fetchall()
    if len(user_infos) == 1:
        for info in user_infos:
            saved_password = info.password
            if sha256_crypt.verify(password, saved_password):
                return render_template("success.html", message='Login successful!')
            else:
                return render_template("login.html", error_message='Wrong username or password'), 403
    else:
        return render_template("login.html", error_message='Duplicate user!'), 409
    
@app.route("/register", methods=["POST", "GET"])
def register():
    """Creates the user"""
    #TODO Hash the password in the front-end.
    #TODO Return to login page or open app console after successful registration.

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
        password = request.form.get("password")
        password = sha256_crypt.hash(password)

        #Check if username already exists
        print(f"Checking if user {username} exists.")
        if mydb.db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount == 0:
                print(f"User {username} is available.")
        else:
            message = "User " + username + " has already been picked."
            print(message)
            return render_template("error.html", message=message), 409
        # try:
        #     if mydb.db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount == 0:
        #         print(f"User {username} is available.")
        #     else:
        #         message = "User " + username + " already picked."
        #         print(message)
        #         return render_template("error.html", message=message), 409
        # except:
        #     return render_template("error.html", message='Error connecting to the database.'), 500

        try:
            registration_date = datetime.datetime.now()
            print(registration_date)
            mydb.db.execute("INSERT INTO users (name, lastname, username, password, registration_date) VALUES (:name, :lastname, :username, :password, :registration_date)",
                {"name": name, "lastname": lastname, "username": username, "password": password, "registration_date": str(registration_date)})
            mydb.db.commit()
            message = "User " + username + " registered successfully!"
            return render_template("success.html", message=message, redirect=True)
        except:
            return render_template("error.html", message='Registration failed.'), 400

if __name__ == "__main__":
    main()
