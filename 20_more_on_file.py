# File handling seek(), tell()


'''it is for open file(mayank.txt in read mode). 'tell' will help to find
that our file pointer or file handler is at which character index'''
file1 = open("mayank.txt")
print(file1.mode) #it shows our file mode
print(file1.name) #it shows our file name
print(file1.tell()) # it will print 0 because we haven't start our readline
print(file1.readline())
print(file1.tell()) # it will print character index of second line because we once use readline
print(file1.readline())
print(file1.tell()) # it will print character index of third line because we once use readline
#you have to close file
file1.close()

'''it is for open file(mayank.txt in read mode). 'tell' will help to find that our file pointer or
file handler is at which character index and 'seek' will initialize your character index count'''
file1 = open("mayank.txt")
print(file1.tell()) # it will print 0 because we haven't start our readline
file1.seek(8)
print(file1.tell()) # it will print 8 because we seek(8)
print(file1.readline())
print(file1.tell()) # it will print character index of second line because we once use readline
file1.seek(0)
print(file1.tell()) # it will print 0 because we seek(0)
print(file1.readline())
print(file1.tell()) # it will print character index of third line because we once use readline
#you have to close file
file1.close()
