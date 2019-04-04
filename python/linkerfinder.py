# coding: utf-8
import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
    
soup.find_all(['a','b'])
for tag in soup.find_all(True):
    print(tag.name)
    
