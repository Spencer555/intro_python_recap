 
balance = 0

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)
    
    
def deposit(n):
    # telling it its global 
    global balance
    balance += int(n)



def withdraw(n):
    # telling it its global 
    global balance
    balance -= int(n)
    
    
    
if __name__=="__main__":
    main()
    
    
    
    