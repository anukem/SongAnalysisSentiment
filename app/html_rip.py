#PYTHON 3

# Programming to Rip Body Text of HTML
# to be put into alchemy API for sentiment analysis

url= input("Link: ")

# imports
from bs4 import BeautifulSoup
import urllib.request
import re
import pprint as pp

   
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
	# 	return False
	else:
		return True

# *************************************************************************** #

def main(website): 
	"""Rips visible elments"""
	texts = get_html(website)
	visible_text = list(filter(visible, texts))
	rip = "".join(visible_text)

	return("".join(rip))

if __name__ == "__main__":
	main(url)

#pp.pprint(get_html(url))
