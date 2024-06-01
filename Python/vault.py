# Operator Overloading
class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    # Needed because we want to print the object direclty.
    #Thus, need to define the way we want it to be printed
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    # One of the special methods in py alongwith __init__ and __str__
    # Needed for overloading the + operator to add 2 vaults
    # self is left operand and other is right operand of + operator
    def __add__(self, other):
        # Defining/telling the py interpreter on how to add 2 vaults/
        # objects of any class.
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
       
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

"""
galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts
"""

# + operator is being overloaded here to add two vaults
# Automatically, calls the __add__ method. Also implies that
# the other can be of any type
total = potter + weasley
#total = Vault(galleons, sickles, knuts)
print(total)