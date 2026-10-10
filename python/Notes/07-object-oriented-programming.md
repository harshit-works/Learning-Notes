# Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using objects and classes.

It helps in:

- Organizing code
- Reusing code
- Building large applications
- Easier maintenance

---

# Class

A class is a blueprint for creating objects.

Example

```python
class Student:
    pass
```

---

# Object

An object is an instance of a class.

Example

```python
class Student:
    pass

student1 = Student()
student2 = Student()
```

---

# Constructor (__init__)

The constructor is automatically called when an object is created.

Example

```python
class Student:

    def __init__(self):
        print("Object Created")

student = Student()
```

---

# self Keyword

The self keyword refers to the current object.

Example

```python
class Student:

    def __init__(self, name):
        self.name = name

student = Student("Harshit")

print(student.name)
```

---

# Attributes

Attributes are variables inside a class.

Example

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

---

# Methods

Methods are functions inside a class.

Example

```python
class Student:

    def __init__(self, name):

        self.name = name

    def display(self):

        print(self.name)

student = Student("Harshit")

student.display()
```

---

# Encapsulation

Encapsulation means keeping data and methods together inside a class.

Example

```python
class Bank:

    def __init__(self, balance):

        self.balance = balance
```

---

# Inheritance

Inheritance allows one class to use the properties and methods of another class.

Example

```python
class Animal:

    def sound(self):

        print("Animal Sound")

class Dog(Animal):

    def bark(self):

        print("Bark")
```

---

# Method Overriding

A child class can replace a parent's method.

Example

```python
class Animal:

    def sound(self):

        print("Animal")

class Dog(Animal):

    def sound(self):

        print("Bark")
```

---

# Polymorphism

Polymorphism allows the same method name to behave differently.

Example

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

