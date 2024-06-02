# map
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)#using map to uppercase each word
    
    # list comprehension [result function]
    uppercased2 = [word.upper() for word in words]   
    print(*uppercased) #upacking
    print(*uppercased2) #upacking
    
    
    




if __name__ == "__main__":
    main()