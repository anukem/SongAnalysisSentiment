from flask import Flask
import songdictionary
app = Flask(__name__)

from flask import render_template
@app.route("/")
def songUrl():
    link = getSongUrlFromValue(value)
    return link
    # return render_template('testpage.html', songUrl = link)

if __name__ == '__main__':
    app.run()