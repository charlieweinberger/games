import sys
sys.path.append('tic-tac-toe/game')
from game_level_0_1 import *
sys.path.append('tic-tac-toe/players')
from random_player import *

players = [RandomPlayer(), RandomPlayer()]

num_p1_wins = 0
num_p2_wins = 0
num_ties = 0
num_trials = 1000

for i in range(num_trials):
    
    game = Game(players.copy(), who_goes_first = (i % 2) + 1, do_draw_game = (i == 0))
    game.run_to_completion()
    
    winner = game.state['winner']
    if winner == 1:
        num_p1_wins += 1
    elif winner == 2:
        num_p2_wins += 1
    elif winner == 'tie':
        num_ties += 1

print("\np1 win %:", 100 * num_p1_wins / num_trials)
print("p2 win %:", 100 * num_p2_wins / num_trials)
print("tie %:", 100 * num_ties / num_trials)
