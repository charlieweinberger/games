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

    def player_move(self, player_number):
        
        if self.winner == None:

            move = self.players[player_number - 1].move(self.player_coords)
            self.player_coords[player_number].append(move)
            
            if self.do_draw_game:
                self.draw_game()

            self.check_if_player_won(player_number)
            
            if self.do_draw_game:
                print("\nself.winner:", self.winner)

    def check_if_player_won(self, player_number):
        
        player_wins = False
        player_coords = self.player_coords[player_number]
        
        if len(player_coords) > 2:
            
            for combination in self.combinations(player_coords):
                
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
                self.winner = player_number
        
            total_num_coords = self.player_coords[self.who_goes_first] + self.player_coords[self.who_goes_second]
            if not player_wins and len(total_num_coords) == 9:
                self.winner = 'tie'
    
    def combinations(self, input_list):
        
        combinations_list = []
                
        for elem1 in input_list:
            for elem2 in [elem for elem in input_list if elem != elem1]:
                for elem3 in [elem for elem in input_list if elem != elem1 and elem != elem2]:
                    
                    possible_combination = [elem1, elem2, elem3]
                    combination_is_original = True
                            
                    for combination in combinations_list:
                        if sorted(combination) == sorted(possible_combination):
                            combination_is_original = False

                    if combination_is_original:
                        combinations_list.append(possible_combination)
                
        return combinations_list

    def run_to_completion(self):
        while self.winner == None:
            self.player_move(self.who_goes_first)
            self.player_move(self.who_goes_second)

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
        
        print('\n' + str_row_list[0] + '\n' + str_row_list[1] + '\n' + str_row_list[2])