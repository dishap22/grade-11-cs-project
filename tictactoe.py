import random 

def print_game_board(game_board):
    for i in range(3):
        print(game_board[i])

game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
print_game_board(game_board)
user = input()