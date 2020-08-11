import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://www.boxofficemojo.com/yearly/'

resp = requests.get(url)
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text, 'lxml')

# table = soup.find_all('table', attrs={'cellspacing': '1'})
table = soup.find('div', {'id': 'table'})
rows = table.find_all('tr')

colname = rows.pop(0)
colname = [i.text for i in colname]
rows = [list(row.stripped_strings) for row in rows]

df = pd.DataFrame(rows, columns=colname)

results = os.path.abspath('/Users/kail/Documents/PycharmProjects/crawler')
if not os.path.exists(results):
    os.makedirs(results)

filename = os.path.join(results, 'boxofficemojo.csv')
df.to_csv(filename, index=False)
print('Save csv to {}' . format(filename))

