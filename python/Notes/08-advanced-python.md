# Advanced Python (Cybersecurity Edition)

This module covers only the advanced Python topics that are useful in Cybersecurity.



# List Comprehension

List comprehension is a short way to create lists.

Normal Method

```python
numbers = []

for i in range(1,6):
    numbers.append(i)
```

Using List Comprehension

```python
numbers = [i for i in range(1,6)]

print(numbers)
```

Output

```
[1,2,3,4,5]
```



# List Comprehension with Condition

```python
even = [i for i in range(1,11) if i % 2 == 0]

print(even)


Output

```
[2,4,6,8,10]
```

Useful in Cybersecurity

- Filtering open ports
- Filtering IP addresses
- Filtering log entries

---

# Dictionary Comprehension

Creates dictionaries in one line.

Example

```python
square = {i:i*i for i in range(1,6)}

print(square)
```

Useful for

- Storing IP addresses
- Storing usernames
- Storing scan results

---

# *args

Accepts multiple positional arguments.

Example

```python
def add(*numbers):

    print(sum(numbers))

add(10,20,30)
```


# **kwargs

Accepts multiple keyword arguments.

Example

```python
def employee(**details):

    print(details)

employee(name="Harshit",role="Analyst")
```



# Regular Expressions (re)

Regular Expressions are used to search text.

Very important in Cybersecurity.

Example

```python
import re

text = "User logged in"

print(re.search("User",text))
```

Common Functions


search()

findall()

sub()
```

Used for

- Finding IP addresses
- Email extraction
- Password validation
- Log Analysis



# pip

Python Package Manager

Install package

```bash
pip install requests
```

See installed packages

```bash
pip list
```

Upgrade package

```bash
pip install --upgrade requests



# Virtual Environment

Virtual Environment creates an isolated Python environment.

Create

```bash
python -m venv myenv
```

Activate (Windows)

```bash
myenv\Scripts\activate
```

Deactivate

bash
deactivate


Why use it?

- Different projects can use different package versions.
- Prevents package conflicts.

