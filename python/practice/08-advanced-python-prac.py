#LIST COMPREHENSION

numbers = [i for i in range(1,11)]

print(numbers)

even = [i for i in range(1,21) if i % 2 == 0]

print(even)

#args *
def add(*numbers):

    print("Sum =", sum(numbers))

add(10,20,30,40)

#kwargs **
def employee(**details):

    for key,value in details.items():

        print(key,":",value)

employee(name="Harshit",
         role="Cybersecurity Student",
         country="India")
