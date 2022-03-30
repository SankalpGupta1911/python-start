# Strings

string1 = "this is mayank"
print(type(string1)) # find type of variable
print(len(string1)) # find len of variable
print(string1[0:3]) # fetch 0 to 3 indexing character
print(string1[2:10]) # fetch 2 to 10 indexing character
print(string1[-5:]) # fetch -5 to end indexing character
print(string1[:-2]) # fetch start to -2 indexing character
print(string1[1:4:2]) # it will print index 1 to index 3 value but with the gap of 1
print(string1[0:15:3]) # it will print index 0 to index 15 value but with the gap of 2
print(string1.isalnum()) # find variable is alphanumeric or not it will return false bcoz it has space
print(string1.isalpha()) # find variable is alphabatic or not it will return false bcoz it has space
print(string1.endswith("mayank")) # find variable is end with 'string' or not it will return true bcoz it end with 'string'
print(string1.count("s")) # count 's' in this string
print(string1.capitalize()) # change first letter of character into capital
print(string1.lower()) # print string in lower case
print(string1.upper()) # print string in upper case
print(string1.find('m')) # find character start indexing
print(string1.rfind('m')) # find character start indexing in reverse order
print(string1.replace('mayank', 'karan')) # replace any characters