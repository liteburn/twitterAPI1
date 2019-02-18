from flask import Flask, render_template, request,redirect
import json
from twitter2 import get_map

app = Flask(__name__)

students = {"students":[]}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    loc = request.form.get("domain")
    if not request.form.get("domain"):
        return render_template("failure.html")
    get_map(loc)
    return render_template("Map.html")



if __name__ == "__main__":
    app.run()

