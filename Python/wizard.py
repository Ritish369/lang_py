class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

# Student is a sub-class/inherits from the Wizard class
class Student(Wizard):
    def __init__(self, name, house):
        # This is a reference to the super class of this class
        # Accessing the method of that class with super now
        super().__init__(name)
        self.house = house
        
# Prof inheriting from the wizard class
class Professor(Wizard):
    def __init__(self, name, subject):
        # Referencing to super class of this class
        # Accessing the method of that class with super now
        super().__init__(name)
        self.subject = subject
     
   
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the Dark Arts")