"""
# Empty list
names = []

for _ in range(3):
    names.append(input("What's your name? "))
    
# First sorts the list alphabetically i.e., returns ths sorted list
for name in sorted(names):
    print(f"hello, {name}")
"""

# Using File I/O to store these names or information to avoid retyping
# and have them stored at one place.
#name = input("What's your name? ")

# Opens the file that we want and returns a special file handler(value) which is
# assigned to some var allowing to access that file

# "a" for append mode
#file = open("names.txt", "a")

# Writing a file
# More pythonic version of opening and automatically closing the files
# w.r.t the context is by using the with keyword
# Nothing changes but just automates the file open and close process
#with open("names.txt", "a") as file:
    # This LOC is in the context of this with statement 
 #   file.write(f"{name}\n")

#file.close()

# Reading a file
"""
with open("names.txt", "r") as file:
    # This fn returns a list of the file contents that's stored in lines list
    lines = file.readlines()
    
for line in lines:
    #print("hello,", line, end = "")
    # Strips of the new lines from the file and lets the print fn to do the
    # workings i.e., alternate way to the above LOC for print
    print("hello,", line.rstrip())
"""

# More cleaner and elegant way to write the above things for reading file
# is as follows:
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

print("\n")

# The above method is not ideal when a sorted/manipulated way of data
# is needed from the file. Thus, need to first sort/manipulate as reqd
# and then print. Default mode of opening a file is read mode
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f"hello, {name}")
    
print("\n")

# If reverse sort is needed i.e., wants the file to be in reverse
# For more info, see docs
for name in sorted(names, reverse = True):
    print(f"hello, {name}")
    
    """
    # Now, there is no need of lists to store file contents first
    # A simpler way to do the same above sorting is to do this:
    for line in sorted(file):
        print("hello,", line.rstrip())
    """