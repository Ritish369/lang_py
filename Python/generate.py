# Library for doing things randomly. Need to import first to use its fns
# Imports everything here
import random

# To avoid repeatetive association of the fns with resp lib/module,
# use from
# Loads the fn name choice into my current namespace or scope of file 
# currently working in
#from random import choice

# Does randomness as it chooses randomly from the list given as an arg
coin = random.choice(["heads", "tails"])
# The other way
#coin = choice(["heads", "tails"])
print(coin)

# Random choosing between the specified range inclusive
number = random.randint(1, 10)
print(number)

# Shuffling of a list
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)