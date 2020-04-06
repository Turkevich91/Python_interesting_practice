from requests_html import HTMLSession
from bs4 import BeautifulSoup as BS

session = HTMLSession()
result = session.get("https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
result.html.render()
#r = requests.get('https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6')
html = BS(result.content, 'html.parser')

#print(html)

for el in html.select('div'):
    title = el.select('div')
    for x in range(len(title)):
        print(title[x])
