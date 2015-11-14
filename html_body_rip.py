import urllib.request

opener = urllib.request.FancyURLopener({})
url = "http://stackoverflow.com/"
f = opener.open(url)
content = f.read()