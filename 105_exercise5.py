# Exercise 4 guess game
'''write a program to guess a pre assigned number and you will guess from input numeric value from keyboard
untill that you have to show input value is greater or smaller then assigned value and you will get 9 turns to guess'''

assi_value = 40
turns = 9
took = 1

while True:
    inp_val = int(input("Enter your guess value : \n"))
    if inp_val<assi_value:
        if turns==1:
            break
        turns = turns - 1
        took = took + 1
        print("You guess smaller value. Remaining guess turn : ", turns)
        continue
    elif inp_val>assi_value:
        if turns==1:
            break
        turns = turns - 1
        took = took + 1
        print("You guess greater value. Remaining guess turn : ", turns)
        continue
    elif inp_val==assi_value:
        print("Congrats your guess value is correct.")
        print("No. of guesses you took", took)
        break