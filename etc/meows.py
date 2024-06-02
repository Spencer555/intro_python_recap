# constants all caps is by convention a constant which means u should not touch it
MEOWS = 3


for _ in range(MEOWS):
    print("meow") 
    
    
    
class Cat:
    MEOWS = 3 # class constants
    
    """ this is a doc string of the function"""
    
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meows")
            
cat = Cat()