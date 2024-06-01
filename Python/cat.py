"""i = 0
while i < 3:
    print("meow")
    #i = i + 1
    i += 1
    # i++/i-- doesn't work in python
"""

# For loop allows you to iterate over a list of items
# i is automatically initialised to 0 and accordingly updated
# i from the list
#for i in [0, 1, 2]:
#    print("meow")
    
# Improvised version of the above for loop is
# by dflt, init. to 0 and goes upto the arg specified in the range fn and 
# not through it
#for i in range(3):
#    print("meow")
    
# A pythonic version of the same loop when the looping varr 
# ain't used anywhere else and we don't care about its name as it won't 
# change the correctness of the code
# We can do smthng like this
#for _ in range(3):
#    print("meow")
    
# Or even a more pythonic version as
#print("meow\n" * 3, end = "")

#print("\n\n")

# Common paradigm in python till the user gives some cared about value
#while True:
#    n = int(input("What's n? "))
"""if n < 0:
        continue
    else:
        break"""
#    if n > 0:
#        break
    
#for _ in range(n):
#    print("meow")
    
# Now, doing all the above using function
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("Wht's n? "))
        if n > 0:
            # return n
            break
    return n
    
def meow(n):
    for _ in range(n):
        print("meow")
        
main()