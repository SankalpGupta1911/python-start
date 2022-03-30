# Exercise 4 Pattern printing
'''write a program to print pattern with the input value and if second input value is true then print
pattern in ascending order else second input value is false then print pattern in descending order'''

print("Enter n no. for rows and value should be in numeric : ")
n = int(input())
print("Enter 0 or 1 and value is in numeric : ")
bool_val = int(input())
new = bool(bool_val)
row = 0

if bool_val==True:
    while row<n:
        row = row+1
        print("*"*row)
elif bool_val==False:
    while row<n:
        print("*"*n)
        n = n-1