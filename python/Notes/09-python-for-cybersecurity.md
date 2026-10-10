# Python for Cybersecurity

Python is one of the most widely used programming languages in Cybersecurity.

It is used for:

- Automation
- Network Scanning
- Web Requests
- Password Generation
- Log Analysis
- Hashing
- File Management

---

# OS Module

The os module interacts with the operating system.

Example

```python
import os

print(os.getcwd())
```

Common Functions

```python
os.getcwd()

os.chdir()

os.listdir()

os.mkdir()

os.rename()

os.remove()
```

---

# pathlib

A modern way to work with files and folders.

Example

```python
from pathlib import Path

path = Path("sample.txt")

print(path.exists())
```

---

# hashlib

Used to generate hashes.

Example

```python
import hashlib

text = "hello"

hash_value = hashlib.sha256(text.encode())

print(hash_value.hexdigest())
```

Common Hashes

- MD5
- SHA1
- SHA256

---

# socket

Used for network communication.

Example

```python
import socket

print(socket.gethostname())
```

Useful For

- Port Scanner
- Banner Grabbing
- Network Tools

---

# requests

Used to send HTTP requests.

Example

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

---

# subprocess

Runs system commands.

Example

```python
import subprocess

subprocess.run(["ipconfig"])
```

---

# json

Used to store and exchange structured data.

Example

```python
import json

person = {
    "name":"Harshit",
    "role":"Cyber Student"
}

print(json.dumps(person, indent=4))
```

---

# base64

Encodes and decodes data.

Example

```python
import base64

text = "hello"

encoded = base64.b64encode(text.encode())

print(encoded)
```

---

# argparse

Used to accept command-line arguments.

Example

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name")

args = parser.parse_args()
```

---

# threading

Runs multiple tasks at the same time.

Useful for

- Faster Port Scanner
- Faster Network Scanner

---

# time

Useful for delays and measuring execution time.

Example

```python
import time

time.sleep(2)
```

---

# Summary

After this module you should know how to use Python to build basic cybersecurity tools.