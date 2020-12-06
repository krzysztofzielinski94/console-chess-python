from os import system
from termcolor import colored
from board import Board

class Game:
    def __init__(self):
        system('cls')
        self.board_game = Board()
        self.start_game()

    def start_game(self):
        turn = 1
        while self.end_game() != True:
            
            self.board_game.show()
            player = 'W' if turn % 2 else 'B'
            if player == 'W':
                print (colored('WHITE', 'yellow'), 'TURN')
            else:
                print (colored('BLACK', 'red'), 'TURN')
            from_move   = input('ENTER MOVE FROM: ')
            to_move     = input('ENTER MOVE TO: ')

            if (len(from_move) != 2) or (len(to_move) != 2):
                print ('Cannot update the move! Try again...')
                continue

            if self.board_game.update_piece_position(from_move, to_move, player):
                turn += 1

    def end_game(self):
        return self.board_game.get_board_status()

if __name__ == '__main__':
    game = Game()
    