from flask import Flask, render_template, request, jsonify
import json
import os
import hashlib

app = Flask(__name__)
adatok = "adatok.json"
felh = form.get("user")
email = form.get("email")
jelszó = form.get("password")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("register.html")

def passvalid():
    encrypted = hashlib.md5(jelszó.encode())
    with open


@app.route("/submit", methods=["POST", "GET"])
def submit():
    form = {
        
        
    }