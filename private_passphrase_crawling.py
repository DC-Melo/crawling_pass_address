#!/usr/bin/env python
#coding:utf-8
import requests
from bs4 import BeautifulSoup
import time
import os
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
max_page=421
url_terp = 'http://privatekeys.pw/bitcoin/brainwallet/{}'
rows = list()
for index in range(1,max_page):
    url = url_terp.format(index)
    print(url)
    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r,'lxml')
    table = soup.find('table', {'class': 'table table-striped table-hover'})
    trs = table.find_all('tr')[1:]
    for tr in trs:
        row=[td.text.replace('\n', '').replace('\xa0', '').strip() for td in tr.find_all('td')]
        print(row)
        with open("private_passphrase.txt", "a") as output:
            output.write("\t".join(row)+"\n")
    time.sleep(5)
