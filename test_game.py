import matplotlib.pyplot as plt
plt.style.use('bmh')
from game import *
from player import *

players = {0: [Player() for _ in range(25)]}
scores  = {0: {i:0 for i in range(25)}}

# plot_1 = []
# plot_2 = []
plot_3 = []
plot_4 = []

def have_strategies_fight(i):

    if i == 0:
        for j in range(25):
            players[i][j].id = j

    for player_1 in players[i]:
        for player_2 in players[i]:

            if player_1.id == player_2.id: continue

            for n in [1, 2]:

                game = TicTacToe([player_1, player_2], who_goes_first=n)
                game.run_to_completion()

                if game.winner == 1:
                    scores[i][player_1.id] += 1
                    scores[i][player_2.id] -= 1

                elif game.winner == 2:
                    scores[i][player_1.id] -= 1
                    scores[i][player_2.id] += 1

def select_best(i, selection_method):
    if selection_method == 'hard_cutoff':
        return list(dict(sorted(scores[i].items(), key=lambda elem: elem[1])).keys())[-5:]
    if selection_method == 'tournament':
        best_player_ids = []
        for j in range(5):
            random_3_ids = [random.randint(0, 25) for k in range(3) if k not in best_player_ids]
            # scores_for_random = {k:v for k, v in scores[i].items() if k in random_3_ids}
            scores_for_random = {k:scores[i][k] for k in random_3_ids}
            best_id_of_3 = list(dict(sorted(scores_for_random.items(), key=lambda elem: elem[1])).keys())[-1]
            best_player_ids.append(best_id_of_3)
        return best_player_ids

def mate(i, selection_method):
    
    best_5_player_ids = select_best(i, selection_method)
    best_5_players = [players[i][player_id] for player_id in best_5_player_ids]

    # plot_1.append(fight_another_gen(best_5_players, 0))
    plot_3.append(fight_another_gen(best_5_players, 0))
    # if i != 0: plot_2.append(fight_another_gen(best_5_players, i-1))
    if i != 0: plot_4.append(fight_another_gen(best_5_players, i-1))

    next_gen_players = best_5_players.copy()
    next_gen_scores  = {player.id:0 for player in best_5_players}

    player_id = 5

    for player_1 in best_5_players:
        for player_2 in best_5_players:

            if player_1 == player_2: continue

            offspring = Player()
            offspring.id = player_id
            player_id += 1

            for index in offspring.strategy:
                offspring.strategy[index] = random.choice([player_1, player_2]).strategy[index]
            
            next_gen_players.append(offspring)
            next_gen_scores[offspring.id] = 0
    
    return next_gen_players, next_gen_scores

def fight_another_gen(best_5_players, i):
    
    score = 0

    for player_1 in best_5_players:
        for player_2 in players[i]:

            if player_1.id == player_2.id: continue

            for n in [1, 2]:

                game = TicTacToe([player_1, player_2], who_goes_first=n)
                game.run_to_completion()

                if   game.winner ==   n: score += 1
                elif game.winner == 3-n: score -= 1
    
    return score / 5

def strats_have_converged(i):

    have_converged = True

    for j in range(25):
        for k in range(25):
            if players[i][j].strategy != players[i][k].strategy:
                have_converged = False

    return have_converged

number_of_generations = 20

for i in range(number_of_generations):
    have_strategies_fight(i)
    players[i + 1], scores[i + 1] = mate(i, 'tournament')

plt.figure(3)
plt.plot(list(range(number_of_generations)), plot_3)
plt.xlabel('generation number')
plt.ylabel('tournament selection: score vs 1st generation')
plt.savefig('plot_3.png')

plt.figure(4)
plt.plot(list(range(1, number_of_generations)), plot_4)
plt.xlabel('generation number')
plt.ylabel('tournament selection: score vs previous generation')
plt.savefig('plot_4.png')

# plt.figure(1)
# plt.plot(list(range(number_of_generations)), plot_1)
# plt.xlabel('generation number')
# plt.ylabel('hard cutoff: score vs 1st generation')
# plt.savefig('plot_1.png')

# plt.figure(2)
# plt.plot(list(range(1, number_of_generations)), plot_2)
# plt.xlabel('generation number')
# plt.ylabel('hard cutoff: score vs previous generation')
# plt.savefig('plot_2.png')