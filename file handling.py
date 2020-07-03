import os
print("To open a file stored in python folder:")
# with open() function
file = open("data.txt")
print(file.read())
print("\n")
# open () function with r anf t method
file = open ("data.txt", "rt")
print("Open a file which is stored outside from python folder: ")
file = open("C:/Users/bahet/Desktop/data.txt", "r")
print(file.read())
print("\n")

# To read the contents of file by characters
file = open("C:/Users/bahet/Desktop/data.txt", "r")
print(file.read(19))

print("\n")

# To read a line in a file with readline() function

file = open("C:/Users/bahet/Desktop/data.txt", "r")
print("Read one line of a file: ")
print(file.readline())
print("\n")

# to read whole file line by line
print("Read a lines in a file with for loop: ")
file = open("C:/Users/bahet/Desktop/data.txt", "r")
for line in file:
    print(line)

# To close file with close() function
file = open("C:/Users/bahet/Desktop/data.txt", "r")
print("To close a file: ")
print(file.readline())
file.close()

#Write() function
print("Write the data in file with a attribute:")
file = open("data.txt", "a")
file.write("Data science is a growing field. A career as a data scientist is ranked at the third best job in America for 2020 by Glassdoor, and was ranked the number one best job from 2016-2019")
file.close()
file= open("Data.txt", "r")
print(file.read())

print("\n")
print("Write the data in file with w attribute:")
file = open("data.txt", "w")
file.write("Data science is a growing field. A career as a data scientist is ranked at the third best job in America for 2020 by Glassdoor, and was ranked the number one best job from 2016-2019")
file.close()
file= open("Data.txt", "r")
print(file.read())

#To Create a New File
file1 = open("datafield.txt", "x")
file1 = open("datafield.txt", "w")
file1.write("There are a variety of different technologies and techniques that are used for data science which depend on the application. More recently, full-featured, end-to-end platforms have been developed and heavily used for data science and machine learning.")
file1 = open("datafield.txt", "r")
print(file1.read())

#To remove File

if os.path.exists("datafield.txt"):
    os.remove("datafield.txt")
    print("File removed")
else:
    print("File not existed.")
