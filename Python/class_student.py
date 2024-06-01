# Conventionally, class names start with capitals.
# User-defined data type
# Encapsulation
# Instance variables and fns/methods can't have the same name.
class Student:
    # Instance method(Initializes the contents of an obj from a class)
    # Kinda seems to be similar to default/parametrized constructor in C++
    # Always called
    # self gives access to the current obj just created
    # Automatically called
    
    # Way to make things/args optional is:
    #def __init__(self, name, house = None):
    
    #def __init__(self, name, house, patronus):
    def __init__(self, name, house):
        # Instance var creation and storeing the args
        """
        if not name:
            # raise is used to raise exceptions when some errors are
            # encountered and signal them
            raise ValueError("Missing name")
        """        
        """
        if house not in ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid house")
        """
        self.name = name
        self.house = house
        #self.patronus = patronus
        
    # User friendly
    # ReturnS a human-readable string of the obj created.
    # Called by print() fn in python. Mainly used when an obj is to be 
    # used/printed as a string.(Kinda converts an obj to a string)
    # Automatically called
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    """
    # Conventionally, every method/fn-in-a-class will take at least one
    # prameter/arg which is the reference to the current obj and other addnals.
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"
    """
    
    """
    # Conventionally, any inst var like _smthng is kinda private
    # saying(by py) not to touch this otherwise things may mess up
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    # Decorator(decorator syntax for getters using properties)
    @property
    # Getter(fn for a class to get)
    # Always 1 arg
    def house(self):
        #return self.house
        
        # _house is now my instance variable and my property is house
        return self._house
    
    # Decorator(decorator syntax for setters using properties)
    # Clue is given to python from here
    @house.setter
    # Always has 2 args
    # Setter(fn for a class to set)
    # Called automatically by any house assigment/setting
    # that's been made/written or when the obj is made for 1st time
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]:
            raise ValueError("Invalid house")
        #self.house = house
        
        # Becuse instance var & fn had the same name, Thus, to differentiate
        #_house is now my instance variable and my property is house
        self._house = house
    """

def main():
    #student = get_student()
    
    # Because of use of class methods.
    student = Student.get()
    
    # Accesssing attributes here
    #print(f"{student.name} from {student.house}")
    #print("Expecto Patronum!")
    
    # Some adversarial change
    # Not too secure for the data of the user. Need defensive approach.
    #student.house = "Number Four, Privet Drive"
    print(student)
    
    #print(student.charm())
    
"""
def get_student():
    # 3 qoute comment
    # Object creation i.e., instantiation of a class
    student = Student()
    # Attributes assignment/storing
    student.name = input("Name: ")
    student.house = input("House: ") # 3 qoute comment
    
    #name = input("Name: ")
    #house = input("House: ")
    #patronus = input("Patronus: ")
    # Kinda doing standardization of the type of data to store
    # in/through the class & gives control over the correctness of data
    # Constructor Call i.e., instantiate a Student obj
    # Because parameters are passed in this constructor, contents of 
    # the obj can be customized
    # See about some __new__ method, similar working here of that fn
    #student = Student(name, house)
    # Returning that object
    #return student
    #return Student(name, house)
    #return Student(name, house, patronus)
"""

if __name__ == "__main__":
    main()