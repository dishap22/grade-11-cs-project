# Process
# 1. Creating a boart using 2D lists and making temporary board
# 2. Making the mermging functions for up, down, right and left
# 3. Starting game (requires empty gameboard and random values)
# 4. Making rounds, user chooses to merge in one of the four directions, then next boar shows
# 5. Add new values per round
# 6. Check if user has won/lost

import random
import copy

# variable for board size
boardSize = 4

# printing out board in grid format


def display():
    # finding largest value on board
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    # maximum no. of spaces needs to be according to length of largest value
    numSpaces = len(str(largest))

    for row in board:
        currRow = "|"
        for element in row:
            # if element is 0, add a space
            if element == 0:
                currRow += " " * numSpaces + "|"
                # if not then we should add the value
            else:
                currRow += (" " * (numSpaces - len(str(element)))
                            ) + str(element) + "|"

        # printing the generated row
        print(currRow)
    print()

# Merging one row left


def mergeOneRowL(row):
    # Move everything to left-most
    for j in range(boardSize-1):
        for i in range(boardSize - 1, 0, -1):
            # Check for empty space and if so move over
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0

    # merging everything to the left
    for i in range(boardSize - 1):
        # Testing whether the current value is identical to the next one
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i+1] = 0

    # moving everything to the left
    for i in range(boardSize - 1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    return row

# merging the entire board to the left


def merge_left(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])

    return currentBoard

# reversing the order of a row


def reverse(row):
    # adding all elements of the row to a new list in reversed order
    new = []
    for i in range(boardSize - 1, -1, -1):
        new.append(row[i])
    return new

# merging board right


def merge_right(currentBoard):
    # looking at every row
    for i in range(boardSize):
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])

    return currentBoard

# Transposing the whole board


def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][j]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard

# Merging the board up


def merge_up(currentBoard):
    # Transposes the whole board, merges it all left, then transposes it back
    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard

# Merging the board down


def merge_down(currentBoard):
    # Transposes the whole board, merges it all right, then transposes it back
    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard

# Pick a new value for the board


def pickNewValue():
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2

# Adding a vaule to the board in the empty space


def addNewValue():
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    # Picking spot until an empty space is found
    while not board[rowNum][colNum] == 0:
        rowNum = random.randint(0, boardSize - 1)
        colNum = random.randint(0, boardSize - 1)

    # Filling the empty space with a new value
    board[rowNum][colNum] = pickNewValue()

# Checking if the user has won


def won():
    for row in board:
        if 2048 in row:
            return True
    return False

# Checking if the user has lost


def noMoves():
    # Creating two copies of the board
    tempBoard1 = copy.deepcopy(board)
    tempBoard2 = copy.deepcopy(board)

    # Testing every possible move
    tempBoard1 = merge_down(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_up(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempBoard1 = merge_left(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = merge_right(tempBoard1)
                if tempBoard1 == tempBoard2:
                    return True
    return False


# Creating a blank board
board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

# Filling two spots with the random values, to start the game
numNeeded = 2
while numNeeded > 0:
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numNeeded -= 1

print("Welcome to 2048! Your goal is to combine value to get the number 2048, by merging the board in different directions. Everytime, you will need to type 'd' to merge right, 'w' to merge up, 'a' to merge left, and 's' to merge down. \n\nHere is the staring board:")
display()

gameOver = False

# Asking user for input while the game isn't over
while not gameOver:
    move = input("Which way do you want to merge ? ")

    # Assuming that the user has entered a valid input
    validInput = True

    # Creating a copy of the board
    tempBoard = copy.deepcopy(board)

    # Figuring out which direction the user wants to merge and the correct function to call
    if move == "d":
        board = merge_right(board)
    elif move == "w":
        board = merge_up(board)
    elif move == "a":
        board = merge_left(board)
    elif move == "s":
        board = merge_down(board)
    else:
        validInput = False

    # If the input is not valid, they need to re-enter a new input, and this round will be over
    if not validInput:
        print("Invalid input, please try again")
    # Otherwise their input was valid
    else:
        # Testing if move was unsuccessful
        if board == tempBoard:
            # Telling user to try again
            print("Try a different move!")
        else:
            # Checking if the user has won
            if won():
                display()
                print("You won!")
                gameOver = True
            else:
                # Add a new value
                addNewValue()

            display()

            # Checking if the user has lost
            if noMoves():
                print("Sorry, you have lost!")
                gameOver = True
