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

def gen_i_vs_j(info, i, j):

    scores = []

    for player_1 in info[i]:

        score = 0

        for player_2 in info[j]:

            if player_1 == player_2: continue

            this_round_players = [player_1, player_2]

            for n in [1, 2]:

                game = TicTacToe(this_round_players, who_goes_first=n)
                game.run_to_completion()

                if   game.winner == '1': score -= 1
                elif game.winner == '2': score += 1

        scores.append(score)

    return scores

# code

info = {0: {Player() : 0 for _ in range(25)}}

number_of_generations = 25

plots = {
    # 'gen 0 vs gen i': []
    'gen i-1 vs gen i': []
}

for i in range(number_of_generations):
    
    have_strategies_fight(info, i)

    # plot_1 = gen_i_vs_j(info, 0, i)
    # plots['gen 0 vs gen i'].append(sum(plot_1) / len(plot_1))

    if i != 0:
        plot_2 = gen_i_vs_j(info, i-1, i)
        plots['gen i-1 vs gen i'].append(sum(plot_2) / len(plot_2))
    
    info[i + 1] = mate(info, i)

# plotting

import matplotlib.pyplot as plt
plt.style.use('bmh')

# plt.figure(1)
# plt.plot(list(range(number_of_generations)), plots['gen 0 vs gen i'])
# plt.xlabel('generation number')
# plt.ylabel('score vs 1st generation')
# plt.savefig('plot_1.png')

# plt.figure(2)
plt.plot(list(range(1, number_of_generations)), plots['gen i-1 vs gen i'])
plt.xlabel('generation number')
plt.ylabel('score vs previous generation')
plt.savefig('plot_3.png')