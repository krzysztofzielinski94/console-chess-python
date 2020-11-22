class Piece:
    def __init__(self, color, position):
        self.initial = ''
        self.status = 'active'
        self.color = color
        self.position = position

    def move(self):
        pass 

    def kill(self):
        pass

    def small_castle(self):
        pass 
    
    def big_castle(self):
        pass

    def can_move(self, lp, np, color):
        return True

    def possible_moves(self, position):
        return '0'

    def __str__(self):
        return self.color + self.initial 

class EmptyField(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = ' '
        self.status = 'disabled'

    def possible_moves(self, position, player):
        print ('Log: no possible moves')
        return None
    
    def __str__(self):
        return self.initial + str(self.color)
    
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'K' 

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'Q' 

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'R' 

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'B' 

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'N' 

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'P'
        self.moved = False
        self.move_left_up = [-1, 0]
        self.move_up = []

    def can_move(self, last_position, new_position, player):
        if self.color != player:
            return False
        if self.color == 'W':
            if (last_position[0] - 1 == new_position[0] and last_position[1] == new_position[1]):
                self.moved = True
                return True
            elif (last_position[0] - 2 == new_position[0] and last_position[1] == new_position[1] and self.moved == False):
                self.moved = True
                return True

        if self.color == 'B':
            if (last_position[0] + 1 == new_position[0] and last_position[1] == new_position[1]):
                self.moved = True
                return True
            elif (last_position[0] + 2 == new_position[0] and last_position[1] == new_position[1] and self.moved == False):
                self.moved = True
                return True
                 
        return False

    def possible_moves(self, position, player):
        if self.color != player:
            print ('Log: Do not touch the pawn - it is not your\'s piece')
            return None
        return ['a2','g5']

    
    
