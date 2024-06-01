"""
# global variable
# global var are local to the module
# Reading a globa lvar is possible. However, writing(changing its
# value) in the same way ain't possible.
balance = 0

def main():
    # Won't work as balance is local to main() now.
    #balance = 0
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)
    
def deposit(n):
    # global is soln to writing
    global balance
    # Writing
    balance += n
    
def withdraw(n):
    # global is the soln to writing the var
    global balance
    balance -= n
    
if __name__ == "__main__":
    main()
"""

# Better way for this prblm(kinda to encapsulate)
# classes use is good since account is a real world entity
class Account:
    def __init__(self):
        # _smthing is just to indacate that its private but not 
        # enforced by python
        self._balance = 0
        
    # A property, in some sense, an instance var that's somehow 
    # protected(gives more ctrl over read & write of them)
    # This is a getter
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
        
    def withdraw(self, n):
        self._balance -= n
        
def main():
    account = Account()
    # Here, accessing the property, balance for printing it
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)
    
if __name__ == "__main__":
    main()