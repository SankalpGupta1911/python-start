list_val = ["Subodh", "Mayank", "Amit", "Karan", "Mohit"]

# for print this and join we use for loop
for item in list_val:
    print(item, "and", end=" ")
print("are Integer employees")

# we can do this in one line and without using for loop with the help of join function.
join_data = " and ".join(list_val)
print(f"{join_data} are Integer employees")

join_data = ", ".join(list_val)
print(f"{join_data} are Integer employees")