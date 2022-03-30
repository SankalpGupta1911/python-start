# Exercise 1
'''create a dictionary and take input from the user and if that word exist in your dictionary
then return the meaning of that word from the dictionary else return You have entered wrong word'''

data = {"Set": "It's a collection of well define objects",
        "Mutable": "It can change",
        "Immutable": "It can't change"}

print("Enter a word from our dictionary('Set', 'Mutable', 'Immutable')")
keys_name = data.keys()
inpword = input()

#one way to check our input is correct or not
'''for key_item in keys_name:
    if key_item==inpword:
        checkexist = '1'
        break
    else:
        checkexist = '0' 

if checkexist=='1':
    print(data[inpword])
else:
    print("You have entered wrong word")'''

#second way to check our input is correct or not
if inpword in keys_name:
    checkexist = '1'
else:
    checkexist = '0'

if checkexist=='1':
    print(data[inpword])
else:
    print("You have entered wrong word")