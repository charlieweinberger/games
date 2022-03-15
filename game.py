import math

class TicTacToe():

    def __init__(self, players, who_goes_first=1, do_draw_game=False):
        
        self.players = players
        self.player_order = [1 if who_goes_first == 2 else 2]
        self.set_player_numbers()

        self.do_draw_game = do_draw_game
        
        self.game_state = '000000000'
        
        self.winner = None

    def set_player_numbers(self):
        for i, player in enumerate(self.players):
            player.set_player_number(i + 1)

    def run_to_completion(self):
       
        while self.winner == None: 
            
            for player_number in self.player_order:

                if self.winner == None:

                    self.move(player_number)
                    self.winner = self.check_for_winner()

                    # if self.do_draw_game:
                        # self.draw_game()
                    
    def move(self, player_number):
        move = self.players[player_number - 1].move(self.game_state)

        print(f'\n{move = }')
        print(f'before {self.game_state = }')

        game_state_copy = list(self.game_state)
        game_state_copy[move] = str(player_number)

        self.game_state = ''
        for elem in game_state_copy:
            self.game_state += elem
        
        print(f'after  {self.game_state = }')
        
    def check_for_winner(self):

        winning_options = [
            [self.game_state[0], self.game_state[1], self.game_state[2]],
            [self.game_state[3], self.game_state[4], self.game_state[5]],
            [self.game_state[6], self.game_state[7], self.game_state[8]],
            [self.game_state[0], self.game_state[3], self.game_state[6]],
            [self.game_state[1], self.game_state[4], self.game_state[7]],
            [self.game_state[2], self.game_state[5], self.game_state[8]],
            [self.game_state[0], self.game_state[4], self.game_state[8]],
            [self.game_state[2], self.game_state[4], self.game_state[6]],
        ]

        for arr in winning_options:
            if arr[0] == arr[1] and arr[1] == arr[2] and arr[0] == arr[2] and arr[0] != '0':
                return arr[0]

        if '0' not in self.game_state:
            return '0'

    def draw_game(self):
        
        rows = [0 for _ in range(9)]

        for key in self.player_order:
            for index, x in enumerate(self.game_state):
                if int(x) == key:
                    rows[index] = key
        
        print(f'\n{rows[0]} {rows[1]} {rows[2]}')
        print(f'{rows[3]} {rows[4]} {rows[5]}')
        print(f'{rows[6]} {rows[7]} {rows[8]}')