# Recursion
# two types of recursion : iterative and recursive


'''Iterative Method for finding factorial'''
# def factorial_iterative(n):
#     """
#     :param n: Integer
#     :return: n * n-1 * n-2 * n-3....1
#     """
#     fac = 1
#     for i in  range(n):
#         fac = fac * (i+1)
#     return fac
#
# number = int(input("Enter the number: "))
# print("Factorial using iterative method:", factorial_iterative(number))



'''Recursive Method for finding factorial'''
# def factorial_recursive(n):
#     """
#     :param n: Integer
#     :return: n * n-1 * n-2 * n-3....1
#     """
#     if n==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1) # factorial of three = 3*2*1
# '''
#         3 * factorial_recursive(2)
#         3 * 2 * factorial_recursive(1)
#         3 * 2 * 1
# '''
#
# number = int(input("Enter the number: "))
# print("Factorial using recursive method:", factorial_recursive(number))



'''Recursive Method for find the no. in fibonacci series'''
def fibonacci(n):
    """
    :param n: 0, 1, 1, 2, 3, 5...nth
    """
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the number: "))
print("fibonacci series no. is: ", fibonacci(number))