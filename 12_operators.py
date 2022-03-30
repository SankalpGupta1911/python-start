# operators in python
'''
1. Arithmetic operators
2. Assignment operators
2. Comparison operators
2. Logical operators
2. Identity operators
2. Membership operators
2. Bitwise operators
'''

# Arithmetic operators
print("5 + 6 is", 5+6)
print("5 - 6 is", 5-6)
print("5 * 6 is", 5*6)
print("5 / 6 is", 5/6)
print("5 % 6 is", 15%6)
print("2 ** 3 is", 2**3) # 2 ki power 3
print("5 // 6 is", 5//6)

# Assignment operators
x = 5
print(5)
x+=7
print(x)
x/=7
print(x)
x*=4
print(x)
x-=4
print(x)
x%=2
print(x)

#Comparison operators
c = 7
print(c==4)
print(c<=4)
print(c>=4)
print(c!=4)

#Logical operators
a = True
b = False
print(a and a)
print(a and b)
print(b and b)
print(a or b)

#Identity operators
c = True
d = False
print(c is c)
print(c is d)
print(c is not d)
print(c is not c)

#Membership operators
list = [3, 9, 7, 10, 45, 6]
print(3 in list)
print(34 in list)
print(34 not in list)

#Bitwise operators(binary)
#0 = 00
#1 = 01
#2 = 10
#3 = 11
print(0 & 1) # print 0 because (0&0=0 0&1=0)=00 and 00 is '0' binary
print(0 | 1) # print 1 because (0|0=0 0|1=1)=01 and 01 is '1' binary
print(1 & 2) # print 0 because (0&1=0 1&0=0)=00 and 00 is '0' binary
print(0 | 2) # print 2 because (0|1=1 0|0=0)=10 and 00 is '2' binary
print(1 & 3) # print 2 because (0&1=0 1&1=1)=01 and 01 is '1' binary
print(1 | 3) # print 3 because (0|1=1 1|1=1)=11 and 11 is '3' binary
