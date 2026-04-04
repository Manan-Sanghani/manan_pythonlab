# 1:->

try:
    number1=int(input("Enter a number : "))
    number2=int(input("Enter another number : "))
    result=number1/number2
except ZeroDivisionError:
    print("You cannot divide by zero!")     
except ValueError:
    print("Please enter a valid number!")     
else:
    print("Division successfil result is : ",result)
finally:
    print("This block always runs.")
    
    
# 2:->

try:
    my_list=[1,2,3]
    print(my_list) #this index does not exist
except IndexError:
    print("index is out of range !")
else:
    print("Element found successfully!")
finally:
    print("program finished.")