from game import *
from player import *

def set_strategies(players):
    for _ in range(25):
        player = Player()
        player.set_strategy()
        players[player] = 0

def have_strategies_fight(players):

    for player_1 in players:
        for player_2 in players:

            if player_1 == player_2: continue

            this_round_players = [player_1, player_2]

            for game_number in [player.player_number for player in this_round_players]:

                game = TicTacToe(this_round_players, who_goes_first=game_number)
                game.run_to_completion()

                if game.winner == '1':
                    players[player_1] += 1
                    players[player_2] -= 1
                
                if game.winner == '2':
                    players[player_1] -= 1
                    players[player_2] += 1

def mate(players):

    new_players = {}

    best_5_players = dict(sorted(players.items(), key=lambda elem: elem[1])).keys()[-5:]

    for player_1 in players:
        for player_2 in players:

            if player_1 == player_2: continue

            this_round_players = [player_1, player_2]

            for offspring_number in [player.player_number for player in this_round_players]:

                offspring = Player()
                offspring.set_strategy()

                for index in offspring.strategy:
                    coin_flip = random.randint(0, 1)
                    offspring.strategy[index] = this_round_players[coin_flip].strategy[index]
                
                new_players[offspring] = 0
    
    return list(new_players)

players = {}

set_strategies(players)

for i in range(15):
    have_strategies_fight(players)
    players = mate(players)