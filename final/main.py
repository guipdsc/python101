from gameplay import *


def play(player, computer):
    win = player.show_winner(computer)

    if win == 'W':
        print(f'You won!!!')
    elif win == 'L':
        print(f'You lost!!!')
    else:
        print(f'You draw!!!')








player = Gameplay()
computer = Gameplay()

while True:
    print('start:')
    option = int(input())

    computer.set_play_random()

    if option == 0 or option == 1 or option == 2:
        player.set_play(option)

        play(player, computer)
    elif option == 3:
        instructions()
    else:
        break
