from flask import Flask, redirect, session, render_template,request, jsonify,flash
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("secret_key")

@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method =="POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        session["name"]=username
        session["email"]=email
        session['passwd']= password
        with open("dashboard.txt","a") as f:
                    f.write(f"Name: {username}\n Email:{email}\n Password:{password}\n")
        if not username or not email or not password:
            flash("Error!, Fill in all the details")
            return redirect("/")
        flash("login Successful, redirecting....")
        

        return redirect("/dashboard")
@app.route("/dashboard")
def dashboard():
    username = session.get("name")
    email = session.get("email")
    password = session.get("passwd")
    return render_template("dashboard.html", username=username, email=email, password = password)
@app.route("/project",methods = ["GET"])
def project():
    user = session.get("name")
    email = session.get("email")
    return render_template("project.html", username = user, email=email)

@app.route("/data", methods = ["GET"])
def data():
    return render_template ("dashboard.txt")

@app.route("/analytics",methods = ["GET"])
def analytic():
    user = session.get("name")
    email = session.get("email")
    return render_template("analytics.html", username = user, email=email)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ =="__main__":
    app.run(host="0.0.0.0", port =5000)
