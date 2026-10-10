#Control Flow Practice
#Statment
#if statment
age = 20 
if age > 18:
    print("Eligible")

#if else statment
age = 20 
if age > 18:
    print("Eligible")
else:
    print("Not Eligible")

#elseif statment
marks = int(input("Enter your marks="))
if marks>90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("False")

#nested if
age = 20
citizen = True 
if age>20:
    if citizen:
        print("Eligible to vote")

#LOOPS
#for loop
for i in range(5):
    print(i)
#range
for i in range(2,11,2):
    print(i)
#while loop
count = 1 
while count <=5:
    print(count)
    count +=1
#break
for i in range(10):
    if i == 5:
        break 
    print (i)
#continue
for i in range(10):
    if i == 3:
        continue 
    print(i)


#MINI TASKS
# Take a number from the user.
# Print whether it is Positive, Negative or Zero.
a = int(input("Enter a number"))
if a>0:
    print("its a positive number")
elif a<0:
    print("its a negative number")
else:
    print("zero")

# Print numbers from 1 to 20 using a for loop.
for i in range(1,20):
    print(i)

#Print the multiplication table of any number entered by the user.
num = int(input("Enter a number"))
i = 1
while i<=10:
    print(num,"X",i,"=",num*i)
    i += 1

# Print all even numbers from 1 to 50.
for i in range(1,50):
    if(i%2==0):
        print(i)

# Find the sum of numbers from 1 to 100.
total = 0
for i in range(1,100):
    total = total + i
    print(total)