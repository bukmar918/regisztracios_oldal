from flask import Flask, render_template
import hashlib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "register.html"
    )

@app.route("/submit", methods=["POST", "GET"])
def submit():
    form = {
        
        
    }