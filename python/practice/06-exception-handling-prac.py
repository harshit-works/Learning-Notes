#try except

try:
    n = int(input("Enter a number: "))
    print(100/n)
except:
    print("Someting is wrong")

#SPECIFIC ERROR
    
try:
    n = int(input("Enter a number: "))
    print(100/n)
except ValueError:
    print("plase enter only numbers")
except ZeroDivisionError:
    print("zero not allowed")

#else statment

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Invalid Age")

else:
    print("Age Accepted")

#finally
try:
    print("Opening Program")

finally:
    print("Closing Program") #always print the program


### MINI TASKS ###
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Answer:", result)

except ZeroDivisionError:
    print("You cannot divide by zero.")