from gameplay import *


def play(player, computer):
    win = player.show_winner(computer)

    if win == 'W':
        print(f'You won!!!')
    elif win == 'L':
        print(f'You lost!!!')
    else:
        print(f'You draw!!!')

def instructions():
    print("Winning Rules of the Rock paper scissor game as follows: \n"
                                    +"rock vs paper->paper wins \n"
                                    + "rock vs scissor->rock wins \n"
                                    +"paper vs scissor->scissor wins \n")


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
    print('start:')
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
mostrar a nossa jogada

nomes e ler args
mostrar pontuacao a cada jogada
alterar 0 1 2 3 para nomes starts with

funcao q fecha o jogo se score max for atingido
'''

