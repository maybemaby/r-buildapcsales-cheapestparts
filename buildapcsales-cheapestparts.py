#! python3
# Scrapes cheapest pc parts of the day from reddit.

import requests, bs4,logging, re
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)

PartCategory = {'[CPU]':10000,'[GPU]':10000, '[RAM]':10000, '[HDD]':10000, '[SSD]':10000, '[Motherboard]':10000, '[Monitor]':10000,
'[PSU]':10000, '[Webcam]':10000, '[Controller]':10000, '[Laptop]':10000, '[Other]':10000, '[VR]':10000, '[Case]':10000, '[Cooler]':10000,
'[Headphones]':10000, '[Fan]':10000, '[Prebuilt]':10000, '[Headset]':10000, '[Optical Drive]':10000, '[OS]':10000, '[Speakers]':10000,
'[Keyboard]':10000, '[Networking]':10000, '[Furniture]':10000, '[Mouse]':10000, '[Bundle]':10000, '[HTPC]':10000, '[Cables]':10000,
'[Flash Drive]':10000, '[Router]':10000, '[Mic]':10000}
PartLinks = {'[CPU]':'','[GPU]':'', '[RAM]':'', '[HDD]':'', '[SSD]':'', '[Motherboard]':'', '[Monitor]':'',
'[PSU]':'', '[Webcam]':'', '[Controller]':'', '[Laptop]':'', '[Other]':'', '[VR]':'', '[Case]':'', '[Cooler]':'',
'[Headphones]':'', '[Fan]':'', '[Prebuilt]':'', '[Headset]':'', '[Optical Drive]':'', '[OS]':'', '[Speakers]':'',
'[Keyboard]':'', '[Networking]':'', '[Furniture]':'', '[Mouse]':'', '[Bundle]':'', '[HTPC]':'', '[Cables]':'',
'[Flash Drive]':'', '[Router]':'', '[Mic]':''}

PriceRegex = re.compile(r'\$\d+\.?\d{2}')
url = 'https://old.reddit.com/r/buildapcsales/top/'
headers = {'User-Agent': 'Mozilla/5.0'}

print(f'Here are the cheapest PC parts from {url} for today:')
res = requests.get(url, headers = headers)
res.raise_for_status
soup = bs4.BeautifulSoup(res.text, 'html.parser')

PostSelect = soup.select('a[class="title may-blank outbound"]')
for post in PostSelect:
    logging.debug(post.get_text())
    link = post.get('href')
    price = PriceRegex.search(post.get_text())
    logging.debug(price)
    if price == None:
        continue
    else:
        price = float(price.group()[1:])
    for k,v in PartCategory.items():
        if k in post.get_text() and price < v:
            PartCategory[k] = price
            PartLinks[k] = link

for k,v in PartCategory.items():
    if v == 10000:
        continue
    else:
        print(k[1:-1] + ': $' + str(v) + ' URL: ' + PartLinks[k])
        print('\n')

input('Enter any key to exit..')

