# Exercise 5 Health Management System
# 3 Clients - Mayank, Sakshi, Karan
# Total 6 files
# Write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def getdate():
    import datetime
    return datetime.datetime.now()

def take(k):
    if k==1:
        c = int(input("Press 1 for exercise and press 2 for food: "))
        if c==1:
            value = input("Type your exercise\n")
            with open("mayank_ex.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
        elif c==2:
            value = input("Type your food\n")
            with open("mayank_food.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
    elif k==2:
        c = int(input("Press 1 for exercise and press 2 for food: "))
        if c==1:
            value = input("Type your exercise\n")
            with open("sakshi_ex.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
        elif c==2:
            value = input("Type your food\n")
            with open("sakshi_food.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
    elif k==3:
        c = int(input("Press 1 for exercise and press 2 for food: "))
        if c==1:
            value = input("Type your exercise\n")
            with open("karan_ex.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
        elif c==2:
            value = input("Type your food\n")
            with open("karan_food.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")


def retrieve(k):
    if k==1:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c==1:
            with open("mayank_ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("mayank_food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c==1:
            with open("sakshi_ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("sakshi_food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==3:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c==1:
            with open("karan_ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("karan_food.txt") as op:
                for i in op:
                    print(i,end="")

print("Health Management System:")
a = int(input("Press 1 for log the value and press 2 for retrieve the values: "))

if a==1:
    b = int(input("Press 1 for Mayank, 2 for Sakshi and 3 for Karan: "))
    take(b)
elif a==2:
    b = int(input("Press 1 for Mayank, 2 for Sakshi and 3 for Karan: "))
    retrieve(b)