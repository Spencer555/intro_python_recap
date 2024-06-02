first, _ = input("What's your name? ").split(" ")
# we use underscore if we do not intend to use the other split value

print(f"hello, {first}")


coins = [100, 50, 25]

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * + knuts 


dict_coins = {"galleons":100, "sickles":50, "knuts":25}

print(total(100, 50, 25))


# *coins to unpack list
# to unpack dictionary **coins
# results galleons=100, sickles=50, knuts=25
print(total(**dict_coins), "knuts")

print(total(*coins), "knuts")


def f(*args, **kwags):
    print("Positional:", args)
    
    
    
    
f(1000, 2000, 3000)