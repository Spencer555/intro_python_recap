
students = [
    {"name":"Hermione", "house":"Gryffindor"},
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"},
    {"name":"Padma", "house":"Ravenclaw"},
]

# filter out only gryffindor students 


gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]


for gryffindor in sorted(gryffindors):
    print(gryffindor)
    
    
    
def is_gryffindor(s):
    return s["house"] == "Gryffindor"
       
       
# filter (a function that returns true or false, list)
# lambda variable: functionlogic 
gryffindors1 = filter(is_gryffindor, students)


for gryf in gryffindors1:
    print(gryf["name"])
    
    
    

# dictionary comprehension
studs = ["hermoine", "harry", "ron"]

gryffindors2 = []

# dictionary comprehension
gryffindors3 = [{"name":stud, "house":"Gryffindor"} for stud in studs]

print(gryffindors3, 'dictionary comprehension')


for stud in studs:
    gryffindors2.append({"name":stud, "house":"Gryffindor"})
    
    
print('dictionary comprehension: ', gryffindors2)

2:28