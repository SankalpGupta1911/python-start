# Lists(Mutable) '[]'
# we can reassigned or modify list

l1 = []
print(type(l1)) # print type

colleges = ['IIT', 'NIT', 'AEC', 'HCST', 'IIT1', 'NIT1', 'AEC1', 'HCST1']
print(colleges)
print(colleges[1:4]) # it will print colleges[1] to colleges[3] value
print(colleges[0:7:2]) # it will print colleges[0] to colleges[7] value but with the gap of 1
print(colleges[0:7:3]) # it will print colleges[0] to colleges[7] value but with the gap of 2
print(colleges[2])
print(colleges[0])
for clg in colleges:
    print(clg)

#if you want to replace or re-assign any value of any array indexing(for example replace 'AEC' with 'Anand')
colleges[2] = 'Anand'
print(colleges[2])

#if you want to replace or re-assign full array
colleges = ['Anand', 'Hindustan']
print(colleges)
print(colleges[1])
print(colleges[0])
for clg in colleges:
    print(clg)


list2 = ['table', 'chair', 'fan', 'stool']
print(list2)

#if you want to append one more value in list2 array
list2.append('glass')
print(list2)

#if you want to append one more value in list2 array but at specific place
list2.insert(3, 'water')
print(list2)

#if you want to add more than one value only for showing in list2 array
print(list2 + ['pillow', 'bed', 'sofa'])

#if you want to remove one value from list2 array(for ex lets remove stool)
list2.remove('stool')
print(list2)

#if you want to get length of array
print(len(list2))

#if you want to get max(alphabatically largest value) of array
print(max(list2))

#if you want to get min(alphabatically smallest value) of array
print(min(list2))

numbers = [2 , 7, 4, 9, 20, 16]
print(numbers)
numbers.pop() # remove last value
print(numbers)
numbers.sort()
print(numbers) # print sorting in asc of numbers
numbers.reverse()
print(numbers) # print reverse of sorting numbers