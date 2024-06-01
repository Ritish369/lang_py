def main():
    x = int(input("What's x? "))
    #x = input("What's x? ")
    print("x squared is", square(x))
    
def square(n):
    return n * n
    # Exponetial (n raised to the power of 2)
    #return n ** 2
    # or, the func for the same is
    #return pow(n, 2)

if __name__ == "__main__":
    main()