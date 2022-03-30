n = int(input("Enter how many input you want to take :\n"))
while True:
    print("Which comprehension you want to select")
    print("1.List\n2.Dictionary\n3.Set")
    inp = input()

    if inp not in ['1', '2', '3']:
        print("😞 Please enter a valid option 😞")
        continue
    else:
        inp = int(inp)

    if inp == 1:
        ls = [i for i in range(n)]
        print(ls)

    elif inp == 2:
        dict1 = {
            i: f"Item{i}" for i in range(n)
        }
        dict1 = {
            value:key
            for key,value in dict1.items()
        }
        print(dict1)

    elif inp == 3:

        set1 = {i for i in range(n)}

    print("Press Q to quit OR C to continue")

    opt1 = ""
    while (opt1 != "q" and opt1 != "c") or (opt1 != "q" and opt1 != "c"):
        opt1 = input()
        if opt1 == "q" or "Q":
            break
        elif opt1 == "C" or "c":
            continue