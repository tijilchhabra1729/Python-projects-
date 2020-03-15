import random


def win():
    if user_inp.lower() == 'rock' and ran == 'rock':
        print("It's a tie! Computer too chose rock")
    elif user_inp.lower() == 'rock' and ran == 'paper':
        print("Computer wins! Computer chose paper.")
    elif user_inp.lower() == 'rock' and ran == 'scissors':
        print("You win! Computer chose scissors.")
    elif user_inp.lower() == 'paper' and ran == 'paper':
        print("It's a tie! Computer too chose paper")
    elif user_inp.lower() == 'paper' and ran == 'scissors':
        print("Computer wins! Computer chose scissors.")
    elif user_inp.lower() == 'paper' and ran == 'rock':
        print("You win! Computer chose rock.")
    elif user_inp.lower() == 'scissors' and ran == 'scissors':
        print("It'a a tie! Computer too chose scissors.")
    elif user_inp.lower() == 'scissors' and ran == 'rock':
        print("Computer wins! Computer chose rock.")
    elif user_inp.lower() == 'scissors' and ran == 'paper':
        print("You win! Computer chose paper.")


inp_list = ['rock', 'paper', 'scissors']
while True:
    ran = random.choice(inp_list)
    user_inp = input("Enter 'rock' or 'paper' or 'scissors':  ")
    if user_inp.lower() not in inp_list:
        print("I don't understand that")
    win()
    play = input("Press any alphabet or number key to continue and quit to exit:  ")
    if play.lower() == 'quit':
        break
    else:
        pass