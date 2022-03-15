import random

class Player():
    
    def __init__(self):
        self.player_number = None
        self.strategy = {}

    def set_player_number(self, n):
        self.player_number = n

    def move(self, game_state):
        # available_moves = [elem for elem in range(9) if game_state[elem] == 0]
        # return random.choice(available_moves)
        return self.strategy[game_state]

    def set_strategy(self):

        n = ['0', '1', '2']
        equal = lambda x, y, z: x == y and y == z and x == z

        for a in n:
            for b in n:
                for c in n:
                    if not equal(a, b, c):
                        for d in n:
                            for e in n:
                                for f in n:
                                    if not equal(d, e, f):
                                        for g in n:
                                            if not equal(c, e, g) and not equal(a, d, g):
                                                for h in n:
                                                    if not equal(b, e, h):
                                                        for i in n:
                                                            if not equal(g, h, i) and not equal(c, f, i) and not equal(a, e, i):
                                                                key = f'{a}{b}{c}{d}{e}{f}{g}{h}{i}'
                                                                self.strategy[key] = random.randint(0, 8)