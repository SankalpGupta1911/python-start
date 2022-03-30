# Exercise 2 faulty calculator
'''design a calculator which will correctly solve all the problems except the following ones:
45*3=555, 56+9=77, 56/6=4 '''
'''Your program should take operator and the two number as input and then return the result'''

v1=int(input("Enter Variable 1:"))
v2=int(input("Enter Variable 2:"))
op=input("Enter the operator:")
print("The result is: ",end="")
if ((v1==45 and v2==3) or (v1==3 and v2==45)) and op=="*":
    print("555")
elif ((v1==56 and v2==9) or (v1==9 and v2==56)) and op=="+":
    print("77")
elif ((v1==56 and v2==6) or (v1==6 and v2==56)) and op=="/":
    print("77")
else:
    if op=="+":
        print(v1+v2)
    elif op=="-":
        print(v1-v2)
    elif op=="*":
        print(v1*v2)
    elif op=="/":
        print(v1/v2)
    elif op=="%":
        print(v1%v2)
    else:
        print("Invalid Input! Try Again!")

111111111111111111111111111111111111111111111111111111111111111111111111111

operator = input("Enter operator :")
firstNum = input("Enter FirstNum :")
secondNum = input("Enter SecondNum :")
FaultyDict={"45*3":"555", "56+9":"77","56/6":"4"}
expression = firstNum+operator+secondNum
reverse = secondNum+operator+firstNum
if expression in FaultyDict.keys():
    print (FaultyDict[expression])
    pass
elif reverse in FaultyDict.keys():
    print (FaultyDict[reverse])
    pass
else:
    print(eval(firstNum+operator+secondNum))