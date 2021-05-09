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

    num_p1_wins = 0
    num_p2_wins = 0
    num_ties = 0
    num_trials = 1000

    for i in range(num_trials):
        
        game = TicTacToe(players, who_goes_first = (i % 2) + 1, do_draw_game = (i == 0))
        game.run_to_completion()
    
        num_p1_wins += int(game.winner == 1)
        num_p2_wins += int(game.winner == 2)
        num_ties += int(game.winner == 'tie')

    print("\np1 win %:", 100 * num_p1_wins / num_trials)
    print("p2 win %:", 100 * num_p2_wins / num_trials)
    print("tie %:", 100 * num_ties / num_trials)

else:

    game = Game(players, who_goes_first = 1, do_draw_game = True)
    game.run_to_completion()