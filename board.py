from pieces import Rook, King, Knight, Queen, Bishop, Pawn, EmptyField
from termcolor import colored

class Board:
    def __init__(self):
        self.size = 10
        self.board = list()
        self.game_over = False
        for i in range(self.size):
            self.board.append(list())
            for _ in range(self.size):
                self.board[i].append(EmptyField('None', [i, _], '-'))
    
        self.create_pieces()

    def create_pieces(self):
        header = 'XABCDEFGHX'
        for i in range(self.size):
            self.board[0][i] = EmptyField('None', [0, i], header[i])
            self.board[self.size-1][i] = EmptyField('None', [i, self.size-1], header[i]) 

        for i in range(1, self.size-1, 1):
            self.board[i][0] = EmptyField('None', [i, 0], (self.size -1) - i)
            self.board[i][self.size-1] = EmptyField('None', [i, self.size-1], (self.size -1) - i)
        
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
        self.board[8][3] = Queen('W', [8,3])
        self.board[1][5] = King('B', [1,5])
        self.board[1][4] = King('B', [1,4])
        self.board[8][5] = King('W', [8,5])
        
        for i in range(1, self.size-1, 1):
            self.board[2][i] = Pawn('B', [2, i])
            self.board[7][i] = Pawn('W', [7, i])

        # Only for testing purposes 
        #self.board[3][3] = Bishop('W', [3,3])
        #self.board[3][5] = Bishop('W', [3,5])
        #self.board[8][3] = Queen('W', [8,3])
        #self.board[1][4] = King('B', [1,4])
        #self.board[8][5] = King('W', [8,5])


    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].get_player() == 'W':
                    print (colored(f'{self.board[i][j]}', 'yellow'), end ='  ')
                elif self.board[i][j].get_player() == 'B':
                    print (colored(f'{self.board[i][j]}', 'red'), end ='  ')
                else:
                    print (colored(f'{self.board[i][j]}', 'white'), end ='  ')
            print ('')
        print ('')

    def field_to_array(self, move):
        move_x = move[0]
        move_y = move[1]
        vertical   = ['8', '7', '6', '5', '4', '3', '2', '1']
        horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        if move_y not in vertical or move_x.lower() not in horizontal:
            return [0, 0]

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

    def is_check_mate(self, player, enemy_player):
        nk_moves = self.get_pieces_possible_and_kill_moves(player)
        neutral_moves = nk_moves['neutral_moves']
        killing_moves = nk_moves['killing_moves']

        check_mate = True
        for nm in neutral_moves:
            for m in nm:
                check_mate *= self.is_check(player, enemy_player, m)

        for km in killing_moves:
            for m in km:
                check_mate *= self.is_check(player, enemy_player, m)

        return check_mate


    def is_check(self, player, enemy_player, piece_position=None):
        e_nk_moves = self.get_pieces_possible_and_kill_moves(enemy_player, piece_position)
        e_neutral_moves = e_nk_moves['neutral_moves']
        e_killing_moves = e_nk_moves['killing_moves']
        
        if piece_position == None:
            my_piece = self.get_piece(King, player)
            piece_position = my_piece.get_position()

        #print (e_killing_moves)
        #print (e_neutral_moves)
        #print (piece_position)

        check = False
        for k in e_killing_moves:
            if piece_position in k:
                check = True
                break

        for nm in e_neutral_moves:
            if piece_position in nm:
                check = True
                break

        print ('Check', check)
        return check
  

    def update_piece_position(self, move_from, move_to, player, enemy_player):
        mf = self.field_to_array(move_from)
        mt = self.field_to_array(move_to)

        piece_moves   = self.get_piece_moves(self.board[mf[0]][mf[1]])
        nk_moves      = self.get_piece_possible_and_kill_moves(piece_moves, player)
        neutral_moves = nk_moves['neutral_moves']
        killing_moves = nk_moves['killing_moves']
        
        # For Logging purposes!
        #print ('[Log: All Possible Piece Moves]', piece_moves)
        #print ('[Log: Piece Moves]', neutral_moves)
        #print ('[Log: Kill Moves]', kill_moves)
        #print ('[Log: Move To]', mt)

        if (mt not in neutral_moves) and (mt not in killing_moves):
            print ('Cannot update the move! Try again...')
            return False
        elif mt in neutral_moves:
            self.board[mt[0]][mt[1]], self.board[mf[0]][mf[1]] = self.board[mf[0]][mf[1]], self.board[mt[0]][mt[1]]
        elif mt in killing_moves:
            empty_field =  EmptyField('None', [mf[0], mf[1]], '-')
            # simple end game
            if isinstance(self.board[mt[0]][mt[1]], King):
                self.game_over = True
            self.board[mt[0]][mt[1]], self.board[mf[0]][mf[1]] = self.board[mf[0]][mf[1]], empty_field
        
        self.board[mt[0]][mt[1]].update_status(mt)
        return True

    def get_piece(self, piece_type, player):
        for i in range(self.size):
            for j in range(self.size):
                if isinstance(self.board[i][j], piece_type):
                    if self.board[i][j].get_player() == player:
                        return self.board[i][j]
        return None

    def get_pieces(self, player):
        pieces = list()
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].get_player() == player:
                    pieces.append(self.board[i][j])
        return pieces

    def get_piece_moves(self, piece):
        return piece.get_possible_moves()   

    def get_pieces_moves(self, pieces):
        pieces_moves = list()
        for piece in pieces:
            pieces_moves.append(piece.get_possible_moves())
        return pieces_moves

    def get_piece_possible_and_kill_moves(self, moves, player, special_move=None):
        pieces_type = (Rook, King, Knight, Queen, Bishop, Pawn)
        neutral_moves = list()
        kill_moves = list()
        for move in moves:
            for pm in move:
                if pm == special_move:
                    kill_moves.append(pm)
                elif isinstance(self.board[pm[0]][pm[1]], pieces_type):
                    if self.board[pm[0]][pm[1]].get_player() != player:
                        kill_moves.append(pm)
                    break
                else:
                    if (pm != []):
                        neutral_moves.append(pm)

        piece_possible_and_kill_moves = dict()
        piece_possible_and_kill_moves['neutral_moves'] = neutral_moves
        piece_possible_and_kill_moves['killing_moves'] = kill_moves
        return piece_possible_and_kill_moves

    def get_pieces_possible_and_kill_moves(self, player, special_position=None):
        pieces = self.get_pieces(player)
        pieces_moves = self.get_pieces_moves(pieces)
        pieces_possible_and_kill_moves = dict()
        piece_neutral_moves = list()
        piece_kill_moves = list()
        
        for moves in pieces_moves:
            temp_move = self.get_piece_possible_and_kill_moves(moves, player, special_position)
            piece_neutral_moves.append(temp_move['neutral_moves'])
            piece_kill_moves.append(temp_move['killing_moves'])    
        
        pieces_possible_and_kill_moves['neutral_moves'] = piece_neutral_moves
        pieces_possible_and_kill_moves['killing_moves'] = piece_kill_moves
        
        return pieces_possible_and_kill_moves

    def get_board_status(self):
        return self.game_over