import random

class Player():
    
    def __init__(self):
        self.player_number = None
        self.strategy = self.set_strategy()

    def set_player_number(self, n):
        self.player_number = n

    def move(self, game_state):
        return self.strategy[game_state]

    def set_strategy(self):

        n = ['0', '1', '2']
        test = lambda x, y, z: x != y or y != z or x != z or x == '0' or y == '0' or z == '0'

        strategy = {}

        for a in n:
            for b in n:
                for c in n:
                    if test(a, b, c):
                        for d in n:
                            for e in n:
                                for f in n:
                                    if test(d, e, f):
                                        for g in n:
                                            if test(c, e, g) and test(a, d, g):
                                                for h in n:
                                                    if test(b, e, h):
                                                        for i in n:
                                                            if test(g, h, i) and test(c, f, i) and test(a, e, i):
                                                                key = f'{a}{b}{c}{d}{e}{f}{g}{h}{i}'
                                                                strategy[key] = random.randint(0, 8)
        
        return strategy