def cube(input_list):
    # function to cube the list of digits of the number entered by the user
    cubed_list = []
    for m in input_list:
        m = int(m)
        cubed_list.append(m**3)
    return cubed_list


while 1:
    num = input("Enter a number to check if its a armstrong number:  ")
    # asking the user to input the number
    try:
        a = len(num)
        digit_list = []
        for i in range(1, a + 1):
            # for loop to create a list of digits of the number entered by the user
            digit_list.append(num[(i - 1)])
        if sum(cube(digit_list)) == int(num):
            # checking if the number enteres is an armstrong number or not
            print("Number you have entered is an armstrong number.")
        else:
            print("Number you have entered is not an armstrong number.")
    except ValueError:
        print("Looks like the value entered its not a number")
    play = input("Enter any alphabet key if u want to play again and quit to exit:  ")
    if play.lower() == 'quit':
        # exiting the code 
        break
    else:
        # continuing if the user doesn't want to exit
        pass
