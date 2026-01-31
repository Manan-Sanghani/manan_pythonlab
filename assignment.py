# 1. print a message

print("Hello, Welcome to Python!") 


# 2. Add to numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b) 


# 3. Even or Odd


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd") 


# 4. Check leap year

year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year") 


# 5. print PI value

import math
print("Value of PI =", math.pi) 


# 6. Store and print constant value

PI = 3.14159
print("Constant value of PI:", PI) 


# 7. Square of a number

num = int(input("Enter a number: "))
print("Square =", num * num) 


# 8. Area of a circle

radius = float(input("Enter radius: "))
area = 3.14159 * radius * radius
print("Area of Circle =", area) 


# 9. Check data type

value = input("Enter something: ")
print(type(value)) 


# 10. Use math functions

import math

num = int(input("Enter a number: "))
print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(num)) 


# 11. Find power

base = int(input("Enter base: "))
power = int(input("Enter power: "))
print("Result =", base ** power) 


# 12. Check Positive or Negative

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero") 



