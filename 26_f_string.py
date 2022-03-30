# F Strings

# these below 3 are basic concept
'''me = "Mayank"
a = "this is %s"%me
print(a)'''

'''me = "Mayank"
a1 = 3
a = "this is %s %s"%(me, a1)
print(a)'''

'''me = "Mayank"
a1 = 3
a = "this is {} {}"
b = a.format(me, a1)
print(b)
c = "this is {1} {0}"
d = c.format(me, a1)
print(d)'''


# f string concept
me = "Mayank"
a1 = 3
a = f"this is {me} {a1}"
print(a)
b = f"this is {a1} {me} {46*4}"
print(b)