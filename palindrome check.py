while 1:
    my_str = input("Enter a string to check if its a palindrome:  ")
    try:
        pal_str = my_str[::-1]
        if my_str == pal_str:
            print("The string you entered is a palindrome")
        else:
            print("The string you entered is not a palindrome")
    except TypeError:
        print("Looks like the value you have entered is not a string.")
    play = input("Press any alphabet key to continue and quit to exit:  ")
    if play.lower() == 'quit':
        break
    else:
        pass