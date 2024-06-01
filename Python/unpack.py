#def total(galleons, sickles, knuts):
#    return (galleons * 17 + sickles) * 29 + knuts

#coins = [100, 50, 25]
#coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# *coins does the explosion/unpacking thing i.e., it unpacks all
# the values in the coins list and assign them to the fn's parameters
# respectively as needed.
# * operator here takes a data structure and unpacks it individually.

# Unpacking a list
#print(total(*coins), "Knuts")
 
#print(total(galleons=100, sickles=50, knuts=25), "Knuts")
#print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

# Unpacking a dictionary(passes in both keys and values separated
# conceptually with = sign, like the named param passing total fn above)
#print(total(**coins), "Knuts")


# *args and **kwargs
# fn takes varible no of positional args/param(only values) & 
# named/keyword args/param(both names/keys and their resp values).
def f(*args, **kwargs):
    print("Psitional:", args)
    print("Named:", kwargs)
    
# kwargs is automatically a dictionary.
f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)