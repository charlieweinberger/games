import matplotlib.pyplot as plt
plt.style.use('bmh')
from game import *
from player import *

# made line 10 like line 9, aka get the top 5 players by score. the 2nd bracket (the empty one) in line 10 should be the player id, which you get using the scores dict.

# info = {0: {Player() : 0 for _ in range(25)}}
# dict(sorted(info[i].items(), key=lambda elem: elem[1])).keys()
# players[i][][-5:]

players = {0: [Player() for _ in range(25)]}
scores  = {0: {i:0 for i in range(25)}}

plot_1 = []
plot_2 = []

def set_player_id(i):
    for j in range(25):
        players[i][iden].id = j

def have_strategies_fight(i):

    set_player_id(i)
    if i == 0: print([player.id for player in players[0]])

    for player_1 in players[i]:
        for player_2 in players[i]:

            if player_1.id == player_2.id: continue

            for n in [1, 2]:

                game = TicTacToe([player_1, player_2], who_goes_first=n)
                game.run_to_completion()

                if game.winner == 1:
                    info[i][player_1.id] += 1
                    info[i][player_2.id] -= 1

                elif game.winner == 2:
                    info[i][player_1.id] -= 1
                    info[i][player_2.id] += 1

def mate(i):

    best_5_players = list(dict(sorted(info[i].items(), key=lambda elem: elem[1])).keys())[-5:]

    plot_1.append(fight_another_gen(best_5_players, 0))
    if i != 0:
        plot_2.append(fight_another_gen(best_5_players, i-1))

    next_gen = {player:0 for player in best_5_players}

    for player_1 in best_5_players:
        for player_2 in [elem for elem in best_5_players if elem != player_1]:

            offspring = Player()

            for index in offspring.strategy:
                offspring.strategy[index] = random.choice([player_1, player_2]).strategy[index]
                
            next_gen[offspring] = 0
    
    return next_gen

def fight_another_gen(best_5_players, i):
    
    score = 0

    for player_1 in best_5_players:

        for player_2 in info[i]:

            if player_1 == player_2: continue

            this_round_players = [player_1, player_2]

            for n in [1, 2]:

                game = TicTacToe(this_round_players, who_goes_first=n)
                game.run_to_completion()

                if   game.winner ==   n: score += 1
                elif game.winner == 3-n: score -= 1
    
    return score / 5

number_of_generations = 25

for i in range(number_of_generations):
    have_strategies_fight(i)
    info[i + 1] = mate(i)

# plt.figure(1)
# plt.plot(list(range(number_of_generations)), plot_1)
# plt.xlabel('generation number')
# plt.ylabel('score vs 1st generation')
# plt.savefig('plot_1.png')

# plt.figure(2)
plt.plot(list(range(1, number_of_generations)), plot_2)
plt.xlabel('generation number')
plt.ylabel('score vs previous generation')
plt.savefig('plot_2.png')