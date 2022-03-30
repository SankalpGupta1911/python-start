# File IO - reading the content of a file

# 'open' it opens file and in this we didn't give any mode to open so it will open in default(read) mode
f = open("mayank.txt")
content = f.read()
print(content)
# 'close' it close our opened file. it is a good habit for programmer
f.close()

# we give any mode to open so it will open in that mode
#1
f = open("mayank.txt", "rb")
content = f.read()
print(content)
f.close()

#2
f = open("mayank.txt", "rt")
content = f.read()
print(content)
f.close()

# file read but limited characters
f = open("mayank.txt", "rt")
content = f.read(16)
print(content)
f.close()

# file read multiple but limited characters
f = open("mayank.txt", "rt")
content = f.read(16)
print("First 16 character : ", content)
content = f.read(10)
print("Read 10 character but after First 16 character : ", content)
f.close()

'''file read multiple in limited characters but if our first written limit 
count is more then file contains character count then our next read will return blank'''
f = open("mayank.txt", "rt")
content = f.read(70)
print("First 70 character : ", content)
content = f.read(10)
print("Read 10 character but after First 70 character : ", content)
f.close()


# file read and print character by character
f = open("mayank.txt", "rt")
content = f.read()
for line in content:
    print(line)
f.close()

# file read and print line by line
f = open("mayank.txt", "rt")
# content = f.read()
for line in f:
    print(line)
f.close()

# file read one line and print
f = open("mayank.txt", "rt")
content = f.readline()
print(content)
f.close()

# file read line by line and print
f = open("mayank.txt", "rt")
print(f.readline()) #this print first line
print(f.readline()) #this print second line
f.close()

# file read all lines and print
f = open("mayank.txt", "rt")
print(f.readlines()) #this print first line
f.close()
