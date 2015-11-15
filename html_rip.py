# Programming to Rip Body Text of HTML
# to be put into alchemy API for sentiment analysis

# imports
from bs4 import BeautifulSoup
import urllib.request
import re
import pprint as pp

# *************************************************************************** #

def to_text(website): 
	"""Rips visible elments __main__"""
	texts = get_html(website)
	visible_text = list(filter(visible, texts))
	rip = "".join(visible_text)

	return("".join(rip))
   
# *************************************************************************** #

def get_html(website):
	"""Rips the body text from the page"""
	with urllib.request.urlopen(website) as page:
		soup = BeautifulSoup(page)
		body = soup.body
		texts = body.findAll(text=True)

	return texts

# *************************************************************************** #

def visible(element):
	"""For analysis of HTML tags & returns True for text visible to the user"""
	tags = ['style', 'script', '[document]', 'head', 'title']

	if element.parent.name in tags:
		return False
	elif re.match('<!--.*-->', str(element)):
		return False
	# elif re.match('/*.*/', str(element)):
	# 	return Falsef
	else:
		return True

# *************************************************************************** #

def link_or_nah(_input):
	"""link or just text"""
	x = list(_input)
	for element in x:
		if element == " ":
			return False
	return True

# *************************************************************************** #

# if _input is a link call mains
if link_or_nah(_input):
	text = to_text(_input)
else:
	# print("text is already good to go.")
	pass