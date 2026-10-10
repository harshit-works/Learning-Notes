# Functions & Modules

Functions are reusable blocks of code that perform a specific task.

They help make programs:
- Organized
- Reusable
- Easier to understand
- Easier to debug

---

# Creating a Function

Use the `def` keyword to create a function.

Example

```python
def greet():
    print("Hello!")
```

Calling the function

```python
greet()
```

---

# Function with Parameters

Parameters allow functions to receive data.

Example

```python
def greet(name):
    print("Hello", name)

greet("Harshit")
```

---

# Function with Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

# Default Parameters

A default value is used if no argument is provided.

Example

```python
def country(name="India"):
    print(name)

country()
country("Japan")
```

---

# Keyword Arguments

Arguments can be passed using parameter names.

Example

```python
def student(name, age):
    print(name, age)

student(age=20, name="Harshit")
```

---

# Return Statement

The `return` statement sends a value back to the caller.

Example

```python
def square(num):
    return num * num

result = square(5)

print(result)
```

---

# print() vs return

| print() | return |
|----------|---------|
| Displays output | Sends value back |
| Cannot reuse output | Output can be stored and reused |

---

# Variable Scope

## Local Variable

Accessible only inside the function.

Example

```python
def demo():
    x = 10
    print(x)

demo()
```

---

## Global Variable

Accessible throughout the program.

Example

```python
x = 100

def demo():
    print(x)

demo()
```

---

# Recursion

A function calling itself is called recursion.

Every recursive function must have a base case.

Example

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n-1)

countdown(5)
```

---

# Lambda Function

A lambda function is a small anonymous function.

Syntax

```python
lambda arguments : expression
```

Example

```python
square = lambda x: x*x

print(square(5))
```

---

# Modules

A module is a Python file containing functions and variables that can be imported into another program.

Example

```python
import math
```

---

# Importing Specific Functions

```python
from math import sqrt
```

---

# Math Module

Common Functions

```python
math.sqrt()

math.pow()

math.ceil()

math.floor()

math.factorial()
```

Example

```python
import math

print(math.sqrt(25))
```

---

# Random Module

Used to generate random values.

Example

```python
import random

print(random.randint(1,10))
```

Common Functions

```python
random.randint()

random.choice()

random.shuffle()
```

---

# Datetime Module

Used to work with date and time.

Example

```python
from datetime import datetime

print(datetime.now())
```

---
