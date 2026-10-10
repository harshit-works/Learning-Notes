# Control Flow

Control Flow determines the order in which a program executes statements.

It allows a program to make decisions and repeat tasks.

---

# Conditional Statements

Conditional statements execute code based on a condition.

## if

Executes a block only if the condition is True.

Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

## if...else

Executes one block if the condition is True, otherwise executes another block.

Example

```python
age = 15

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## if...elif...else

Used when there are multiple conditions.

Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

# Nested if

An if statement inside another if statement.

Example

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
```

---

# Loops

Loops repeat a block of code.

Python has two loops:

- for
- while

---

# for Loop

Used when the number of iterations is known.

Example

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

# range()

Creates a sequence of numbers.

Examples

```python
range(5)

range(2,6)

range(2,11,2)
```

Outputs

```
0 1 2 3 4

2 3 4 5

2 4 6 8 10
```

---

# while Loop

Repeats until the condition becomes False.

Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Loop Control Statements

## break

Stops the loop immediately.

Example

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## continue

Skips the current iteration.

Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## pass

Acts as a placeholder.

Example

```python
if True:
    pass
```

---

# Summary

After completing this module you should be able to:

- Make decisions using if statements
- Use nested conditions
- Repeat tasks using loops
- Control loops using break, continue and pass