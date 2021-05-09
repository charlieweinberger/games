class InputPlayer():
    
    def __init__(self):
        self.player_number = None

    def set_player_number(self, n):
        self.player_number = n

    def move(self, player_coords):
        
        move = 'before input'

        while not self.is_move_valid(move, player_coords):
            
            if move == 'before input':
                move = input("\nYour move: ")
            else:
                print("that move is not valid")
                move = input("Your move: ")
            
            for character in ", ":
                move = move.replace(character, "")
        
            move = [int(elem) for elem in move]
        
        return move

    def is_move_valid(self, move, player_coords):
        
        if move == 'before input':
            return False
        
        for elem in move:
            if elem not in [0, 1, 2]:
                return False
        
        all_coords = [[x, y] for x in range(3) for y in range(3)]
        both_player_coords = player_coords[1] + player_coords[2]
        free_coords = [coord for coord in all_coords if coord not in both_player_coords]

        return move in free_coords