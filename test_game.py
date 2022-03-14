import sys
from game import *
from player import *
import time

players = [Player(), Player()]

players[0].set_strategy()
print(players[0].strategy)

num_wins = {0: 0, 1: 0, 2: 0}
num_trials = 1000

for i in range(num_trials):
    
    game = TicTacToe(players, who_goes_first = (i % 2) + 1, do_draw_game = (i == 0))
    game.run_to_completion()
    num_wins[game.winner] += (100 / num_trials)

    if i == 0:
        print(f"\n{game.winner = }")

num_wins = {key:round(value, 5) for key, value in num_wins.items()}
print(f"\n{num_wins = }\n")