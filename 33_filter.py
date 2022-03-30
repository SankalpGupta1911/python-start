# Filter

list_val = [4, 8, 10, 2, 9, 1, 6, 5, 7]

'''We need only greater than 5 values of this list_val'''
def is_grt_5(num):
    return num>5 #it will return True or False

greater_than_5 = list(filter(is_grt_5, list_val))

print(greater_than_5)