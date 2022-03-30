# Snake Water Gun game
'''
user = u, computer = c, snake = s, water = w, gun = g
s.u and w.c = win u because snake drink water
g.u and w.c = win c because gun doobgyi water mai
g.u and s.c = win u because gun shoot snake
'''

'''write a program for create a game which is play between computer and user. Tt will play 10 times.
show who win every single time and in the end show win more out of 10 times'''

import random
user_count = 0
comp_count = 0
loop_count = 0
comp_list = ['S', 'G', 'W']
print("Snake = S, Gun = G, Water = W")
while loop_count<10:
    user_inp = input("Enter your choice from S, G and W: ")
    user_cap = user_inp.capitalize()
    comp_choice = random.choice(comp_list)
    if user_cap=='S' and comp_choice=='G':
        comp_count = comp_count + 1
        loop_count = loop_count + 1
        print("You =", user_cap, "Computer =",comp_choice)
        print("Computer win this round. Score is Computer=",comp_count," and You=",user_count,"\n", 10-loop_count," chances left")
    elif user_cap == 'S' and comp_choice == 'W':
        user_count = user_count + 1
        loop_count = loop_count + 1
        print("You =", user_cap, "Computer =", comp_choice)
        print("You win this round. Score is Computer=",comp_count," and You=",user_count,"\n", 10-loop_count," chances left")
    elif user_cap=='G' and comp_choice=='S':
        user_count = user_count + 1
        loop_count = loop_count + 1
        print("You =", user_cap, "Computer =", comp_choice)
        print("You win this round. Score is Computer=",comp_count," and You=",user_count,"\n", 10-loop_count," chances left")
    elif user_cap == 'G' and comp_choice == 'W':
        comp_count = comp_count + 1
        loop_count = loop_count + 1
        print("You =", user_cap, "Computer =", comp_choice)
        print("Computer win this round. Score is Computer=",comp_count," and You=",user_count,"\n", 10-loop_count," chances left")
    elif user_cap=='W' and comp_choice=='S':
        comp_count = comp_count + 1
        loop_count = loop_count + 1
        print("You =", user_cap, "Computer =", comp_choice)
        print("Computer win this round. Score is Computer=",comp_count," and You=",user_count,"\n", 10-loop_count," chances left")
    elif user_cap == 'W' and comp_choice == 'G':
        user_count = user_count + 1
        loop_count = loop_count + 1
        print("You =", user_cap, "Computer =", comp_choice)
        print("You win this round. Score is Computer=",comp_count," and You=",user_count,"\n", 10-loop_count," chances left")
    elif user_cap=='S' and comp_choice=='S':
        loop_count = loop_count + 1
        print("You =", user_cap, "Computer =", comp_choice)
        print("This round is tie. Score is Computer=",comp_count," and You=",user_count,"\n", 10-loop_count," chances left")
    elif user_cap == 'G' and comp_choice == 'G':
        loop_count = loop_count + 1
        print("You =", user_cap, "Computer =", comp_choice)
        print("This round is tie. Score is Computer=", comp_count, " and You=", user_count, "\n", 10 - loop_count,
              " chances left")
    elif user_cap == 'W' and comp_choice == 'W':
        loop_count = loop_count + 1
        print("You =", user_cap, "Computer =", comp_choice)
        print("This round is tie. Score is Computer=", comp_count, " and You=", user_count, "\n", 10 - loop_count,
              " chances left")
    elif user_cap != '' and (user_cap != 'W' or user_cap != 'S' or user_cap != 'G'):
        print("You have entered something wrong")
        print("Again play this round. Score is Computer=", comp_count, " and You=", user_count, "\n", 10 - loop_count,
              " chances left")
print("You =", user_count, "Computer =", comp_count)
if user_count>comp_count:
    print("You win")
elif user_count<comp_count:
    print("Computer win")
elif user_count==comp_count:
    print("It's a tie")