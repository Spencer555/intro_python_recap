
# generator it used for large code and generate a peice at a time
def main():
        
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


    
# instead of this we use this
# def sheep(n):
#     for i in range(n):
#         return "</|\>" * i

        
# with this it generates one at a time so the program is not hanging
def sheep(n):
    for i in range(n):
        yield "</|\>" * i
        
if __name__ == "__main__":
    main()