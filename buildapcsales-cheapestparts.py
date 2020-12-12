#! python3
# Scrapes cheapest pc parts of the day from reddit.

import praw, re

# praw object
reddit = praw.Reddit(
    client_id = "lZQ2lRgVygfsbw",
    client_secret = "2Z2hbuBBkmg91xrqdzlJHRajiqZTxA",
    user_agent = "Windows:lZQ2lRgVygfsbw:v0.0.1 (by u/Free_Brandon)",
    username = "Free_Brandon",
    password = "Donyhm97"
)

PriceRegex = re.compile(r'\$\d+\.?(\d{2})?')
PartRegex = re.compile(r'(\[.{1,10}\])')
# Looping through posts for the day.
print('Here are the cheapest PC parts from r/buildapcsales for today.')
cheapParts = {}
partLinks = {}
for submission in reddit.subreddit('buildapcsales').top('day', limit = 50):
    price = PriceRegex.search(submission.title)
    part = PartRegex.search(submission.title)
    partcategory = part.group(1)
    if partcategory not in cheapParts:
        cheapParts.setdefault(partcategory.upper(), float(price.group()[1:]))
    elif cheapParts[partcategory.upper()] > float(price.group()[1:]):
        cheapParts[partcategory.upper()] = float(price.group()[1:])

print(cheapParts)