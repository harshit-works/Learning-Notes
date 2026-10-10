#Classes and objects 
class Student:
    def __init__(self,name,age):
        self.name =name
        self.age = age 
    def display(self):
        print("name" ,self.name)
        print("age" ,self.age)

Student1 = Student("Harish",20)
Student1.display()

#Methods
class Calculator:
    def add(self,a,b):
        return a +b

calc = Calculator()
print(calc.add(10,20))

#Encapsulation
class Bank:
    def __init__(self,balance):
        self.balance = balance
    def show_balance(self):
        print("balance",self.balance)

acc1 = Bank(2000)
acc1.show_balance()

#Inhertance 
class animal():
    def sound(self):
        print("Animal sound")
class dog(animal):
    def bark(self):
        print("Barks")

D = dog()
dog.sound()
dog.bark()

#Method overridding
class Bird:
     def sound(self):
        print("Bird Sound")
class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")

bird = Sparrow()
bird.sound()

#polymor