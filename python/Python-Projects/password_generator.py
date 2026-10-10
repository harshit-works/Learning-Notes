length = int(input("Enter the length of the password"))

letter = "abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQURSTWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*"
# print(letter)
# print(numbers)
# print(letter)
import random

all = letter + numbers + symbols
password = ""
for i in range(length):
    password = password + random.choice(all)

print("password generated",password)
