def hello():
    print("hello")
    
# Main function having everything
# Defined func
def main():
    name = input("What's your name? ")
    #hello(name)
    
    print(hello(name))
    
# Default argument of world to the parameter to
# defined func
def hello(to = "world"):
    #print("hello,", to)
    
    # To import this file into test_hello.py and make the program more
    # testable as pytest works good with fn args and their returns only majorly.
    return f"hello, {to}"
    
# Calling main here to execute
if __name__ == "__main__":
    main()