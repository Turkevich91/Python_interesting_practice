# from requests_html import HTMLSession
# from bs4 import BeautifulSoup as BS
#
# session = HTMLSession()
# result = session.get("https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
# result.html.render()
# #r = requests.get('https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6')
# html = BS(result.content, 'html.parser')
#
# #print(html)
#
# for el in html.select('div'):
#     title = el.select('div')
#     for x in range(len(title)):
#         print(title[x])
import os, re

S = "1873 PAP 14"
# pattern = re.compile(r'\d+$')
# matches = re.compile(r'\d+$').finditer(S)
# print(re.compile(r'[^\d]\d').match("PAP02", 0))
# for match in re.compile(r'\w+.' + '02').finditer("PAP 02 PAP 12"):
#     print(match)
print(re.findall(r'([a-zA-Z]+|\d+)', S))

# os.mkdir(S, mode=0o777, dir_fd=None)
# os.makedirs(S, mode=0o777, exist_ok=False)
# os.rename(src, dst, src_dir_fd=None, dst_dir_fd=None)
