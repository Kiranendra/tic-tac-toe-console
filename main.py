p1 = 'X'
p2 = 'O'
play_game = True
available_positions = [1,2,3,4,5,6,7,8,9]
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

print(" Welcome to Tic Tac Toe Console Game ")
print("\n Player 1: X \n Player 2: O \n")

for i in board:
    for j in i:
        print(" " + j, end=' |')
    print("\n ------------")
    
key = input("\n Press 'ENTER' to start the game ")
turn = 1
if key == '':
    print(' Game Started \n')
else:
    quit()
    
def re_initialize():
    global available_positions, board
    available_positions = [1,2,3,4,5,6,7,8,9]
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    print("\n NEW GAME \n")
    
    for i in board:
        for j in i:
            print(" " + j, end=' |')

        print("\n ------------")


def remove_pos(pos):
    available_positions.remove(pos)


def insert_in_board(pos, item):
    if pos == 1:
        board[0][0] = item
        remove_pos(pos)
        print()
    elif pos == 2:
        board[0][1] = item
        remove_pos(pos)
        print()
    elif pos == 3:
        board[0][2] = item
        remove_pos(pos)
        print()
    elif pos == 4:
        board[1][0] = item
        remove_pos(pos)
        print()
    elif pos == 5:
        board[1][1] = item
        remove_pos(pos)
        print()
    elif pos == 6:
        board[1][2] = item
        remove_pos(pos)
        print()
    elif pos == 7:
        board[2][0] = item
        remove_pos(pos)
        print()
    elif pos == 8:
        board[2][1] = item
        remove_pos(pos)
        print()
    elif pos == 9:
        board[2][2] = item
        remove_pos(pos)
        print()
    else:
        print(" Invalid Position")
        print()

def check_available_pos():
    if len(available_positions) == 0:
        return True
    else:
        return False

def check_win():
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return ""
    

while play_game:

    if turn == 1:
        print(f" Player {turn} turn ")
        print(f"\n Where do you want to insert 'X' in {available_positions}: ", end='')
        pos = input()
        try:
            pos = int(pos)
        except ValueError:
            print(' Enter number only')


        if pos in available_positions:
            insert_in_board(pos, p1)
            for i in board:
                for j in i:
                    print(" " + j, end=' |')

                print("\n ------------")
                    
            turn = 2
            win = check_win()
            if win != "" and win != "-":
                if win == p1:
                    print(' Player 1 won the game')
                else:
                    print(' Player 2 won the game')

                play_game = False

            if check_available_pos():
                if win == p1 or win == p2:
                    pass
                else:
                    print(' DRAW')
                    
                play_game = False
        else:
            print(" Number not in range")

    else:
        print(f" Player {turn} turn ")
        print(f"\n Where do you want to insert 'O' in {available_positions}: ", end='')
        pos = input()
        try:
            pos = int(pos)
        except ValueError:
            print(' Enter number only')

        if pos in available_positions:
            insert_in_board(pos, p2)
            for i in board:
                for j in i:
                    print(" " + j, end=' |')

                print("\n ------------")
                    
            turn = 1
            win = check_win()
            if win != "" and win != "-":
                if win == p1:
                    print(' Player 1 won the game')
                else:
                    print(' Player 2 won the game')

                play_game = False

            if check_available_pos():
                if win == p1 or win == p2:
                    pass
                else:
                    print(' DRAW')
                    
                play_game = False
        else:
            print(" Number not in range")

    if play_game == False:
        inp = input(" Do you want to play again[y/n]? ")
        if inp.lower().strip() == "y":
            re_initialize()
            play_game = True
        else:
            quit()
