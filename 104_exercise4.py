# Exercise 4
'''write a program to input numeric value from keyboard untill the input value is greater
than 100 and if input value is greater than 100 then print congratulations you have entered 'input value' '''

#first way
'''inp_val = int(input("Enter numeric value : "))
while inp_val<100:
    inp_val = int(input("Enter another numeric value : "))
print("congratulation you have entered", inp_val)'''

#second way

while True:
    inp_val = int(input("Enter value : \n"))
    if inp_val>=100:
        print("congratulation you have entered", inp_val)
        break
    else:
        print("Try Again!")
        continue