def main():
    # Also a tuple in unpacked way
    #name, house = get_student()
    
    # Tuple in abstracted way
    student = get_student()
    
    """
    # Won't work as tuples are immutable and here, we're changing the
    # second value of the tuple in if clause
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    """
    # Dicts are mutable and thus, chnages can be made to if clause as
    # follows which is to use the keys
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
     
     
    # For tuples and list   
    #print(f"{name} from {house}")
    #print(f"{student[0]} from {student[1]}")
    
    # For Dicts
    print(f"{student['name']} from {student['house']}")
    
    
def get_student():
    #This is returning a tuple of 2 values namely, name & house here
    #name = input("Name: ")
    #house = input("House: ")
    #return name, house
    #return (name, house)

    """
    #Using dictionary obj here thus, returning a dict here
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
    """
    # Alternate way for dict returning
    name = input("Nmae: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()