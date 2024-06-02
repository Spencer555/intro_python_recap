
# operator overloading using opertor to do more than its defualt e.g adding 2 objects etc

class Vault:
    
    def __init__(self,  galleons=0, sickles=0, knuts=0):
        
        self.galleons = galleons 
        self.sickles = sickles
        self.knuts = knuts
        
        
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.sickles + other.knuts
        return Vault(galleons, sickles, knuts)
        
        
    def __str__(self):
        return f"Galleons: {self.galleons}, Sickles: {self.sickles}, Knuts: {self.knuts}"
        
        
potter = Vault(100, 50, 25)
weasly = Vault(25, 100, 50)
    
    
print(potter)
print(weasly)
# using operator overloading the + feature
print(weasly + potter)