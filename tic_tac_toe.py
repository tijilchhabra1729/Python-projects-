def cls():
    # function to clear the terminal
    print('\n' * 100)


def create_board(board):
    # function to print the board
    print(' ' + board[6] + '|' + board[7] + '|' + board[8])
    print('-------')
    print(' ' + board[3] + '|' + board[4] + '|' + board[5])
    print('-------')
    print(' ' + board[0] + '|' + board[1] + '|' + board[2])


def win():
    # function to check matches to identify the winner
    iswin  = False
    if play_board_list[0] == 'X' and play_board_list[1] == 'X' and play_board_list[2] == 'X':
        # check for bottom horizontal match for X
        iswin = True
        return iswin
    elif play_board_list[0] == 'O' and play_board_list[1] == 'O' and play_board_list[2] == 'O':
        # check for bottom horizontal match for O
        iswin = True
        return iswin
    elif play_board_list[3] == 'X' and play_board_list[4] == 'X' and play_board_list == 'X':
        # check for middle horizontal match for X
        iswin = True
        return iswin
    elif play_board_list[3] == 'O' and play_board_list[4] == 'O' and play_board_list == 'O':
        # check for middle horizontal match for O
        iswin = True
        return iswin
    elif play_board_list[6] == 'X' and play_board_list[7] == 'X' and play_board_list[8] == 'X':
        # check for top horizontal match for X
        iswin = True
        return iswin
    elif play_board_list[6] == 'O' and play_board_list[7] == 'O' and play_board_list[8] == 'O':
        # check for top horizontal match for O
        iswin = True
        return iswin
    elif play_board_list[0] == 'X' and play_board_list[3] == 'X' and play_board_list[6] == 'X':
        # check for first vertical match for X
        iswin = True
        return iswin
    elif play_board_list[0] == 'O' and play_board_list[3] == 'O' and play_board_list[6] == 'O':
        # check for first vertical match for O
        iswin = True
        return iswin
    elif play_board_list[1] == 'X' and play_board_list[4] == 'X' and play_board_list[7] == 'X':
        # check for second vertical match for X
        iswin = True
        return iswin
    elif  play_board_list[1] == 'O' and play_board_list[4] == 'O' and play_board_list[7] == 'O':
        # check for second vertical match for O
        iswin = True
        return iswin
    elif play_board_list[2] == 'X' and play_board_list[5] == 'X' and play_board_list[8] == 'X':
        # check for third vertical match for X
        iswin = True
        return iswin
    elif play_board_list[2] == 'O' and play_board_list[5] == 'O' and play_board_list[8] == 'O':
        # check for third vertical match for O
        iswin = True
        return iswin
    elif play_board_list[0] == 'X' and play_board_list[4] == 'X' and play_board_list[8] == 'X':
        # check for first diagonal match for X
        iswin = True
        return iswin
    elif play_board_list[0] == 'O' and play_board_list[4] == 'O' and play_board_list[8] == 'O':
        # check for first diagonal match for O
        iswin = True
        return iswin
    elif play_board_list[2] == 'X' and play_board_list[4] == 'X' and play_board_list[6] == 'X':
        # check for second diagonal match for X
        iswin = True
        return iswin
    elif play_board_list[2] == 'O' and play_board_list[4] == 'O' and play_board_list[6] == 'O':
        # check for second diagonal match for O
        iswin = True
        return iswin
    else:
        return iswin


while 1:
    print("Keep this grid in mind and accordingly tell the position of your piece on your turn: ")
    board_test_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    create_board(board_test_list)
    print('\n' * 5)
    play_board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    create_board(play_board_list)
    playctr = 1
    winner = False
    while (playctr <= 4) and (winner == False):
        incorrect = True
        while incorrect:
            player1_input = int(input("Player 1 enter your position (X): "))
            if play_board_list[player1_input - 1] != ' ':
                print("enter again, this position is already occupied")
                incorrect = True
            else:
                play_board_list[player1_input - 1] = 'X'
                incorrect = False
        create_board(play_board_list)
        incorrect = True
        winner = win()
        if winner:
            print("Player1 wins")
            break
        if not winner:
            while incorrect:
                player2_input = int(input("Player 2 enter your position (O): "))
                if play_board_list[player2_input - 1] != ' ':
                    print("enter again, this position is already occupied")
                    incorrect = True
                else:
                    play_board_list[player2_input - 1] = 'O'
                    incorrect = False
            create_board(play_board_list)
            playctr += 1
            winner = win()
            if winner:
                print("player2 wins")
                break
    else:
        player1_input = int(input("Player 1 enter your position (X): "))
        play_board_list[player1_input - 1] = 'X'
        create_board(play_board_list)
        winner = win()
        if winner:
            print("player1 wins")
        else:
            print("It's a draw")
    play = input("Press any alphabet/number key to continue and quit to quit:  ")
    if play.lower() == 'quit':
        break
    else:
        pass