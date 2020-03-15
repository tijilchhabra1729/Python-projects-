def cube(input_list):
    cubed_list = []
    for m in input_list:
        m = int(m)
        cubed_list.append(m**3)
    return cubed_list


while 1:
    num = input("Enter a number to check if its a armstrong number:  ")
    try:
        a = len(num)
        digit_list = []
        for i in range(1, a + 1):
            digit_list.append(num[(i - 1)])
        if sum(cube(digit_list)) == int(num):
            print("Number you have entered is an armstrong number.")
        else:
            print("Number you have entered is not an armstrong number.")
    except ValueError:
        print("Looks like the value entered its not a number")
    play = input("Enter any alphabet key if u want to play again and quit to exit:  ")
    if play.lower() == 'quit':
        break
    else:
        pass