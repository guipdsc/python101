from gameplay import *
import os
from time import sleep


def play(player, computer):
    win = player.show_winner(computer)
    my_hand = player.show_play()
    pc_hand = computer.show_play()
    if win == 'W':
        print(f'You won!!! Your hand ({my_hand}) is stronger then the computers ({pc_hand})')
        sleep(3) # Waiting for 4 seconds to clear the screen
        os.system('clear') # Clearing the Screen
    elif win == 'L':
        print(f'You lost!!!')
        sleep(3) # Waiting for 4 seconds to clear the screen
        os.system('clear') # Clearing the Screen
    else:
        print(f'You draw!!!')
        sleep(3) # Waiting for 4 seconds to clear the screen
        os.system('clear') # Clearing the Screen

def instructions():
    print("\nWinning Rules of the Rock paper scissor game as follows: \n"
                                    +"rock vs paper->paper wins \n"
                                    + "rock vs scissor->rock wins \n"
                                    +"paper vs scissor->scissor wins \n")
    sleep(10) # Waiting for 4 seconds to clear the screen
    os.system('clear') # Clearing the Screen


def read_input():
    while True:
        print("Enter choice \n 0 for rock \n 1 for paper \n 2 for scissor \n 3 for instructions \n 4 for exit ")

        players_choice =  input()

        if players_choice == '0' or players_choice == '1' or players_choice == '2' or players_choice == '3' or players_choice == '4':
            return int(players_choice)
        else:
            print('please choose from one of the valid options')



player = Gameplay()
computer = Gameplay()

while True:
    print('Welcome:')
    option = read_input()
    computer.set_play_random()

    if option == 0 or option == 1 or option == 2:
        player.set_play(option)
        play(player, computer)
    elif option == 3:
        instructions()
    else:
        break



'''
clears
mostrar pontuacao a cada jogada
alterar 0 1 2 3 para nomes starts with

nomes e ler args
mostrar a nossa jogada
funcao q fecha o jogo se score max for atingido

'''

