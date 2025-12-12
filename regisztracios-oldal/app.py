from flask import Flask, render_template, request, jsonify
import json
import os
import hashlib
import re

app = Flask(__name__)
adatok = "adatok.json"
emailreg = r"^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$"


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("register.html")
    if request.method == "POST":
        try:
            user = request.form.get("user", "").strip()
            email = request.form.get("email", "").strip()
            password = request.form.get("password", "").strip()
            password2 = request.form.get("password2", "").strip()

            if not name or not email:
                return redirect(url_for("index"))

            with open(adatok, "r") as f:
                data = json.load(f)

            adatok.append({"user": user, "email": email})

def passvalid(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


@app.route("/submit", methods=["POST", "GET"])
def submit():
    form = {
        
        
    }