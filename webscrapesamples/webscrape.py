from requests import get
from bs4 import BeautifulSoup as bs

res = get('https://m.facebook.com/login')
html = bs(res.text, 'lxml').prettify()

with open('path\\to\\filename', 'w') as file:
	file.write(str(html))

