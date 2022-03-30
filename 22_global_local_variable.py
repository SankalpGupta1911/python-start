#Scope, local variables, Global Variables and Global Keyword
#private function have only scope for that function and every function first check private variable and if it doesn't exist then global
#private function have scope for every function

'''l = 4 #Global variable
def func1(n):
    l=10 # it is local variable and we are initialising here. if this 'l' is not assigned here then l=4 from global var
    m=6 #local variable
    print(l, m)
    print(n, "I have printed")

func1("This is me")
print(l) # print 4'''


'''if we want to change value of global variable into function(if we change the value of global variable without 
using 'global' keyword then it will throw error. if you want to change global var value then you have to use 'global'
keyword in that function)'''
# wrong way to change global variable value: it is working and this is for show how we will get error
'''l = 4 #Global variable
def func1(n):
    l = l + 10 #'l' is global variable and we are trying to add 10 in that variable. it will throw error
    m = 6 #local variable
    print(l, m)
    print(n, "I have printed")

func1("This is me")
print(l)'''

# correct way of changing value of global varialble
'''l = 4 #Global variable
def func1(n):
    global l
    l = l + 10 #'l' is global variable and we are trying to add(10+4) in that variable. it will print 14
    m = 6 #local variable
    print(l, m)
    print(n, "I have printed")

func1("This is me")
print(l) #it will also print 14'''


# nested function
def mayank():
    x = 20
    def sakshi():
        global x
        x = 88
    print("Before calling sakshi", x)
    sakshi()
    print("After calling sakshi", x)

mayank()
print(x) # print 88 because it will create x in global variable with value 88