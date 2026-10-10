import math 
import random
from datetime import datetime

#Funtions
def greet():
    print ("Hello ji Good Morning")

greet()

#Functions with Multiple parmeter
def add(a,b):
    print(a+b)

add(5,2)

#Default parameter
def country(name="India"):
    print(name)

country()
country("japann")

#keywprd Arguments 
def student(name,age):
    print("Name",name)
    print("Age",age)

student(age=20,name="Hars")

#Return
def square(num):
    return num*num

result = square(6)
print("Square",result)

# Local Variable
def demo():
    x = 50
    print("Local:", x)

demo()

# Global Variable
x = 100
def show():
    print("Global:", x)

show()

#Recursion 
def countdown(n):
    if n == 0:
        return
    print(n)

    countdown(n-1)

countdown(10)

# Random Module
print(random.randint(1,100))

colors = ["Red","Blue","Green"]

print(random.choice(colors))

### MINI TASK ###
# Create a function that prints your name.
def name():
    a = (input("Enter your name"))
    print(a)

name()

# Create a function that takes two numbers
# and returns their sum.
def sum():
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    print(a+b)

sum()

# Create a function that returns the cube
# of a number.
def cube(a):
    print(a*a*a)

cube(4)

# Create a function to check whether a
# number is Even or Odd.
def evenodd():
    z = int(input("Enter the number"))
    if z % 2 == 0:
        print("even number")
    else:
        print("odd number")

evenodd()

# Create a function that finds the
# largest of three numbers.
def largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c

result = largest(10, 25, 18)

print(result)
