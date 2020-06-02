#Britni Canale
#SoftDev1 pd 6
#K26 -- Getting More REST
#2018-11-15


from flask import Flask, render_template, session, request, url_for, redirect, flash
import os

app = Flask(__name__)

@app.route("/", methods = ['POST', "GET"])
def welcome():
    if 'username' not in session:
        if "uname" not in request.form:
            return redirect(url_for("login"))
    return render_template("temp.html")

@app.route("/login", methods = ['POST', "GET"])
def login():
    if 'username' in session:
        flash("You are already logged in")
        return redirect(url_for("welcome"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    if 'username' in session:
        flash("You have successfully logged out")
        session.clear()
    return redirect(url_for("login"))

@app.route("/register", methods = ["GET"])
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
