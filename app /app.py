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
	# if response['status'] == 'OK':
			return response['docSentiment']['score']



