#! python3
# Scrapes cheapest pc parts of the day from reddit.

import requests, bs4, os, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

url = 'https://www.reddit.com/r/buildapcsales/top/'
print(f'Here are the cheapest PC parts from {url} for today:')

res = requests.get(url)
res.raise_for_status

