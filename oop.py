class Student:
    
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError('Missing Name')
        
        self._name = name 
        self._house = house #this also calls the setter
        self._patrouns = patronus
        
        
    def charm(self):
        match self.patrouns:
            case "Stag":
                return "fire"
            case "Otter":
                return "water"
            case "Bird":
                return "Air"
            case _:
                return "/"
        
     #getter  - get some attibute we name it @property
    @property
    def house(self):
        return self._house 
    
    #setter - set some attribute we name it @functioname.setter
    # one argument self for the getter 2 argument or more for the setter
    # a prefix with one _ means dont touch or alter it double __ means really dont touch it
    @house.setter
    def house(self, house):
        if self.house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        # since the main init contains self .house we cant have the same here so we add underscore
        self._house = house
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    def patronus(self):
        return self.patronus
    
    
    @classmethod
    # with this no student is instantiated
    def get_student(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        
        return (name, house, patronus)
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    
    
    
    
    

def main():
    # name, house = get_student()
    # print(f"{name} from {house}") 

    # student = get_student()
    student = Student.get_student()
    # print("Expecto Patronum!")
    # print(student.charm()) 
    # student.house = "Number Four, Privet Drive" 
    print(student)


# moved to a class method
# def get_student():
#     name = input("Name: ")
#     house = input('House: ')
#     patronus = input('Patronus: ')
#     return  Student(name, house, patronus)
        


if __name__ == "__main__":
    main()