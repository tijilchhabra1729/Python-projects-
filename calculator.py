print("Welcome to my calculator")
num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    print('''
    Type: 
    '+' for addition
    '-' for subtraction
    '*' for multiplication
    '/' for division''')
    type = input("Enter your command: ")
    try:
        if type.lower() == '+':
            answer = num_1 + num_2
            answer = str(answer)
            print("Your required result is " + answer)
            print("Thank you for using my calculator!!")
        if type.lower() == '-':
            answer = num_1 - num_2
            answer = str(answer)
            print("Your required result is " + answer)
            print("Thank you for using my calculator!!")
        if type.lower() == '*':
            answer = num_1 * num_2
            answer = str(answer)
            print("Your required result is " + answer)
            print("Thank you for using my calculator!!")
        if type.lower() == '/':
            answer = num_1 / num_2
            answer = str(answer)
            print("Your required result is " + answer)
            print("Thank you for using my calculator!!")
    except ArithmeticError:
        print("something went wrong!!")
        raise Exception()
    if type.lower() != "+" and type.lower() != "-" and type.lower() != "*" and type.lower() != "/":

        print("I don't understand that")
        print('''
    Please type any one of these and rerun:
    add for addition
    Difference for subtraction
    product for multiplication
    quotient for division
    ''')
except ValueError:
    print('''OOPS!! It seems you have entered something incorrect.
Enter a valid Number Next Time. Bye!!''')
except Exception:
    print("Better luck next time")
