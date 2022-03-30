'''Map'''
list_val = ["34", "50", "14", "46", "78"]

#Suppose we need to add 1 in 14(list_val[2]) we need to change list_val values in integer because its in string

# 1st method is for loop
'''for i in range(len(list_val)):
    list_val[i] = int(list_val[i])'''

# 2nd method is we can change string to integer with one line and without for loop
list_val = list(map(int, list_val))

list_val[2] = list_val[2] + 1
print(list_val)

'''Use map with lambda'''
# we need squares of the list _val values
# 1st method
'''def sq(a):
    return a*a
square_list = list(map(sq, list_val))
print(square_list)'''

# 2nd method is with the help of lambda
'''square_list = list(map(lambda x:x*x, list_val))
print(square_list)'''

# we need squares and cubes of the list _val values by single lambda
def sqaure(a):
    return a*a

def cube(a):
    return a*a*a

func = [sqaure, cube]

for item in range(len(list_val)):
    values = list(map(lambda x:x(list_val[item]), func))
    print(values)
