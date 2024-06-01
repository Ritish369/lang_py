# Generators
def main():
    n = int(input("What's n? "))
    #for i in range(n):
        #print("🐏" * i)
    #    print(sheep(i))
    # Using loop to iterate over the iterator returned by yield 
    # of sheep func
    for s in sheep(n):
        print(s)

def sheep(n):
    #return "🐏" * n
    """
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock
    """
    # Using yield keyword for generators here
    for i in range(n):
        # returns an iterator or iterable in some sense
        yield "🐑" * i
     
if __name__ == "__main__":
    main()