# Tell the unique houses in this list of dicts
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

"""
# One approach
# List to get all the unique houses
houses = [], list()
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])
        
for house in sorted(houses):
    print(house)
    """
    
# Second Approach
# set automatically eliminates the duplicates
houses = set()
for student in students:
    # add for a set
        houses.add(student["house"])
        
for house in sorted(houses):
    print(house)