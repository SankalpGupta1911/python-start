khana = ["roti", "sabzi", "dal"]
'''we can end our loop by two ways 1st is with the break and 2nd is for loop completion. Else only work with 2nd way of for loop'''
# 1st way
for item in khana:
    if item=="sabzi":
        break
else:
    print("Your item was not found")


# 2nd way
for item in khana:
    if item=="paratha":
        break
else:
    print("Your item was not found")