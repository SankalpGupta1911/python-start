# Decorators

# ----- start first we will revise function concept
'''def function1():
    print("Hello guys")
func2 = function1 #function 'function1' copy to func2
del function1 # delete 'function1' function
func2() # it will print 'Hello guys' because i copied 'function1' to 'func2' before delete 'function1' '''

'''def funcret(num):
    if num==0:
        return print
    elif num==1:
        return sum
input_val = int(input("Enter 0 or 1\n"))
a = funcret(input_val)
print(a)'''

# function as an argument
'''def executor(func):
    func("This")
executor(print)'''

# ----- End first we will revise function concept

# decorator
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1 #1st way of creating decorator
def who_is_mayank():
    print("Mayank is a good boy")

# who_is_mayank = dec1(who_is_mayank) #1st way of creating decorator
who_is_mayank()