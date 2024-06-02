import random 
# classes are used to rep real world entites or fantasy world entity 

# with harry porter there is only one hat for sorting so lets try to implement that
class Hat:
    # we dont meed init when we need only one of the class
    # def __init__(self):
    #     self.houses = ["Luanga", "kizito", "Faucauld", "Claver", "Agustine", "Poress"]
    
    # a class variable 
    houses = ["Luanga", "kizito", "Faucauld", "Claver", "Agustine", "Poress"]
    
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)
        
    
    

def main():
    
    # accessing class methods
    Hat.sort("harry")
    
    
    
if __name__ == "__main__":
    main()