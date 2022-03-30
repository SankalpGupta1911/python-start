# File read with 'with'

''' if we don't want to write 'open() and close()' then we use 'with' '''
# best way to open file
with open("mayank.txt") as file1:
    val = file1.read(4)
    print(val)