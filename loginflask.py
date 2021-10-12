from flask import Flask, abort, g, redirect, render_template, request, session, url_for
import sqlite3

verbindung = sqlite3.connect("user.db")
anweisung = create.table(personen("user"))
verbindung.commit()

class User:
    def __init__(sef, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User: {self.username}>"

users = ["user.db"] #Datenbank hier?
users.append(User(id = 1, username = "sara", password ="1234"))



app = Flask(__name__)
app.secrect_key = "key"

@app.before_request()
def before_request():
    if "user_id" in session:
        user = [x for x in users if x.id == session["user_id"][0]
        g.user == user 

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("user_id", None)
        username = request.form["username"]
        password = request.form["password"]

        user =[x for x in users if x.username == username][0]
        if user and user.password == password:
            session["user_id"] == user.id
            return redirect(url_for("profile"))

        return redriect(url_for("login"))

    return render_template("login.html") #Verknüpfung html

@app.profile("/profile")
def profile():
    if not g.user:
        return redirect(url_for("login"))

    return render_template("profile.html") #Verknüpfung html


verbindung.close()