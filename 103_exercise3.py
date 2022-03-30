# Exercise 3
'''write a program to check list of value is number or not and the value is
greater then 6. if value is number then print that value'''

list_val = ['first', 8, 'game', 7, 5, 'test', 9, 12]

for item in list_val:
    if str(item).isnumeric() and item>6:
        print(item)
