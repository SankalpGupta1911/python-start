#Docstring is a comment which is written just after def 'function' line

def average(num1, num2):
    """This is my docstring of this function"""
    return (num1+num2)/2

av_val = average.__doc__
print(av_val)

#if function have no docsting then it will print 'None'