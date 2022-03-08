import random

class RandomPlayer():
    
    def __init__(self):
        self.player_number = None

    def set_player_number(self, n):
        self.player_number = n

    def move(self, available_moves):
        return random.choice(available_moves)