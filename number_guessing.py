import random
print("You have 3 tries to guess the secret number from 0 - 20")
while 1:
    ran_num = random.randint(0, 20)
    i = 1
    while i <= 3:
        entered_num = input("Your guess:  ")
        try:
            if ran_num == int(entered_num):
                print("You guessed right!!!")
                break
            else:
                pass
            i += 1
        except ValueError:
            print("Looks like you have not entered a number.")
    play_again = input("Enter any alphabet or number to continue and quit to quit:  ")
    if play_again.lower() == 'quit':
        break