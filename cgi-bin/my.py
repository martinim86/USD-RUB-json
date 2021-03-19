#! /usr/bin/python3
# -*- coding: UTF-8 -*-
import cgi, sys
import re
import json

print("Content-type: text/html\n")
import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='inline-stocks__value_inner')
num = float(quotes[0].text.replace(',', '')) / 100

form = cgi.FieldStorage()
x = {
"Input Dollars": form['$'].value,
"Rubles": float(form['$'].value) * num,
}
y = json.dumps(x)
print y



