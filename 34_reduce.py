# Reduce

list_val = [4, 8, 10, 2, 9, 1, 6, 5, 7]

''' suppose we need to add first value into second and second into third... etc and get sum of list_val values'''
# 1st method is with loop
num = 0
for i in list_val:
    num = num + i
print(num)

# 2nd method is with reduce
from functools import reduce
num = reduce(lambda x,y: x+y, list_val)
print(num)

# for multiply 1st value in 2nd value.. etc and get multiply value of list_val values
num = reduce(lambda x,y: x*y, list_val)
print(num)