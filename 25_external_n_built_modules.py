import random

random_number = random.randint(0,50) # print 0 to 50 any random int value
print(random_number)

rand = random.random() * 100 # print 0 to 100 any no. with decimal
print(rand)

rand_list = ['Mayank', 'Karan', 'Sakshi', 'Rohit', 'Subodh']
choice = random.choice(rand_list)
print(choice)