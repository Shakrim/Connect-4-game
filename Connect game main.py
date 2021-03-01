"""Connect 4 game """

# def my_board_desk
def my_board_desk(field):
    default_row = 11
    default_column = 13
    print(f'{"=" * 1} BOARD DESK {"=" * 1}')
    for row in range(default_row): # 0,1,2,3,4,5,6,7,8,9,10
        if row % 2 == 0:
            practical_row = int(row / 2)
            for column in range(default_column): #0,1,2,3,4,5,6,7,8,9,10,11,12
                if column % 2 == 0:
                    practical_column = int(column / 2)
                    if column != (default_column-1):
                        print(current_field[practical_column][practical_row],end="")
                    else:
                        print(current_field[practical_column][practical_row])
                else:
                    print("|", end = "")
        else:
            print("-" * (default_column))
    print(f'{"=" * 1} BOARD DESK {"=" * 1}')
    print()
    print(f'{"="*13} LAYOUT {"="*13}')
    for row in range(default_row): # 0,1,2,3,4,5,6,7,8,9,10
        if row % 2 == 0:
            practical_row = int(row/2)
            for column in range(default_column): #0,1,2,3,4,5,6,7,8,9,10,11,12
                if column % 2 == 0:
                    practical_column = int(column / 2)
                    if column != (default_column-1):
                        print(f'c{practical_column}r{practical_row}', end="")
                    else:
                        print(f'c{practical_column}r{practical_row}')
                else:
                    print("|", end = "")
        else:
            print("-" * (default_column+21))
    print(f'{"=" * 13} LAYOUT {"=" * 13}')



player = 1
current_field =[[" "," "," "," "," "," "], #c1r0 c1r1 c1r2 c1r3 c1r4 c1r5
                [" "," "," "," "," "," "], #c2r0 c2r1 c2r2 c2r3 c2r4 c2r5
                [" "," "," "," "," "," "], #c3r0 c3r1 c3r2 c3r3 c3r4 c3r5
                [" "," "," "," "," "," "], #c4r0 c4r1 c4r2 c4r3 c4r4 c4r5
                [" "," "," "," "," "," "], #c5r0 c5r1 c5r2 c5r3 c5r4 c5r5
                [" "," "," "," "," "," "], #c6r0 c6r1 c6r2 c6r3 c6r4 c6r5
                [" "," "," "," "," "," "]] #c7r0 c7r1 c7r2 c7r3 c7r4 c7r5
my_board_desk(current_field)
win = False
while not win:
    print("Player\'s turn", player)
    move_row = int(input("Please enter the row move: "))
    move_column = int(input("Please enter the column move: "))
    boardheight = 6
    boardwidth = 7
    if player == 1:
        #make a move for player 1
        if current_field[move_column][move_row] == " ":
            current_field[move_column][move_row] = "X"
            # check horizontal spaces
            for y in range(boardheight):
                for x in range(boardwidth - 3):
                    if current_field[x][y] == "X" and current_field[x + 1][y] == "X" and current_field[x + 2][y] == "X" and \
                            current_field[x + 3][y] == "X":
                        print(f'Player 1 won!')
                        win = True
            # check vertical spaces
            for x in range(boardwidth):
                for y in range(boardheight - 3):
                    if current_field[x][y] == "X" and current_field[x][y + 1] == "X" and current_field[x][y + 2] == "X" and current_field[x][
                        y + 3] == "X":
                        win = True
            # check / diagonal spaces
            for x in range(boardwidth - 3):
                for y in range(3, boardheight):
                    if current_field[x][y] == "X" and current_field[x + 1][y - 1] == "X" and current_field[x + 2][y - 2] == "X" and \
                            current_field[x + 3][y - 3] == "X":
                        win = True

            # check \ diagonal spaces
            for x in range(boardwidth - 3):
                for y in range(boardheight - 3):
                    if current_field[x][y] == "X" and current_field[x + 1][y + 1] == "X" and current_field[x + 2][y + 2] == "X" and \
                            current_field[x + 3][y + 3] == "X":
                        win = True
            player = 2

    else:
        # make a move for player 2
        if current_field[move_column][move_row] == " ":
            current_field[move_column][move_row] = "O"
            player = 1
    my_board_desk(current_field)

