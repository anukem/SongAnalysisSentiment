from bs4 import BeautifulSoup
import urllib.request
import re
import pprint as pp

url1 = "http://pathsensitive.blogspot.com/2015/08/sources-of-power.html"

# *************************************************************************** #

def get_html(website):
	"""Rips the body text from the page"""
	with urllib.request.urlopen(website) as page:
		html = page.read()
		soup = BeautifulSoup(html)
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
