from pieces import *

class Board:
    def __init__(self):
        self.size = 10
        self.board = list()
        for i in range(self.size):
            self.board.append(list())
            for _ in range(self.size):
                self.board[i].append(EmptyField('-', [i, _]))
        
        self.create_pieces()

    def create_pieces(self):
        header = 'XABCDEFGHX'
        for i in range(self.size):
            self.board[0][i] = EmptyField(header[i], [0, i])
            self.board[self.size-1][i] = EmptyField(header[i], [i, self.size-1]) 

        for i in range(1, self.size-1, 1):
            self.board[i][0] = EmptyField((self.size -1) - i, [i, 0])
            self.board[i][self.size-1] = EmptyField((self.size -1) - i, [i, self.size-1])
        
        self.board[1][1] = Rook('B', [1, 1])
        self.board[1][8] = Rook('B', [1, 8])
        self.board[8][1] = Rook('W', [8, 1])
        self.board[8][8] = Rook('W', [8, 8])
        self.board[1][2] = Knight('B', [1,2])
        self.board[1][7] = Knight('B', [1,7])
        self.board[8][2] = Knight('W', [8,2])
        self.board[8][7] = Knight('W', [8,8])
        self.board[1][3] = Bishop('B', [1,3])
        self.board[1][6] = Bishop('B', [1,6])
        self.board[8][3] = Bishop('W', [8,3])
        self.board[8][6] = Bishop('W', [8,6])
        self.board[1][4] = Queen('B', [1,4])
        self.board[8][4] = Queen('W', [8,4])
        self.board[1][5] = King('B', [1,5])
        self.board[8][5] = King('W', [8,4])
        
        for i in range(1, self.size-1, 1):
            self.board[2][i] = Pawn('B', [2, i])
            #self.board[5][i] = Pawn('W', [5, i])
  
    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                print (f'{self.board[i][j]}', end ='  ')
            print ('')
        print ('')

    def field_to_array(self, move):
        move_x = move[0]
        move_y = move[1]
        vertical   = ['8', '7', '6', '5', '4', '3', '2', '1']
        horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        x = vertical.index(move_y) + 1
        y = horizontal.index(move_x.lower()) + 1
       
        return [x, y]

    def array_to_field(self, move):
        move_x = move[0]
        move_y = move[1]
        vertical   = ['8', '7', '6', '5', '4', '3', '2', '1']
        horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        x = vertical[move_x - 1]
        y = horizontal[move_y - 1]
       
        return y + x

    def update_move(self, move_from, move_to, player):
        mf = self.field_to_array(move_from)
        mt = self.field_to_array(move_to)

        piece_moves = self.check_move_from(move_from, player)
        board_moves = self.check_move_board(piece_moves, player)
        #kill_moves  = self.check_move_kill(board_moves, player)

        if mt not in board_moves:
            print ('Cannot update the move! Try again...')
            return False
        
        self.board[mt[0]][mt[1]], self.board[mf[0]][mf[1]] = self.board[mf[0]][mf[1]], self.board[mt[0]][mt[1]]
        self.board[mt[0]][mt[1]].update_status(mt)
        return True

    def check_move_from(self, move, player):
        mf = self.field_to_array(move)
        return self.board[mf[0]][mf[1]].possible_moves(mf, player)   

    def check_move_board(self, moves, player):
        type_pieces = (Rook, King, Knight, Queen, Bishop, Pawn)
        out_moves = list()
        kill_moves = list()
        for move in moves:
            for pm in move:
                if isinstance(self.board[pm[0]][pm[1]], type_pieces):
                    if self.board[pm[0]][pm[1]].get_player() != player:
                        kill_moves.append(pm)
                    break
                else:
                    out_moves.append(pm)

        print ('kill moves:', kill_moves) 
        print ('out moves:', out_moves) 
        return out_moves 
    
    def check_move_kill(self, move, player):
        pass 

    def check_move_to(self):
        pass

    def game_over(self):
        return False