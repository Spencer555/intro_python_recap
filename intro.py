# to format 1000 to 1,000


z = 1000 

print(f"{z:,}")

# to two decimal points
print(f"{z:.2f}")




# put ur main code at the top 
# this allows u to call function before u create them
def main():
    name = input("whats your name? ")
    hello(name)
    
    
  
  
def hello(to):
    print("hello,", to)  


main()
# section 2 


# match is the same as swich in javascript for testing multiple cases 


name = input("what's your name")

match name:
    case "Harry" | "Parry":
        print('harry boy')
        
    case "Hermione":
        print("this is h boy")
        
    case _:
        print("this is default my G")
        
        
# sequence is something that is list like 


