# if else statements

''' between multiple line comment have working code  '''

#if we want input field and print that input value
'''number = input()
print(number)'''

# in above input() it will take string input bydefault and if we want integer input then
'''int_number = int (input())
print(int_number)'''

# grade check program with the help of and operator
'''print('Enter your marks')
marks = int (input())
print(marks)
if (marks>=90 and marks<=100):
    grade = 'A'
elif (marks>=80 and marks<90):
    grade = 'B'
else:
    grade = 'fail'
print("The grade is", grade)'''


# grade program with the help of or operator
'''print('Enter your marks')
marks = int (input())
print(marks)
if (marks>=90 or marks<=100):
    grade = 'A'
else:
    grade = 'fail'
print("The grade is", grade)'''

# check list have input value or not with the help of 'in' and 'not in'
list_data = [70, 75, 4, 10, 56]
print('Enter your value')
inp_val = int (input())
print(inp_val in list_data)
if inp_val not in list_data:
    check = 'not in our records'
elif inp_val in list_data:
    check = 'in our records'
print("Entered value is", check)