#list comprehensions
'''suppose we need number between 0-100 which is divisible by 3'''
'''ls = []
for i in range(1 ,100):
    if i%3==0:
        ls.append(i)
print(ls)'''

'''We can do above problem with list comprehensions'''
'''ls = [i for i in range(1, 100) if i%3==0]
print(ls)'''

#dictionary comprehensions
'''suppose we want to create dictionary 0-99 like {0:"item0", 1:"item1", 2:"item2"... so on to 99}'''

# dict = {0:"item0", 1:"item1", 2:"item2"} #this is the worst method to create this

'''dict1 = {i:f"Item{i}" for i in range(1, 100)}
print(dict1)
# if we want only 3 divisible values
dict2 = {i:f"Item{i}" for i in range(1, 100) if i%3==0}
print(dict2)
dict3 = {value:key for key, value in dict2.items()} #if we want key as a value and value as a key
print(dict3)'''

# Set comprehensions
'''dresses = {dress for dress in ["Dress1", "Dress2", "Dress1", "Dress2", "Dress1", "Dress2"]}
print(dresses) #it will return only 2 value of set 'dresses' bcoz remaining are same
print(type(dresses)) #it will return set class'''

# Generator comprehensions
evens = (i for i in range(100) if i%2==0)
print(type(evens))
print(evens)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
# for item in evens:
#     print(item)