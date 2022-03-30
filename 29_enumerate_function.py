# emurate function
''' manlo tum kuch samaan lene gye or baadme ghar se call aaya ki list k even numbers waale item mat laana '''

list_val = ["Coffee", "Tea", "Milk", "Toffee", "Sugar", "Salt", "Haldi"]

# basic way to make remaining item list
i = 1
for item in list_val:
    if i%2 != 0:
        print(f"Jarvis please buy {item}")
    i += 1


# enumerate way to make remaining item list
for index, item in enumerate(list_val):
    if index%2 == 0:
        print(f"Jarvis please buy {item}")
