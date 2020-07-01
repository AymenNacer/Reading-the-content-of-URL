import urllib.request
from inscriptis import get_text

url = "https://sjmulder.nl/en/textonly.html"
html = urllib.request.urlopen(url).read().decode('utf-8')

text = get_text(html)
print(text)
