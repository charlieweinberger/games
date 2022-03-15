from game import *
from player import *

number_of_generations = 15

def have_strategies_fight(info, i):

    for player_1 in info[i]:
        for player_2 in info[i]:

            if player_1 == player_2: continue

            this_round_players = [player_1, player_2]

            for game_number in [player.player_number for player in this_round_players]:

                print('new game')

                game = TicTacToe(this_round_players, who_goes_first=game_number)
                game.run_to_completion()
                
                if game.winner != '0': print(f'{game.winner = }')
                
                if game.winner == '1':
                    info[i][player_1] += 1
                    info[i][player_2] -= 1
                
                if game.winner == '2':
                    info[i][player_1] -= 1
                    info[i][player_2] += 1

def mate(info, i):

    next_gen = {}

    best_5_players = list(dict(sorted(info[i].items(), key=lambda elem: elem[1])).keys())[-5:]

    for player_1 in best_5_players:
        for player_2 in best_5_players:

            if player_1 == player_2: continue

            this_round_players = [player_1, player_2]

            for _ in range(2):

                offspring = Player()

                for index in offspring.strategy:
                    offspring.strategy[index] = random.choice(this_round_players).strategy[index]
                
                next_gen[offspring] = 0
    
    return next_gen

info = {0: {Player() : 0 for _ in range(25)}}

for i in range(number_of_generations):
    print(f'{i = }')
    have_strategies_fight(info, i)
    info[i + 1] = mate(info, i)

print(f'\n{info[0] = }')
print(f'\n{info[14] = }')