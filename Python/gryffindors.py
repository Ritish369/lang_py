"""
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# List comprehension with conditionals
# gryffindors = [
#     student["name"] for student in students
#     if student["house"] == "Gryffindor"
# ]


# More functional approach to this prblm
# Boolean return fn
#def is_gryffindor(s):
#    return s["house"] == "Gryffindor"

# Using filter func which is similar in spirit of map func
#gryffindors = filter(is_gryffindor, students)
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

# Sorting a list of dicts
# for gryffindor in gryffindors:
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    # print(gryffindor)
    print(gryffindor["name"])
"""

# Will be using Dictionary Comprehensions further here
students = ["Hermione", "Harry", "Ron"]

# Sorta list comprehension on list of dicts
#gryffindors = [{"name": student, "house": "Gryffindor"}
#               for student in students]

# Dictionary comprehension is here now
# dict = {key: value loop}
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
print("\n")

#for i in range(len(students)):
#    print(i + 1, students[i])

# Similar in working & outcome to the above for loop but just written
# tightly
for i, student in enumerate(students):
    print(i + 1, student)