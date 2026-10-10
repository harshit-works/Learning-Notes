# Data Structures

Data Structures are used to store and organize data efficiently.

Python provides the following built-in data structures:

- Strings
- Lists
- Tuples
- Sets
- Dictionaries

---

# Strings

A string is a sequence of characters enclosed in single (' ') or double (" ") quotes.

Example

```python
name = "Harshit"
```

## Accessing Characters

```python
name = "Python"

print(name[0])
print(name[-1])
```

Output

```
P
n
```

---

## String Slicing

```python
name = "Python"

print(name[0:3])
print(name[2:])
print(name[:4])
```

---

## Common String Methods

```python
upper()

lower()

title()

capitalize()

strip()

replace()

find()

count()

split()

startswith()

endswith()
```

Example

```python
text = "hello world"

print(text.upper())
print(text.replace("world","Python"))
```

---

# Lists

Lists store multiple values and are mutable (can be changed).

Example

```python
numbers = [10,20,30,40]
```

## Accessing Elements

```python
print(numbers[0])
print(numbers[-1])
```

---

## List Slicing

```python
print(numbers[1:3])
```

---

## Common List Methods

```python
append()

insert()

extend()

remove()

pop()

clear()

sort()

reverse()

count()

index()
```

---

# Tuples

Tuples are ordered collections that cannot be modified after creation.

Example

```python
student = ("Harshit",20,"BCA")
```

## Tuple Methods

```python
count()

index()
```

---

# Lists vs Tuples

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| [] | () |
| More Methods | Fewer Methods |

---

# Sets

Sets store unique values.

Example

```python
numbers = {1,2,3,4}
```

Duplicate values are automatically removed.

---

## Set Methods

```python
add()

remove()

discard()

union()

intersection()

difference()
```

Example

```python
A = {1,2,3}
B = {3,4,5}

print(A.union(B))
print(A.intersection(B))
```

---

# Dictionaries

A dictionary stores data as key-value pairs.

Example

```python
student = {
    "name":"Harshit",
    "age":20,
    "course":"BCA"
}
```

---

## Accessing Values

```python
print(student["name"])
```

---

## Adding Data

```python
student["city"] = "Delhi"
```

---

## Updating Data

```python
student["age"] = 21
```

---

## Removing Data

```python
student.pop("course")
```

---

## Dictionary Methods

```python
keys()

values()

items()

get()

pop()

update()
```

---

# Summary

After completing this module you should be able to:

- Work with Strings
- Store data in Lists
- Use Tuples
- Perform Set operations
- Create and manage Dictionaries