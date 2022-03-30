# File IO


'''it is for open file(mayank.txt in write mode and write mode will replace your old data). if this file doesnot
exist in our current directory then it will create automatically'''
file1 = open("mayank.txt", "w")
print(file1.mode) #it shows our file mode
print(file1.name) #it shows our file name

# if will write data in our file
file1.write("write this to my file\nMy name is mayank")
#you have to close file
file1.close()

'''it is for open file(mayank.txt in append mode) and append mode is use for 
not replace our old data and merge our current data into old data'''
file1 = open("mayank.txt", "a")
print(file1.mode) #it shows our file mode
print(file1.name) #it shows our file name

# if will append data in our file
write_count = file1.write("\nMy age is 23\nLived in dayalbagh")
print(write_count) # it return how many characters we have write in our file
#you have to close file
file1.close()


'''it is for open file(mayank.txt in write mode). if this file doesnot
exist in our current directory then it will create automatically'''
# file1 = open("mayank.txt", "wb")
# print(file1.mode) #it shows our file mode
# print(file1.name) #it shows our file name
#
# # if will write data in our file
# file1.write(bytes("write this to my file", "UTF-8"))
# #you have to close file
# file1.close()

'''it is for open file(mayank.txt in read and write mode).'''
file1 = open("mayank.txt", "r+")
print(file1.mode) #it shows our file mode
print(file1.name) #it shows our file name
text_read = file1.read()
print(text_read)
file1.write("\nThanks for your patient")
#you have to close file
file1.close()