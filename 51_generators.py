# iteratable - __iter__() or __getitem__() if run any of these methods on object then it will provide iterator
# iterators - __next__()
# iterations - process of iterator is iteration
# generators - generator are those type of iterator which we can only one time traverse

# for i in range(78):
#     print(i)

def gen(n):
    for i in range(n):
        yield i #on the fly generate value
#generators are only once iterate
g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())

for i in g:
    print(i)

m = "Mayank" # only string is iterable
iter_val = iter(m)
print(iter_val.__next__())
print(iter_val.__next__())
print(iter_val.__next__())
print(iter_val.__next__())
print(iter_val.__next__())
print(iter_val.__next__())

for c in m:
    print(c)