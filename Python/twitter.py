# Goal is to prompt user for their twttr profile & extract info from it/
# infer from it that what is the user's username

import re

url = input("URL: ").strip()

# replace(what do you want to replace, what do you want to replace it with)
# Similar to find and replace in VSCode 
#username = url.replace("https://twitter.com/", "")
#username = url.removeprefix("https://twitter.com/")
#print(f"Username: {username}")

# Essentially is find & replace using regexes
#username = re.sub(r"^(https|http)://twitter\.com/", "", url)

# Useful for cleaning up data
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

#matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
#if matches:
#if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):

# Using non-capturing version of parenthesis/groupin
#if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):

# Because twttr docs have rules for the combination of usernames i.e, 
# what char to be used.
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
# if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")

#print(f"Username: {username}")