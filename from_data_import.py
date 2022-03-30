testing = "Mayank"

def testClass(a_string):
    return f"This is created function for export {a_string}"

def printmay(strin_val):
    return f"Ye string mayank ko dede {strin_val}"

#wrong addition class
def add(num1, num2):
    return num1 + num2 +5

'''Suppose any file import testClass function from this file then it will run below content also from testClass '''
'''print(printmay("Thakur"))
addition = add(15, 6)
print(addition)'''

'''for not run below content from testClass() after import testClass() we use __name__=='__main__' '''
if __name__ == '__main__':
    print(printmay("Thakur"))
    addition = add(15, 6)
    print(addition)

'''value of __name__ is __main__ if we run current/own file but if we import 
this file to another file then into that file __name__ value of this file is from_data_import(file name)'''
print("And the name is", __name__)