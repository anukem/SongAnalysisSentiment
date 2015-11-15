from __future__ import print_function
from alchemyapi import AlchemyAPI
from flask import request
import requests
from flask import Flask, render_template
app = Flask(__name__)
app.config["DEBUG"] = True
def determineSubject(text):
	alchemyapi = AlchemyAPI()
	response = alchemyapi.sentiment('text', text, {'sentiment': 1})
	if response['status'] == 'OK':
		return response['docSentiment']['score'] + '\n' + render_template('index.html')
	'''if response['status'] == 'OK':
					return response['keywords']
				return "This passage can't be interpreted."'''
	'''if response['status'] == 'OK':
				    for keyword in response['keywords']:
				        print(keyword['text'])
				        print('relevance: ', keyword['relevance'])
				        print('sentiment: ', keyword['sentiment']['type'])
				        if 'score' in keyword['sentiment']:
				            print('sentiment score: ' + keyword['sentiment']['score'])
				        print('')
				else:
				    return 'Error in keyword extaction call: '''

@app.route("/", methods=["GET", "POST"])
def main():
	if request.method == 'POST':
		x = str(request.form['username'])
		return determineSubject(x)
	else:
		return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)	



