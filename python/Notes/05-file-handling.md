# File Handling

File handling allows a program to store data permanently in files instead of keeping it only in memory.

It is commonly used for:
- Saving user data
- Reading configuration files
- Storing logs
- Generating reports

---

# Opening a File

Python uses the open() function.

Syntax

```python
file = open("filename.txt", "mode")
```

Example

```python
file = open("data.txt", "r")
```

---

# File Modes

| Mode | Description |
|------|-------------|
| r | Read a file |
| w | Write to a file (creates or overwrites) |
| a | Append data |
| x | Create a new file |
| r+ | Read and write |

---

# Reading Files

## read()

Reads the entire file.

Example

```python
file = open("data.txt","r")

print(file.read())

file.close()
```

---

## readline()

Reads one line at a time.

Example

```python
file = open("data.txt","r")

print(file.readline())

file.close()
```

---

## readlines()

Reads all lines and stores them in a list.

Example

```python
file = open("data.txt","r")

print(file.readlines())

file.close()
```

---

# Writing Files

Use write() with "w" mode.

Example

```python
file = open("data.txt","w")

file.write("Hello Python")

file.close()
```

---

# Appending Data

Append mode adds data without deleting existing content.

Example

```python
file = open("data.txt","a")

file.write("\nWelcome")

file.close()
```

---

# Closing Files

Always close the file after use.

```python
file.close()
```

---

# with Statement

The with statement automatically closes the file.

Recommended way.

Example

```python
with open("data.txt","r") as file:
    print(file.read())
```

---

# File Pointer

## tell()

Returns the current cursor position.

Example

```python
with open("data.txt","r") as file:
    print(file.tell())
```

---

## seek()

Moves the cursor.

Example

```python
with open("data.txt","r") as file:
    file.seek(0)
```

---

# CSV Files

CSV stands for Comma-Separated Values.

Used to store tabular data.

Example

```python
import csv

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name","Marks"])
```

---

