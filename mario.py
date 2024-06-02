# print("#")
# print("#")
# print("#")

def main():
    # print_column(3)
    # print_row(3)
    print_square(3)
    
    

# def print_column(height):
#     for _ in range(height):
#         print("#\n" *  height, end="")
        

# def print_row(width):
#     print("?" * width)
        
        
def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            print('#', end='')
        print()
        
        
# reduced to this
def print_square(size):
    for i in range(size):
        print('#' * size)
        
        
        
main()
              
              