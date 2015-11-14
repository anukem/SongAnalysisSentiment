from flask import Flask, render_template
from songdictionary import getSentValue
from songdictionary import getSongUrlFromValue
import json
import datetime as dt
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/music")
def music():
    value = 1 # this is arbitrary. Will reflect the result of the sentiment analysis
    link = getSongUrlFromValue(value)
    return render_template('testpage.html', songUrl = link)

# Added this because it wouldn't start
if __name__ == '__main__':
    app.debut = True
    app.run(host='0.0.0.0')