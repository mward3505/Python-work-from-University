import os

board = [" "] * 9
marks = ["X", "O"]
player = 1

win, draw, running = 1, -1, 0
game = running
mark = "X"


def check_position(x):
    return board[x] == " "


def board_filled():
    return not (" " in board)


def awesome_check(x, y):
    return board[x] != " " and board[x] == board[x+y] == board[x + (y*2)]


def check_win():
    global game
    if awesome_check(0, 1) or awesome_check(3, 1) or awesome_check(6, 1):
        game = win
    elif awesome_check(0, 3) or awesome_check(1, 3) or awesome_check(2, 3):
        game = win
    elif awesome_check(0, 4) or awesome_check(2, 2):
        game = win
    elif board_filled():
        game = draw


def draw_board():
    # for x in board:
    print("1 | 2 | 3 ")
    print(" %s| %s |%s" % (board[0], board[1], board[2]))
    print("__|___|__")
    print("4 | 5 | 6 ")
    print(" %s| %s |%s" % (board[3], board[4], board[5]))
    print("__|___|__")
    print("7 | 8 | 9 ")
    print(" %s| %s |%s" % (board[6], board[7], board[8]))


while game == running:
    draw_board()
    print("Player %d's Turn" % player)
    mark = marks[player - 1]
    choice = int(input("Enter the position you want to draw: ")) - 1
    if check_position(choice):
        board[choice] = mark
        player = 3 - player
        check_win()
        os.system('cls')

draw_board()
if game == draw:
    print("Game is a Draw.")
else:
    player = 3 - player
    print("Player %d Won." % player)
