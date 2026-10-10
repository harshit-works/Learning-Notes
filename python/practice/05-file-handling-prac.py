import csv
#Writing to a file
file = open("sample.txt","w")
file.write("Hello Python")
file.close()

print("Data Written Successfully")

#Reading a file 
file = open("sample.txt","r")
print(file.read())
file.close
#Same we have readline command

#Append
file = open("sample.txt","w")
file.write("\nthis line is appended")
file.close()

print("Data appened")

#with open
with open("sample.txt","r")as file:
    print(file.read())

#csv file
with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Harshit", 95])
    writer.writerow(["Rahul", 90])

print("CSV File Created")

## mini tasks ##
# Copy the contents of one file top another
source = open("source.txt", "r")

data = source.read()

destination = open("destination.txt", "w")

destination.write(data) #copied!

source.close()
destination.close()

# Ask the user to enter
# five names and save them
# in names.txt.
file = open("names.txt", "w")

for i in range(5):
    name = input("Enter a name: ")
    file.write(name + "\n")

file.close()
