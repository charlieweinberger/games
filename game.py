import math
import itertools

class TicTacToe():

    def __init__(self, players, who_goes_first, do_draw_game=False):
        
        self.players = players
        self.set_player_numbers()

        self.who_goes_first = who_goes_first
        self.who_goes_second = 1 if self.who_goes_first == 2 else 2
        self.do_draw_game = do_draw_game

        self.player_moves = {
            self.who_goes_first: [],
            self.who_goes_second: [],
        }

        self.game_state = [0 for _ in range(9)]

        self.winner = None

    def set_player_numbers(self):
        for i, player in enumerate(self.players):
            player.set_player_number(i + 1)

    def run_to_completion(self):
        while self.winner == None:
            self.complete_round()

    def complete_round(self):

        for player_number in self.player_moves.keys():
            if self.winner == None:

                self.move(player_number)
                self.check_for_winner(player_number)
                
                if self.do_draw_game:
                    self.draw_game()

    def move(self, player_number):
        both_player_moves = self.player_moves[1] + self.player_moves[2]
        available_moves = [move for move in range(9) if move not in both_player_moves]
        move = self.players[player_number - 1].move(available_moves)
        self.player_moves[player_number].append(move)
        self.game_state[move] = player_number

    def check_for_winner(self, player_number):

        player_moves = self.player_moves[player_number]
        # print(f'\nPlayer {player_number}: {player_moves}')
        # print([list(elem) for elem in itertools.combinations(player_moves, 3)])

        for combination in itertools.combinations(player_moves, 3):

            possible_combinations = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]
            ]

            if list(combination) in possible_combinations:
                self.winner = player_number
                return

        if 0 not in self.game_state:
            return 'tie'

    def draw_game(self):
        
        rows = [['-' for _ in range(3)] for _ in range(3)]
        
        for x in self.player_moves[1]:
            rows[math.floor(x / 3)][x % 3] = 'X'

        for x in self.player_moves[2]:
            rows[math.floor(x / 3)][x % 3] = 'O'

        str_row_list = ['', '', '']
        for i in range(3):
            for elem in rows[i]:
                str_row_list[i] += f'{elem} '
        
        print('')
        for elem in str_row_list:
            print(elem)

    # def combinations(self, player_moves):
        
    #     combinations_list = []
                
    #     for move_1 in player_moves:
    #         for move_2 in [move for move in player_moves if move != move_1]:
    #             for move_3 in [move for move in player_moves if move != move_1 and move != move_2]:
                    
    #                 possible_combination = [move_1, move_2, move_3]
    #                 combination_is_original = True
                            
    #                 for combination in combinations_list:
    #                     if sorted(combination) == sorted(possible_combination):
    #                         combination_is_original = False

    #                 if combination_is_original:
    #                     combinations_list.append(possible_combination)
                
    #     return combinations_list