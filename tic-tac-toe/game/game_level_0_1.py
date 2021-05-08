import itertools
import random

class Game():

    def __init__(self, players, who_goes_first, do_draw_game=False):
        
        self.players = players
        self.set_player_numbers()

        self.who_goes_first = who_goes_first
        self.who_goes_second = 1 if self.who_goes_first == 2 else 2
        self.do_draw_game = do_draw_game

        self.state = {
            'turn': 1,
            'players': {
                self.who_goes_first: [],
                self.who_goes_second: [],
            },
            'winner': None
        } 

    def set_player_numbers(self):
        for i, player in enumerate(self.players):
            player.set_player_number(i + 1)

    def player_move(self, player_number):
        
        if self.state['winner'] == None:
            
            move = self.players[player_number - 1].move(self.state)
            self.state['players'][player_number].append(move)
            
            if self.do_draw_game:
                self.draw_game()

            self.check_if_player_won(player_number)
            
            if self.do_draw_game:
                print("\ngame.state['winner']:", self.state['winner'])

    def run_to_completion(self):
        while self.state['winner'] == None:
            self.player_move(self.who_goes_first)
            self.player_move(self.who_goes_second)
            self.state['turn'] += 1

    def check_if_player_won(self, player_number):
        
        player_wins = False
        player_coords = self.state['players'][player_number]
        
        if len(player_coords) > 2:

            for combination in itertools.combinations(player_coords, 3):
                
                xs = [elem[0] for elem in combination]
                ys = [elem[1] for elem in combination]

                if len(set(xs)) == 1 or len(set(ys)) == 1:
                    player_wins = True
                    break
                
                left_to_right_diagonal = [x == y for x, y in combination]
                right_to_left_diagonal = [x == 2 - y for x, y in combination]

                if all(left_to_right_diagonal) or all(right_to_left_diagonal):
                    player_wins = True
                    break
        
            if player_wins:
                self.state['winner'] = player_number
        
            total_num_coords = self.state['players'][self.who_goes_first] + self.state['players'][self.who_goes_second]
            if not player_wins and len(total_num_coords) == 9:
                self.state['winner'] = 'tie'
    
    def draw_game(self):
        
        rows = [['-' for _ in range(3)] for _ in range(3)]
        
        for x, y in self.state['players'][1]:
            rows[x][y] = 'X'
        
        for x, y in self.state['players'][2]:
            rows[x][y] = 'O'

        str_row_list = ['', '', '']
        for i in range(3):
            for elem in rows[i]:
                str_row_list[i] += str(elem) + ' '
        
        print('\n' + str_row_list[0] + '\n' + str_row_list[1] + '\n' + str_row_list[2])