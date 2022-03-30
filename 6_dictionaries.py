# Dictionaries '{}'

d1 = {}
print(type(d1)) # print type

names = {'Mayank': 20,
         'Karan': 40,
         'Rahul': 25,
         'Sakshi': 30}  #it is key/name and value/age pair

#if we want 'Rahul' age
print(names['Rahul'])

#if we want to update 'Rahul' age
names['Rahul'] = 45
print(names['Rahul'])

#by any chance we forget our keys and we want to print all keys
print(names.keys())

#by any chance we forget our values and we want to print all values
print(names.values())

# print all key:value pairs
print(names.items())

name = {'Subodh': "burger",
         'Amit': "fish",
         'Kratika': "chicken",
         'Mukul': {"A":"egg", "B":"cake", "C":"sandwich"}}  #In 'Mukul' it has another dictionary

print(name) #print full dictionary
print(name["Mukul"]) #print 'Mukul' dictionary
print(name.get("Mukul")) # another way to get value and print 'Mukul' dLictionary
print(name["Mukul"]["B"]) #print 'Mukul' 'B' value

#merge/update in dictionary
#first way to update
name["Sahil"] = "meat"
name["Rohan"] = "beaf"
print(name) #print full dictionary after merge

#second way to update
name.update({"Rohit":"pastry"})
print(name) #print full dictionary after merge

#delete some key:value in dictionary
del name["Kratika"]
print(name) #print full dictionary after delete

#copy 'name' to 'test_name'
test_name = name
del test_name["Sahil"]
print(test_name)
print(name) # we deleted from 'test_name' but it deleted from name also
'''if we direct put '=' between two dictionary and then delete 'test_name["Sahil"]' 
then it will also delete from 'name["Sahil"]' because it will use as pointers(referrence).
if we want proper work of copy and if we delete from another dictionary key and it will not
deleted from another dictionary key then we use 'copy' '''

#copy 'name' to 'test_name'
test_name = name.copy()
del test_name["Amit"]
print(test_name) # we deleted from 'test_name["Amit"]'
print(name) # we deleted from 'test_name["Amit"]' but this time 'name["Amit"]' not deleted

new_dict = input()
print(type(new_dict))
print(new_dict)