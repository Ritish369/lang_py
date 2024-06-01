name = input("What's your name? ")

# To reduce the more elif statements
#if name == "Harry" or name == "Hermione" or name == "Ron":
 #   print("Gryffindor")
 
#elif name == "Hermione":
 #   print("Gryffindor")
#elif name == "Ron":
 #   print("Gryffindor")

#elif name == "Draco":
 #   print("Slytherin")
#else:
 #   print("Who?")
 
# Better to use match keyword which is similar to switch case statement
# in other languaGES
match name:
    # To reduce the case statements as above for the same outputs
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
        
#    case "Hermione":
#        print("Gryffindor")
#    case "Ron":
#        print("Gryffindor")
    
    case "Draco":
        print("Slytherin")
    # handles any other cases not handled above
    case _:
        print("Who?")