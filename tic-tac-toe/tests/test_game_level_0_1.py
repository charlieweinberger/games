import sys
sys.path.append('tic-tac-toe/game')
from game_level_0_1 import *
sys.path.append('tic-tac-toe/players')
from random_player import *
from input_player import *

# python tic-tac-toe/tests/test_game_level_0_1.py

game_options = ['random vs random', 'player vs random', 'random vs player', 'player vs player']
game_type = game_options[0] # choose here
players = [RandomPlayer() if elem == 'random' else InputPlayer() for elem in game_type.split(' vs ')]

if game_type == 'random vs random':

    num_wins = {1: 0, 2: 0, 'tie': 0}
    num_trials = 1000

    for i in range(num_trials):
        
        game = TicTacToe(players, who_goes_first = (i % 2) + 1, do_draw_game = (i == 0))
        game.run_to_completion()
        num_wins[game.winner] += (100 / num_trials)

        if i == 0:
            print("\ngame.winner:", game.winner)

    num_wins = {key:round(value, 2) for key, value in num_wins.items()}
    print("\nnum_wins:", num_wins)

else:

    game = TicTacToe(players, who_goes_first = 1, do_draw_game = True)
    game.run_to_completion()
    print("\ngame.winner:", game.winner)