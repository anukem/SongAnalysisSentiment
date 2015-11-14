from flask import Flask
from songdictionary import getSentValue
from songdictionary import getSongUrlFromValue
app = Flask(__name__)

from flask import render_template
@app.route("/")
def testpage():
    value = 1
    link = getSongUrlFromValue(value)
    return render_template('testpage.html', songUrl = link)

if __name__ == '__main__':
    app.debut = True
    app.run(host='0.0.0.0')
