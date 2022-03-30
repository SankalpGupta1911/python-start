# This is for factorial by genators, and printing the sequence:-
def factcal(n):
    if n == 1:
        return 1
    return n * factcal(n - 1)


def factgen(n):
    i = 1
    while i <= n:
        yield factcal(i)
        i += 1


num = int(input("Enter your number?\n"))
g = factgen(num)
for i in g:
    print(i)


# This is for fibonacci series to print all it series by using genarotors:-
def fibocal(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibocal(n - 1) + fibocal(n - 2)


def fibogen(n):
    i = 1
    while i <= n:
        yield fibocal(i)
        i += 1


num = int(input("Enter your number for fibonacci series?\n"))
g = fibogen(num)
for i in g:
    print(i)