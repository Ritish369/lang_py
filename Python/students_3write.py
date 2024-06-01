# Writing a CSV file

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students-3.csv", "a", newline = '') as file:
    #writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})