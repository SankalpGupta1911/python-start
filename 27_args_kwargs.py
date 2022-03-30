# Args(*) and kwargs(**)

'''Suppose we are creating function with 4 argument but we passed 5 arguments in calling function
then it will throw error. another way of telling is suppose we have function with 4 name argument and we
have calling function with 4 names argument passes but in future we have to add few more names then we have
to add in both places and it is so hard to handle. So, for this type of problems we use args and kwargs'''
# understand with example : faulty program
# def func1(a, b, c, d): # here we have only 4 arguments
#     print(a, b, c, d)
# func1("Mayank", "Subodh", "Karan", "Amit", "Rohal") # here we passed 5 arguments

def func2(normal, *args1, **kwargs1):
    print(normal)
    for i in args1:
        print(i)
    print("\nNow i would like to introduce our heroes:")
    for key,value in kwargs1.items():
        print(f"{key} is a {value}")

names = ['Mayank', 'Subodh', 'Karan', 'Sakshi', 'Amit']
norm = "This is my normal argument and normal argument always put before args and kwargs in function argument"
kw = {"Mayank":"Head",
      "Subodh":"Monitor",
      "Amit":"Coordinator",
      "Karan":"Fitness Instructor"}
func2(norm, *names, **kw) '''if we will not pass here args(*) or kwargs(**) but we write
args(*) or kwargs(**) in the above function then still our program will run'''