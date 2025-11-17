import pandas as pd
import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
response=requests.get('https://www.ambitionbox.com/list-of-companies?page=1',headers=headers)
print(response.status_code)
# print(response.text)
soup=BeautifulSoup(response.text,'lxml')

for i in soup.find_all('h2'):
    print(i.text.strip())

for i in soup.find_all('p'):
    print(i)
# print(soup.prettify)
