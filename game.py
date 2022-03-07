class TicTacToe():

    def __init__(self, players, who_goes_first, do_draw_game=False):
        
        self.players = players
        self.set_player_numbers()

        self.who_goes_first = who_goes_first
        self.who_goes_second = 1 if self.who_goes_first == 2 else 2
        self.do_draw_game = do_draw_game

        self.player_coords = {
                                self.who_goes_first: [],
                                self.who_goes_second: [],
                             }

        self.winner = None

    def set_player_numbers(self):
        for i, player in enumerate(self.players):
            player.set_player_number(i + 1)

    def run_to_completion(self):
        while self.winner == None:
            self.complete_round()

    def complete_round(self):

        for player_number in self.player_coords.keys():
            if self.winner == None:

                self.player_move(player_number)
                self.check_if_player_won(player_number)
                
                if self.do_draw_game:
                    self.draw_game()

    def player_move(self, player_number):
        
        all_coords = [[x, y] for x in range(3) for y in range(3)]
        both_player_coords = self.player_coords[1] + self.player_coords[2]
        free_coords = [coord for coord in all_coords if coord not in both_player_coords]

        move = self.players[player_number - 1].move(free_coords)
        self.player_coords[player_number].append(move)

    def check_if_player_won(self, player_number):

        player_coords = self.player_coords[player_number]

        if len(player_coords) > 2:
                
            for combination in self.combinations(player_coords):
                    
                xs = [elem[0] for elem in combination]
                ys = [elem[1] for elem in combination]

                if len(set(xs)) == 1 or len(set(ys)) == 1:
                    self.winner = player_number
                    return
                    
                left_to_right_diagonal = [x == y for x, y in combination]
                right_to_left_diagonal = [x == 2 - y for x, y in combination]

                if all(left_to_right_diagonal) or all(right_to_left_diagonal):
                    self.winner = player_number
                    return
        
            total_num_coords = self.player_coords[self.who_goes_first] + self.player_coords[self.who_goes_second]
            if len(total_num_coords) == 9:
                self.winner = 'tie'
                return

    def draw_game(self):
        
        rows = [['-' for _ in range(3)] for _ in range(3)]
        
        for x, y in self.player_coords[1]:
            rows[y][x] = 'X'
        
        for x, y in self.player_coords[2]:
            rows[y][x] = 'O'

        str_row_list = ['', '', '']
        for i in range(3):
            for elem in rows[i]:
                str_row_list[i] += str(elem) + ' '
        
        print('')
        print(str_row_list[0])
        print(str_row_list[1])
        print(str_row_list[2])

    def combinations(self, player_coords):
        
        combinations_list = []
                
        for coord1 in player_coords:
            for coord2 in [coord for coord in player_coords if coord != coord1]:
                for coord3 in [coord for coord in player_coords if coord != coord1 and coord != coord2]:
                    
                    possible_combination = [coord1, coord2, coord3]
                    combination_is_original = True
                            
                    for combination in combinations_list:
                        if sorted(combination) == sorted(possible_combination):
                            combination_is_original = False

                    if combination_is_original:
                        combinations_list.append(possible_combination)
                
        return combinations_list