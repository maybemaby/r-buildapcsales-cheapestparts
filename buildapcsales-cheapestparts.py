#! python3
# Scrapes cheapest pc parts of the day from reddit.

import praw, re

# praw object
reddit = praw.Reddit(
    client_id = "Placeholder",
    client_secret = "Placeholder",
    user_agent = "Placeholder",
    username = "Placeholder",
    password = "Placeholder"
)

PriceRegex = re.compile(r'\$\d+\.?(\d{2})?')
PartRegex = re.compile(r'(\[.{1,10}\])')
# Looping through posts for the day.
print('Here are the cheapest PC parts from r/buildapcsales for today.')
cheapParts = {}
for submission in reddit.subreddit('buildapcsales').top('day', limit = 50):
    price = PriceRegex.search(submission.title)
    price = float(price.group()[1:])
    part = PartRegex.search(submission.title)
    partcategory = part.group(1)
    postdata = []
    if partcategory not in cheapParts:
        postdata.append(submission.title)
        postdata.append(price)
        postdata.append(submission.url)
        cheapParts.setdefault(partcategory.upper(), postdata)
    elif cheapParts[partcategory.upper()][1] > price:
        cheapParts[partcategory.upper()][1] = price

# Results
for k,v in cheapParts.items():
    print(v[0] +'\nURL:' + v[-1])
