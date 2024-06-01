import random

class Hat:
    #def __init__(self):
        # Keeping the list in obj itself as maybe used by many fns
        #self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    # Class Variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        
    @classmethod
    #def sort(self, name):
    
    # No more passing of obj reference here. Rather passing class
    # reference now using cls keyword for class.
    def sort(cls, name):
        #house = random.choice(self.houses)
        house = random.choice(cls.houses)
        print(name, "is in", house)
    
# Obj instantiation
#hat = Hat()
#hat.sort("Harry")

# Now, no need of obj creation. Direclty use the class and its 
# methods using the class name itself. All this bcause of classmethod.
Hat.sort("Harry")