from os import system
from termcolor import colored
from board import Board
from pieces import *

def start_game():
    system('cls')
    game_board = Board()
    
    turn = 1
    while game_board.game_over() != True:
        game_board.show()
        player = 'W' if turn % 2 else 'B'
        if player == 'W':
            print (colored('WHITE', 'yellow'), 'TURN')
        else:
            print (colored('BLACK', 'red'), 'TURN')
        from_move   = input('ENTER MOVE FROM: ')
        to_move     = input('ENTER MOVE TO: ')
        
        if game_board.update_move(from_move, to_move, player):
            turn += 1

if __name__ == '__main__':
    start_game()