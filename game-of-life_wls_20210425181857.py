# Naive, brute force approach
# There's a nice convolution based approach in the problem notes
import copy

board=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

def printBoard(board):
    height = len(board)
    width = len(board[0])
    for x in range(height):
        for y in range(width):
            print(board[x][y], end="")
        print()

def printPrettyBoard(board):
    height = len(board)
    width = len(board[0])
    for x in range(height):
        for y in range(width):
            if board[x][y] == 1:
                print("X", end="")
            else:
                print("·", end="")
        print()

def game_of_life(board, steps):
    printPrettyBoard(board)
    print()
    height = len(board)
    width = len(board[0])
    for i in range(steps):
        nboard = copy.deepcopy(board)
        for x in range(height):
            for y in range(width):

                toprow = x - 1
                if toprow < 0:
                    toprow = height-1

                downrow = x + 1
                if downrow >= height:
                    downrow = 0

                leftcol = y - 1
                if leftcol < 0:
                    leftcol = width-1

                rightcol = y + 1
                if rightcol >= width:
                    rightcol = 0

                # print((x,y),(toprow,downrow,leftcol,rightcol))

                neighbours=0
                if board[toprow][rightcol] == 1:
                    neighbours += 1
                if board[toprow][y] == 1:
                    neighbours += 1
                if board[toprow][leftcol] == 1:
                    neighbours += 1
                if board[x][leftcol] == 1:
                    neighbours += 1
                if board[x][rightcol] == 1:
                    neighbours += 1
                if board[downrow][rightcol] == 1:
                    neighbours += 1
                if board[downrow][y] == 1:
                    neighbours += 1
                if board[downrow][leftcol] == 1:
                    neighbours += 1

                if board[x][y] == 1: # ALIVE
                    if neighbours < 2 or neighbours > 3:
                        nboard[x][y] = 0
                    else:
                        nboard[x][y] = 1
                else: # EMPTY
                    if neighbours == 3:
                        nboard[x][y] = 1
                    else:
                        nboard[x][y] = 0

        board = copy.deepcopy(nboard)
        printPrettyBoard(nboard)
        print()
    return nboard