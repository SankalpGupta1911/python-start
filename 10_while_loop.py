# while loop

'''number_inp = 0
while(number_inp<10):
    print(number_inp)
    number_inp = number_inp+1'''

#it will print untill condition is true
'''print("Enter a number")
number_inp = int(input())
while(number_inp>4):
    print("Number is greater then 4 and number =", number_inp)
    number_inp = number_inp-1'''

#it will ask every time after print
'''print("Enter a number")
number_inp = int(input())

while(number_inp>4):
    print("Number is greater then 4 and number =", number_inp)
    number_inp = int(input())'''

#At some point you want to user continue/break in loop
print("Enter a number")
number_inp = int(input())
while(number_inp>4):
    print("Number is greater then 4 and number =", number_inp)
    if (number_inp==6):
        break
    if (number_inp==8):
        number_inp = number_inp - 1
        continue
    print("loop ended")
    number_inp = number_inp - 1