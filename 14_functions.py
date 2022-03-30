#Functions

#user define function
def average(num1, num2):
    return (num1+num2)/2

av_val = average(2, 4)
print(av_val)

def sum_f(num1, num2):
    val = num1+num2
    print("Sum value is ", val)

sum_val = sum_f(2, 4)
print(sum_val) # print none because sum_f didn't use return

#built in function or predefined function
a = 9
b = 10
c = sum((a, b)) # sum is built in function or predefined function
print(c)