from os import system
from board import Board

def start_game():
    system('cls')
    game_board = Board()
    
    turn = 1
    while game_board.game_over() != True:
        game_board.show()
        player = 'W' if turn % 2 else 'B'
        print ('Player:', player)
        move_from = input('Move From: ')
        move_to = input('Move To: ')
        
        if game_board.update_move(move_from, move_to, player):
            turn += 1

if __name__ == '__main__':
    start_game()