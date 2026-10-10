# Exception Handling

An exception is an error that occurs while a program is running.

Without exception handling, the program stops immediately when an error occurs.

Example

```python
print(10/0)
```

Output

```
ZeroDivisionError
```

---

# Why Exception Handling?

It prevents the program from crashing.

Benefits:

- Handles unexpected errors
- Improves user experience
- Makes programs more reliable

---

# try and except

The try block contains code that may produce an error.

The except block handles the error.

Example

```python
try:
    num = 10 / 0

except:
    print("An error occurred.")
```

---

# Handling Specific Exceptions

Example

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Please enter only numbers.")
```

---

# Multiple Exceptions

Example

```python
try:
    num = int(input())

    result = 10 / num

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# else Block

The else block executes only if no exception occurs.

Example

```python
try:
    num = int(input())

except ValueError:
    print("Invalid Input")

else:
    print("Correct Input")
```

---

# finally Block

finally always executes.

Used for cleanup operations.

Example

```python
try:
    print("Program Started")

finally:
    print("Program Ended")
```

---

# Raising Exceptions

The raise keyword creates your own exception.

Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

# Common Exceptions

- ValueError
- ZeroDivisionError
- TypeError
- NameError
- IndexError
- KeyError
- FileNotFoundError

---

# Summary

After completing this module you should be able to:

- Handle runtime errors
- Use try-except
- Use else and finally
- Raise your own exceptions