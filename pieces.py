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

    def possible_moves(self, position, player):
        return list()
    
    def update_status(self, position):
        pass
    
    def get_player(self):
        return self.color

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
        #self.moves = (
        #    [[i,  0] for i in range(1, 8)] +
        #    [[-i, 0] for i in range(1, 8)] +
        #    [[0,  i] for i in range(1, 8)] +
        #    [[0, -i] for i in range(1, 8)]
        #    )

        self.moves = (
            [[[i,  0] for i in range(1, 8)]] +
            [[[-i, 0] for i in range(1, 8)]] +
            [[[0,  i] for i in range(1, 8)]] +
            [[[0, -i] for i in range(1, 8)]]
            )
    

    def possible_moves(self, position, player):
        if self.color != player:
            print ('Log: Do not touch the pawn - it is not your\'s piece')
            return list()
    
        out_moves = list()
        for test in self.moves:
            temp = list()
            for move in test: 
                if (move[0]+position[0] >= 1 and move[0]+position[0] <= 8 and move[1]+position[1] >= 1 and move[1]+position[1] <= 8):
                    temp.append([move[0]+position[0], move[1]+position[1]])
            out_moves.append(temp)
        
        return out_moves

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
        if self.color == 'W':
            self.moves = [[-2, 0], [-1, -1], [-1, 0], [-1, 1]]
        else:
            self.moves = [[2, 0], [1, 1], [1, 0], [1, -1]]

    def update_status(self, position):
        self.moved = True
        self.position = position 
        if self.color == 'W':
            self.moves = [[-1, -1], [-1, 0], [-1, 1]]
        else:
            self.moves = [[1, 1], [1, 0], [1, -1]]

    def possible_moves(self, position, player):
        if self.color != player:
            print ('Log: Do not touch the pawn - it is not your\'s piece')
            return list()

        #out_moves = list()
        #for direction in self.moves:
        #    for move in direction:
        #        if (move[0]+position[0] >= 1 and move[0]+position[0] <= 8 and move[1]+position[1] >= 1 and move[1]+position[1] <= 8):
        #            out_moves.append([move[0]+position[0], move[1]+position[1]] )
        
        return []
        #print (out_moves)
        #return out_moves

    def get_player(self):
        return self.color