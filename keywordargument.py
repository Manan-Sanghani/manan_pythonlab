# 1.basic keyword argument

def student_info(name,age,city):
    print("Name :",name)
    print("Age :",age)
    print("City :",city)
    
student_info(age=18,city="Rajkot",name="Ravi")


# 2.mixing positional and keyword

def display(a,b,c):
    print("a= ",a)
    print("b= ",b)
    print("c= ",c)
    
display(1,c=3,b=2)
