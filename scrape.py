from ast import keyword
import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep

# http://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# imports a csv file with the url's to scrape
#prod_tracker = pd.read_csv('trackers/TRACKER_PRODUCTS.csv', sep=';')
#prod_tracker_URLS = prod_tracker.url

# fetch the url
page = requests.get("https://www.amazon.com/s?k={}".format(keyword), headers=HEADERS)

# create the object that will contain all the info in the url
soup = BeautifulSoup(page.content, features="lxml")
print(page.content)

# product title
title = soup.find(id='productTitle').get_text().strip()
