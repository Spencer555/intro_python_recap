# inheritance 

class Wizard:
    def __init__(self, name):
        if not name:
            self.name = name 
            
            
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name) #to access parent class values from wizard
        self.house = house 
        
        
class Professor(Wizard): 
    def __init__(self, name, subject):
        super().__init__(name) #to access parent class values from wizard
        self.subject = subject
        
        
        
        
wizard = Wizard("Albus")     
student = Student('Harry', "luanga")
professor = Professor('Perry', "Figher of the dark arts")