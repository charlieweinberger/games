import random 

class RandomPlayer():
    
    def __init__(self):
        self.player_number = None

    def set_player_number(self, n):
        self.player_number = n

    def move(self, game_state):
        all_coords = [[x, y] for x in range(3) for y in range(3)]
        both_player_coords = game_state['players'][1] + game_state['players'][2]
        free_coords = [coord for coord in all_coords if coord not in both_player_coords]
        return random.choice(free_coords)