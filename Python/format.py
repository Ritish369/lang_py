# The goal is to reformat the data into the format that we expect i.e., 
# standardization

import re

# Strings don't support regexes to be used in their respective methods
name = input("What's your name? ").strip()
"""if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")"""

# Using the search fn's return values here to get back specific matches
# that was captured using parenthese/grps
#matches = re.search(r"^(.+), *(.+)$", name)
#if matches:
    #last, first = matches.groups()
    #name = f"{first} {last}"
    
    #last = matches.group(1)
    #first = matches.group(2)
    #name = f"{first} {last}"
    
# Shorter way of writing the above comparisons and all in the if matches sttmnt
# use := operator if you want to assign something and simultaneouly,
# ask an if/elif(boolean) question on the same line about it.
# {:= is known as WALRUS OPERATOR}
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
    
print(f"hello, {name}")