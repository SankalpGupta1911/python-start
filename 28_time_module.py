import time

start_time = time.time()
k=0
while k<4:
    print("This is while loop")
    time.sleep(1) # it will stop program for one second and then run
    k+=1
print(f"While loop ran in {time.time() - start_time} seconds")

start_time2 = time.time()
for i in range(4):
    print("This is for loop")
print(f"For loop ran in {time.time() - start_time2} seconds")


#time.time() will return tick(seconds)
localtime = time.asctime(time.localtime(time.time())) # it will return current time with date, day
print(localtime)