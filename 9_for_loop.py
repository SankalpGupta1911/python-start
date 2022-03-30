# Loops
#for loop
''' between multiple line comment have working code  '''

#basic for loops which 'i' will print 0 to 9 values
'''for i in range(0, 10):
    print(i)'''

#input with keyboard that how many times for loop will execute
'''number_inp = int(input())
for i in range(0, number_inp):
    print(i)'''

#for loop is for list
'''list1 = ['one', 'two', 'three', 'four', 'five']
for item in list1:
    print(item)'''

#for loop is for list of list
#first way
list1 = [[1, 2, 3], [10, 7, 6], [50, 17, 76]]
for item in list1:
    for item2 in item:
        print(item2)

#second way
list2 = [["Mayank", 23], ["Subodh", 34], ["Amit", 45]]
for name, age in list2:
    print(name, "age is", age)

#we can convert list into dictionary
dict_val = dict(list2)
print(dict_val)

#for loop for dictionary
#first method of print only key
for name in dict_val:
    print(name)

#second method of print only key
for name in dict_val.keys():
    print(name)

#print only values
for age in dict_val.values():
    print(age)

#first method of print key values
for item in dict_val.items():
    print(item)

#second method of print key values
for name, age in dict_val.items():
    print(name, "age is", age)
