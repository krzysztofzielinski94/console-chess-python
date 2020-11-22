from os import system
from board import Board

def start_game():
    system('cls')
    b = Board()
    b.show()

    turn = 1
    while b.game_over() != True:
        player = 'W' if turn % 2 else 'B'
        print ('Player:', player)
        # check move from 
        move_from = input('Move From: ')
        if b.check_move_from(move_from, player) == False:
            continue
        
        # check move to 
        move_to = input('Move To: ')
        
        if b.update_move(move_from, move_to, player):
            turn += 1
        
        #system('cls')
        b.show()



if __name__ == '__main__':
    start_game()
    #b = Board()
    #print (b.array_to_field([0, 0]))