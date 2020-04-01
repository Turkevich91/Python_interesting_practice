import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://3dnews.ru/')
html = BS(r.content, 'html.parser')

for el in html.select('.content-block-data'):
    title = el.select('.content-block-data h1')
    print(title[0].text)
