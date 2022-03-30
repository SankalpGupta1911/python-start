#Exception handling

'''first example or error: both input is int but enter num2 as non int value
then it will throw error in line no. 9 and our program will terminate from
line 9 without execute remaining program'''
#print("Enter 1st number:")
#num1 = int(input())
#print("Enter 2nd number:")
#num2 = int(input())
#print("the sum of these two number", num1+num2)
#print("This line is important")

'''Second example or error: enter both input but in second input we entered non int value 
and assign both variable is int in print statement then it will throw error in line no. 20 
and again our program will terminate from line 20 without execute remaining program'''
#print("Enter 1st number:")
#num1 = input()
#print("Enter 2nd number:")
#num2 = input()
#print("the sum of these two number", int(num1)+int(num2))
#print("This line is important")


'''now we use exception handling for this type of program where i want to execute 
remaining program after any getting error'''
print("Enter 1st number:")
num1 = input()
print("Enter 2nd number:")
num2 = input()
try:
    print("the sum of these two number", int(num1)+int(num2))
except Exception as e:
    print(e)
print("This line is important")