# Module apecifically for handling CSV files
import csv

# Reading a CSV file
#with open("students.csv", "r") as file:
"""
with open("students-2.csv", "r") as file:
    for line in file:
        # split fn returns a list of all of the individual parts/strings
        # of the line separated by commas i.e., left and right of it
        
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")
        
        # or
        # Unpacking the contents into two diff vars
        #name, house = line.rstrip().split(",")
        name, home = line.rstrip().split(",")
        #print(f"{name} is in {house}")
        print(f"{name} is in {home}")
        """
        
#print("\n")

# Now, to get the contents in sort of arranged order i.e., sorted order
# We can do as this:
students = []
#with open("students.csv") as file:
"""
with open("students-2.csv") as file:
    for line in file:
        #name, house = line.rstrip().split(",")
        name, home = line.rstrip().split(",")
        #students.append(f"{name} is in {house}")
        
        # To make it shorter and doing all the below dict things at once, one
        # can do this:
        # Also a new non-empty dictionary
        #student = {"name": name, "house": house}
        student = {"name": name, "home": home}
        students.append(student)
"""

# Now, using the csv module functions, see how it gets easy.
with open("students-2.csv", "r") as file:
    # reader fn solves prblms for detecting the content i.e., sorta commas,
    # quotes and other characters
    
    #reader = csv.reader(file)
    
    # To treat the csv file more flexibly, we can use the DictReader fn
    # In dictreader, the first row is used as an inference for the type or
    # kind of data so that even if the file changes, the header tells in adv 
    # It or code breaks when we don't use headers or make assumptions for thr 
    # type of contents in csv
    reader = csv.DictReader(file)
    
    #for row in reader:
    #   students.append({"name": row[0], "home": row[1]})

    # OR
    
    #for name, home in reader:
    #    students.append({"name": name, "home": home})

    # AND for DictReader, we will do:
    for row in reader:
        #students.append({"name": row["name"], "home": row["home"]})
        students.append(row)

"""        
#for student in sorted(students):
#    print(student)
    
    # Empty dictionary

        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)
    """
    
# These two fns are used to sort the list of dicts acc to some key of the dict
"""def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]"""
    
# Sorting based on some key of the dictionary using the key keyword rather
# the named parameter and assigning it the determining func for dict
"""for student in sorted(students, key = get_name):
    # Single quotes to let the py interpreter to differentiate b/w double
    # and single quotes along with the contents they have
    #print(f"{student['name']} is in {student['house']}")
    print(f"{student['name']} is in {student['home']}")
    """

#print("\n")
    
# Because the above two getter fns are being used immediately as they are
# defined and not needed again any further, then we can use LAMBDA Fns to
# tighten the code
# lambdas are sort of anonymous fns i.e., without-any-name fns
for student in sorted(students, key = lambda student: student["name"]):
    #print(f"{student['name']} is in {student['house']}")
    print(f"{student['name']} is from {student['home']}")