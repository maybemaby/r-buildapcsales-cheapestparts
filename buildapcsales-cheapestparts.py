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

PriceRegex = re.compile(r'\$\d+\.?\d{2}')
PartRegex = re.compile(r'\[.+\]')
# Looping through posts for the day.
print('Here are the cheapest PC parts from r/buildapcsales for today.')
cheapParts = {}
partLinks = {}
for submission in reddit.subreddit('buildapcsales').top('day', limit = 50):
    price = PriceRegex.search(submission)
    part = PartRegex.search(submission)
    if part.group() not in cheapParts:
        cheapParts.setdefault(part.group(), float(price.group()[1:]))
    elif cheapParts[part.group()] > float(price.group()[1:]):
        cheapParts[part.group()] = float(price.group()[1:])

print(cheapParts)