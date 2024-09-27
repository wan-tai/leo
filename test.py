import pandas
import numpy
import matplotlib

print("Hello World")

# change working directory
import os
os.chdir("/home/chingfang/code")

# wite a script for tic tac toe
import numpy as np
import random

def create_board():
    return np.zeros((3,3))

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    return board

def possibilities(board):
    return list(zip(*np.where(board==0)))

def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
    return board

def row_win(board, player):
    return np.any(np.all(board==player, axis=1))

def col_win(board, player):
    return np.any(np.all(board==player, axis=0))

def diag_win(board, player):
    return np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player)

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():

    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

results = [play_game() for i in range(1000)]
results.count(1)
results.count(2)
results.count(-1)

#run the game   
play_game()
