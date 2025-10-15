from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import session, redirect
from flask import render_template
from datetime import datetime
from functools import wraps

import database_manager as dbHandler

app = Flask(__name__)
app.secret_key = "your_secret_key"


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("signup"))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
@login_required
def index():
    data = dbHandler.listMessages()
    latest_messages = {
        1: dbHandler.get_latest_message(1),
        2: dbHandler.get_latest_message(2),
        3: dbHandler.get_latest_message(3)
    }
    return render_template("/index.html", content=data, latest_messages=latest_messages)


@app.route("/messages1.html", methods=["GET", "POST"])
@login_required
def messages1():
    if request.method == "POST":
        content = request.form.get("message")
        full_name = session.get("username", "Anonymous")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        dbHandler.add_message(full_name, content, 1, time)
        return redirect(url_for("messages1"))
    messages = dbHandler.get_messages_by_chat(1)
    return render_template("/messages1.html", messages=messages)


@app.route("/messages2.html", methods=["GET", "POST"])
@login_required
def messages2():
    if request.method == "POST":
        content = request.form.get("message")
        full_name = session.get("username", "Anonymous")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        dbHandler.add_message(full_name, content, 2, time)
        return redirect(url_for("messages2"))
    messages = dbHandler.get_messages_by_chat(2)
    return render_template("/messages2.html", messages=messages)


@app.route("/messages3.html", methods=["GET", "POST"])
@login_required
def messages3():
    if request.method == "POST":
        content = request.form.get("message")
        full_name = session.get("username", "Anonymous")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        dbHandler.add_message(full_name, content, 3, time)
        return redirect(url_for("messages3"))
    messages = dbHandler.get_messages_by_chat(3)
    return render_template("/messages3.html", messages=messages)


@app.route("/")
def root():
    return redirect(url_for("signup"))


@app.route("/signup.html", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = dbHandler.listusers()
        print("All users:", users)
        for user, pw in users:
            print("Checking:", user, pw) 
            if user == username and pw == password:
                session["username"] = username
                return redirect(url_for("index"))
        return render_template("/invalid_credentials.html"), 401
    users = dbHandler.listusers()
    return render_template("/signup.html", users=users)


@app.route("/signupp.html", methods=["GET", "POST"])
def signupp():
    if request.method == "POST":
        Full_Name = request.form.get("username")
        Password = request.form.get("password")
        Email = request.form.get("email")

        dbHandler.adduser(Full_Name, Password, Email)
        return redirect(url_for("index"))
    users = dbHandler.listusers()
    return render_template("/signupp.html", users=users)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/signup.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5100)
