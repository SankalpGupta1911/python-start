# Set

s1 = set()
print(type(s1)) # print type

#one way of set
s_from_list = set([1, 2, 3, 4])
print(s_from_list)
print(type(s_from_list))

#second way of set
list = [1, 2, 3, 4]
s_from_list = set(list)
print(s_from_list)
print(type(s_from_list))

set_v = set({74, 80})

#add value in set
set_v.add(1)
#set always retain unique values. so if we add '1' multiple times but it will print only single 1
set_v.add(1)
set_v.add(1)
set_v.add(2)
set_v.add(8)
set_v.add(9)
print(set_v) # print set

#union of set (unique values of two set)
set_v1 = set_v.union({1, 2, 3})
print(set_v1)

#intersection of set (common values of two sets)
set_v2 = set_v.intersection({1, 2, 3})
print(set_v2)

#disjoint of set (both sets are different if yes then print 'true' else 'false')
set_v3 = {4, 15}
print(set_v.isdisjoint(set_v3))

#remove value from set
set_v.remove(2)
print(set_v)