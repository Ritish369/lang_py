def main():
    #yell("This is CS50")
    #yell(["This", "is", "CS50"])
    yell("This", "is", "CS50")
    
#def yell(phrase):
#def yell(words):
# *words in place of *args, to make the fn variatic in sense of taking
# inputs
def yell(*words):
    #print(phrase.upper())
    
    #uppercased = []
    #for word in words:
    #    uppercased.append(word.upper())
    
    # Using the map fn which is an instance of funcal progg.
    # This is an instance as a fn is being passed by reference
    # and map iterates the fn on each of those words & returns a
    # new list containing the reqd doings of the fn passed.
    ##uppercased = map(str.upper, words)
    
    # Using list comprehension here
    uppercased = [word.upper() for word in words]
    # Using unpacking of a list here
    print(*uppercased)
    
if __name__ == "__main__":
    main()