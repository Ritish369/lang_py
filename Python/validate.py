# Library/module for working with regular expressions
import re

email = input("What's your email? ").strip()
#email = input("What's your email? ").strip().lower()

# Not much correct as i/p can be just @ and . because they can be anywhere
# if traditionals for email are not assumed/there
"""
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
    """
    
"""
# More Logial way i.e., need to be more methodical here
username, domain = email.split("@")

#if (username) and ("." in domain):
if username and domain.endswith(".edu"):
    print("valid")
else:
    print("Invalid")"""
    
# All the above ways for pattern matching would take a lot of time for precise
# working and other comparisons for validating i.e., condering every mail
# specifics and doing multiple splits and all

# To avoid this, there are terms to work with known as regular expressions
# through a library/module called "re".

# re.search() fn uses STATE MACHINES to check if matches happened correclty

# Sorta qualifies as a regular expression
#if re.search("@", email):

# Now, it is moving towards being a regex
#if re.search(".*@.*", email):

# Both are equivalent
# \. is referred to as a special sequence telling that we literally want 
# to match on a dot. Further implying to match with .edu i.e., to treat the
# symbols literally, not specially.
# To not let the interpreter misinterpret any of the \ with there usual
# meanings, we use the pattern passed to search fn as a RAW STRING.
#if re.search(r".+@.+\.edu", email):
#if re.search("..*@..*", email):

# To be more precise with the patterns, we use ^ and $ symbols which 
# ultimatelt tells the search fn that to look for the exact match
#if re.search(r"^.+@.+\.edu$", email):

# More advancements using the set of char [] and the completent of it [^]
# Done to avoid @@@ and other repetitive combinations of inputs
# [^@] means any char except @ sign
#if re.search(r"^[^@]+@[^@]+\.edu$", email):

# To make the regex more standardized acc to respective orgs, then do this
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): 
 
# Because some patterns are common and thus, built into addntional patterns
# in the lib
# "\w" is a word character...as well as no.s & the under score 
# i.e., known as an alphanumeric symbol
#if re.search(r"^\w+@\w+\.edu$", email): 

# For handling the lowercase and uppercase of user input. Flags also used
# in one of the ways
#if re.search(r"^\w+@\w+\.edu$", email.lower()):
#if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE): 
 
# For more than one domain name i.e., presencee of sub-domains
#if re.search(r"^\w+@\w+\.\w+\.edu$", email, re.IGNORECASE): 
 
# because of the sub-domains handling in the prev regex, the normal and usual
# mailing regex, onlywith domain, broke. Thus, can be resolved as:
# (\w+\.)? which is a grp, tells either this pattern is there or not 
# i.e., optional and works with both sub-domain and domain mails
#if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): 
 
# Other ways to handle same kinda things on username side
#if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    
# or
if re.search(r"^[a-zA-Z0-9_\.]+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): 
    print("Valid")
else:
    print("Invalid")