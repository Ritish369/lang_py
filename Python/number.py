# Indentations show that what's associated with what i.e., similar to 
# curly braces in other languages

# Caller func
def main():
    # The process of getting an integer from user is abstracted away
    # by using get_int() func which is user defined
    x = get_int("What's x? ")
    print(f"x is {x}")

# Callee func
def get_int(prompt):
    # All the blocks are mutually exclusive
    while True:
        # Trying those things in this block which can actually fail/ give exception/error
        try:
            #x = int(input("What's x? "))
            # use f string to plug in some value for the variable
            #print(f"x is {x}")
            #break
            # Makes the code much shorter
            #return x
            
            # or because not using the var anywhere else, can do this as well
            #return int(input("What's x? "))
            return int(input(prompt))
            
        # tHESE are the exceptions that may occur because of the above maybe 
        # erroneous lines of code
        # Handling of the exceptions i.e., catching of the errors
        except ValueError:
            #print("x is not an integer")
            
            # Or if you want to catch the exception but don't wanna do
            # something with it i.e., simply ignore it after calling, do this
            pass

        # this clause is associated with the try block not the except
        #else:
            #break
            #return x
    #return x

#print(f"x is {x}")

main()

# A raise keyword is used to raise exceptions yourself..........