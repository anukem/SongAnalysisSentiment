from flask import Flask, render_template
import json
import datetime as dt

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')