from game import *
from player import *

def have_strategies_fight(info, i):

    for player_1 in info[i]:
        for player_2 in info[i]:

            if player_1 == player_2: continue

            this_round_players = [player_1, player_2]

            for n in [1, 2]:

                game = TicTacToe(this_round_players, who_goes_first=n)
                game.run_to_completion()

                if game.winner == '1':
                    info[i][player_1] += 1
                    info[i][player_2] -= 1

                elif game.winner == '2':
                    info[i][player_1] -= 1
                    info[i][player_2] += 1

def mate(info, i):

    best_5_players = list(dict(sorted(info[i].items(), key=lambda elem: elem[1])).keys())[-5:]

    next_gen = {player:0 for player in best_5_players}

    for player_1 in best_5_players:
        for player_2 in best_5_players:

            if player_1 == player_2: continue

            offspring = Player()

            for index in offspring.strategy:
                offspring.strategy[index] = random.choice([player_1, player_2]).strategy[index]
                
            next_gen[offspring] = 0
    
    return next_gen

info = {0: {Player() : 0 for _ in range(25)}}

number_of_generations = 15

for i in range(number_of_generations):
    print(f'\n{i = }')
    have_strategies_fight(info, i)
    info[i + 1] = mate(info, i)

    print(list(info[i].values()))
    print(sorted(list(info[i].values())))

import matplotlib as plt