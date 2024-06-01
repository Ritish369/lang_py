# Constant(CAPITALAIZE the var to indicate it as constant but this 
# ain't enforced by python)
"""MEOWS = 3

for _ in range(MEOWS):
    print("meow")"""
    
    
## """.......""" is the docstrings format for comments.
    
    
# Using constants in classes
"""
class Cat:
    # Convention of class constants
    MEOWS = 3
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
            
cat = Cat()
cat.meow()
"""

# Not enforced but convention.
# type hints(: int is a type hint here to tell the inter. for the
# type of n)
# : int is kind of some annotation for the var/arg.
# Whenever one need to hint the return type of a fn, then its done
# using an arrow followed by the type to be returned.(type hint this is also)
#def meow(n: int) -> None:
def meow(n: int) -> str:
#def meow(n):
    # Docstring format having a std format of fn things to get
    # the documentation and get it analyzed by 3rd party tools
    """
    Meow n times.
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """

    #for _ in range(n):
        #print("meow")
    
    # Good follow up practice of returning things from unit tests
    # overloaded * operator(concatenates/joins n meows all together)
    return "meow\n" * n
        
# use of type hint here & int() is a fn call as always
#number: int = input("Number: ")
number: int = int(input("Number: "))
#meow(number)
meows: str = meow(number)
print(meows, end = "")   