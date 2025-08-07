#This is a practice of the file open functions
import os

# 1. Open the file with the key open, then assign to a var that can be read, otherwise will be an object
f = open("demofile")   # -> same to open("demofile", "rt")
print(f.read())

# 2. file handling
'''
"r" - Read, default value, open a file for reading, error if the file doesn't exist
"a" - append, open a file for appending, creates the file if it doesn't exist
"w" - write, open a file for writing, creates the file if it doesn't exist
"x" - create, create the specified file , return an error if the file exist
'''

# 3. Different location
# f = open("C:\\Users\skyh\Desktop\car.jpg")

# 4. with keyword, which will close the file
with open("demofile") as f:
    print(f.read())

# 5. close files
f = open("demofile")
print(f.read())
f.close()

# 6. Read only parts of the file
f= open("demofile")
print(f.read(5))
f.close()

f = open("demofile")
print(f.readline())
print(f.readline())
f.close()

# 7. Python file write
f = open("demofile", "a")
f.write(f"Hi this is sky{1}")


f = open("demofile")
print(f.read())

# 8. Python file replace
f = open("demofile","w")
f.write(f"st i delete something important")

f = open("demofile")
print(f.read())

# # 9. Create a new file
# f = open("demofile2.txt","x")

# 10. Delete a file
# import os
# os.remove("demofile2.txt")

# 11. Check if file exist
if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
else:
    print("file does not exist")