# Tuples(Immutable) '()'
# we can reassigned or modify list but if we don't want to modify then we use tuples

d1 = ()
print(type(d1)) # print type

tup1 = (1, 2, 3, 4)
print(tup1)
print(tup1[2])

#if we try to reassigned tup[2] then it will show error
# tup1[2] = 5
# print(tup1)

#if you want to reassigne tuple then you have to convert tuple in list
list1 = list(tup1)
list1[2] = 5
print(list1)
list1 = tuple(list1)
print(list1)

# tuples max, min, len is same as list