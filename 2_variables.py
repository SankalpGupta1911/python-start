print("hello world")

# this is a single line comment

'''This is a 
multiple line 
comment'''

str1 = "this is string" #this is my string datatype variable
age = 20 #this is my int datatype variable
weight = 67.5 #this is my float datatype variable

print(str1)
print(type(str1)) # find type of variable
print(len(str1)) # find len of variable
print(str1[1:4:2]) # it will print index 1 to index 3 value but with the gap of 1
print(str1[0:15:3]) # it will print index 0 to index 15 value but with the gap of 2
print(str1.isalnum()) # find variable is alphanumeric or not it will return false bcoz it has space
print(str1.isalpha()) # find variable is alphabatic or not it will return false bcoz it has space
print(str1.endswith("string")) # find variable is end with 'string' or not it will return true bcoz it end with 'string'
print(str1.count("t")) # count 's' in this string
print(str1.capitalize()) # print first letter of string in capital case
print(str1.find("is")) # print starting index of 'is' in the string
print(str1.lower()) # print string in lower case
print(str1.upper()) # print string in upper case
print(str1.replace('is', 'are')) # print string with replacement of 'is' with 'are'
print(age)
print(type(age)) # find type of variable
print(weight)
print(type(weight)) # find type of variable

# Main python datatype - Numbers, Srings, Lists, Tuples, Dictionaries

print(str1, age+weight)
print("value of 3 + 5 =", 3 + 5)
print("value of 3 - 5 =", 3 - 5)
print("value of 3 * 5 =", 3 * 5)
print("value of 3 / 5 =", 3 / 5)
print("value of 3 ** 5 =", 3 ** 5)
print("value of 3 // 5 =", 3 // 5)  # '//' double divide is for removing decimal value

print("This is \"")  # '\' it is use when uh want to want double quote in print"

#multi line string
mls = '''This is a multiline string'''

print(mls)

