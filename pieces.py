class Piece:
    def __init__(self, color, position):
        self.initial = ''
        self.color = color
        self.position = position
        self.moves = list()
        self.possible_moves = list()
        self.moved = False
        self.active = True

    def create_possible_moves(self):
        out_moves = list()
        for direction in self.moves:
            temp = list()
            for move in direction:
                if (move[0]+self.position[0] >= 1 and move[0]+self.position[0] <= 8 and move[1]+self.position[1] >= 1 and move[1]+self.position[1] <= 8):
                    temp.append([move[0]+self.position[0], move[1]+self.position[1]] )
            out_moves.append(temp)
        return out_moves
    
    def get_possible_moves(self):
        return self.possible_moves
    
    def update_status(self, position):
        self.position = position
        self.possible_moves = self.create_possible_moves()
        self.moved = True
    
    def get_position(self):
        return self.position

    def get_player(self):
        return self.color

    def get_moved(self):
        return self.moved

    def get_initial(self):
        return self.initial

    def __str__(self):
        return self.color + self.initial

class EmptyField(Piece):
    def __init__(self, color, position, value):
        super().__init__(color, position)
        self.initial = str(value)
        self.moves = list()
        self.possible_moves = list()
        self.active = False
        
    def __str__(self):
        return self.initial
    
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'K' 
        self.moves = (
                        [[[-1, -1]], [[-1, 0]], [[-1, 1]], 
                        [[0, -1]], [[0, 1]], 
                        [[1, -1]], [[1, 0]], [[1, 1]],
                        [[0, -2]], [[0, 2]]
                        ]
                    )
        self.possible_moves = self.create_possible_moves()
    
    def update_status(self, position):
        self.position = position
        self.moves = (
                        [[[-1, -1]], [[-1, 0]], [[-1, 1]], 
                        [[0, -1]], [[0, 1]], 
                        [[1, -1]], [[1, 0]], [[1, 1]]]
                    )
        self.possible_moves = self.create_possible_moves()
        self.moved = True
    
    def update_moves(self, used):
        if used == 'big':
            self.moves = (
                [[[-1, -1]], [[-1, 0]], [[-1, 1]], 
                [[0, -1]], [[0, 1]], 
                [[1, -1]], [[1, 0]], [[1, 1]],
                [[0, 2]]]
            )
        
        elif used == 'small':
            self.moves = (
                [[[-1, -1]], [[-1, 0]], [[-1, 1]], 
                [[0, -1]], [[0, 1]], 
                [[1, -1]], [[1, 0]], [[1, 1]],
                [[0, -2]]]
            )
        
        self.possible_moves = self.create_possible_moves()

    def set_default_moves(self):
        self.moves = (
            [[[-1, -1]], [[-1, 0]], [[-1, 1]], 
            [[0, -1]], [[0, 1]], 
            [[1, -1]], [[1, 0]], [[1, 1]],
            [[0, -2]], [[0, 2]]])

    def __str__(self):
        return '♔' if self.color == 'W' else '♚'

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'Q' 
        self.moves = (
                [[[i,  0] for i in range(1, 8)]] +
                [[[-i, 0] for i in range(1, 8)]] +
                [[[0,  i] for i in range(1, 8)]] +
                [[[0, -i] for i in range(1, 8)]] + 
                [[[i,   i] for i in range(1, 8)]] + 
                [[[i,  -i] for i in range(1, 8)]] + 
                [[[-i,  i] for i in range(1, 8)]] + 
                [[[-i, -i] for i in range(1, 8)]]
            )
        self.possible_moves = self.create_possible_moves()
    
    def __str__(self):
        return '♕' if self.color == 'W' else '♛'
        

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'R' 
        self.moves = (
            [[[i,  0] for i in range(1, 8)]] +
            [[[-i, 0] for i in range(1, 8)]] +
            [[[0,  i] for i in range(1, 8)]] +
            [[[0, -i] for i in range(1, 8)]]
        )
        self.possible_moves = self.create_possible_moves()

    def __str__(self):
        return '♖' if self.color == 'W' else '♜'
    
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'B' 
        self.moves = (
            [[[i,   i] for i in range(1, 8)]] + 
            [[[i,  -i] for i in range(1, 8)]] + 
            [[[-i,  i] for i in range(1, 8)]] + 
            [[[-i, -i] for i in range(1, 8)]]
        )
        self.possible_moves = self.create_possible_moves()

    def __str__(self):
        return '♗' if self.color == 'W' else '♝'

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'N'
        self.moves = (
            [[[-2, -1]], [[-1, -2]], [[1, -2]], [[2, -1]], [[2, 1]], [[1, 2]], [[-2, 1]]]
        )
        self.possible_moves = self.create_possible_moves()

    def __str__(self):
        return '♘' if self.color == 'W' else '♞'
        
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.initial = 'P'
        if self.color == 'W':
            self.moves = [[[-2, 0]], [[-1, -1]], [[-1, 0]], [[-1, 1]]]
        else:
            self.moves = [[[2, 0]], [[1, 1]], [[1, 0]], [[1, -1]]]
        self.possible_moves = self.create_possible_moves()

    def update_status(self, position):
        self.moved = True
        self.position = position 
        if self.color == 'W':
            self.moves = [[[-1, -1]], [[-1, 0]], [[-1, 1]]]
        else:
            self.moves = [[[1, 1]], [[1, 0]], [[1, -1]]]
        self.possible_moves = self.create_possible_moves()

    def __str__(self):
        return '♙' if self.color == 'W' else '♟'