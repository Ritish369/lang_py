students = ["Hermione", "Harry", "Ron", "Draco"]
"""
print(students[0])
print(students[1])
print(students[2])"""

for student in students:
    print(student)
    
# range fn cannot take a list as its arg
for i in range(len(students)):
    print(i + 1, students[i])
    
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# Using Dictionaries{"key":"value"}
students = {"Hermione":"Gryffindor", "Harry":"Gryffindor",
            "Ron":"Gryffindor", "Draco":"Slytherin"}

"""
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])"""

# prints both keys and values
for student in students:
    print(student, students[student], sep = ", ")

print("\n")
    
# List of dictionaries
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")