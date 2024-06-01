# A module that gives access to all of the functions associated with the
# system like cmd-line args
import sys

#try:
    # argv() is an argument vector in sys lib which stores the user input 
    # from the terminal while execution and goes as counting i.e., 1 for first
    # and likewise
    # Similar to a list
    # sys.agv[0] stores the name of the file being executed/interpretted
#    print("hello, my name is", sys.argv[1])
    
#except IndexError:
#    print("Too few arguments")
    
# There is no requirement for exception handling everytime
# Avoiding all index errors by checking using conditionals
if len(sys.argv) < 2:
    #print("Too few arguments")
    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
    #print("Too many arguments")
 #   sys.exit("Too many arguments")
 
# Taking slices of the argv that we need, starting from 1st element till the end
# sys.argv[begin:end] is a slice of argv

# A negative position for the slice indicates that it will start from 
# the last/end of the list i.e., run in the opposite direction
#for arg in sys.argv[1:]:
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
#else:
#    print("hello, my name is", sys.argv[1])

print("\nhello, my name is", sys.argv[1])