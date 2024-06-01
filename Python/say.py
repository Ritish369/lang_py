import cowsay
import sys

# Using the custom library/module fn hello from the file sayings
from sayings import hello # below one also
# The last __name__ conditional lets the interpreter to ignore the main 
# of sayings.py as this module is being imported (when reading this file)
# thus, leading to no execution of main and just imports/ uses the reqd imported fn

if len(sys.argv) == 2:
    # A cow says these things
    #cowsay.cow("hello, " + sys.argv[1])
    
    # Now, a trex says
    #cowsay.trex("hello, " + sys.argv[1])
    
    # Using custom module fn, hello here to demo the use of importing custom
    # libs
    hello(sys.argv[1])
