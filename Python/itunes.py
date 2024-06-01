import requests
import sys

# This module/lib helps in manipulating and cleaning the recieved json data
# in a more human understandable/readabble way
import json

# Some error checking
if len(sys.argv) != 2:
    # premature exit i.e., exits from the whole program for now
    sys.exit()
    
# Here is the python code that is effectively pretending to be a web browser
# And it requests some url from the server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(response.json())

# This line here does the reduction and things using the method
# dumps(for dump string) of json lib and give a more readable file/data
# indent = 2 is a named parameter
#print(json.dumps(response.json(), indent = 2))

# o for object i.e., kinda json object
o = response.json()
for result in o["results"]:
    print(result["trackName"])
