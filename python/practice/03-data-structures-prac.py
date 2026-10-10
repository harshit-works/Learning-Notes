# #Data structures 
# #string
# name = "Python Thakur"
# print(name[1])
# print(name[1:6])
# print(name[-6])
# print(name[6:])
# print(name.upper())
# print(name.lower())
# print(name.replace("Python","Harshit"))

# #Lists
# number = [1,2,35,5,6,322]
# print(number[0:2])
# number.append(50)
# print(number)
# number.remove(2)
# print(number)
# number.pop()
# print(number)
# number.sort()
# print(number)
# number.reverse()
# print(number)

# #Tuples
# tuple1 = ("harry","Laxman",30)
# print(tuple1)
# print(tuple1[2])
# print(tuple1.count(30))
# print(tuple1.index(30))

# #SetS
# A = {5,2,6,7}
# B = {4,55,2,41}

# print(A.union(B))
# print(A.intersection(B))
# print(A.difference(B))
# A.add(10)
# A.remove(2)

# #Dictionaries
# student = {
#     "name":"Harshit",
#     "age":20,
#     "course":"BCA"
# }
# print(student)
# print(student["name"])
# student["city"] = "Bhopal"
# print (student)
# student.pop("course")
# print(student)
# print(student.keys())


# ###  MINI Tasks  ###
# # Take a string from the user and print it in uppercase.
# A = input("Enter yout name")
# print (A.upper())

# # Reverse a string.
# B = "Harshir is a good bot"
# print(B[::-1])

# Count the number of vowels in a string.
C = "my name is Harshit thakur"
v = 0 
for letter in C:
    if letter in('a','e','i','o','u'):
        v += 1

print(v)

# Create a list of 5 numbers and print the largest and smallest number.
L = [1,2,3,4,5]
print("Largest Number",max(L))
print("Largest Number",min(L))

# Take 5 numbers from the user and store them in a list.
E = []
for i in range(5):
    T = int(input("Enter a number: "))
    E.append(T)

print(E)

    


