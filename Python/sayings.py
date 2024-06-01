# This will/is a custom library created by me for me and is imported
# in other files

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")
    
def goodbye(name):
    print(f"goodbye, {name}")
    
# __name__ is a var which is a special symbol in py whose value is 
# automatically set, by py, to be "main" when a file is run from the CLI
# and if this module is not imported in some another file
if __name__ == "__main__":
        main()