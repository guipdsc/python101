from gameplay import *
import os
from time import sleep
from sys import *
#from names import *
#from scores import *

def mapping_hands(hand):
    if hand == 0:
        return 'Rock'
    elif hand == 1:
        return 'Paper'
    elif hand == 2:
        return 'Scizor'
    else:
        'undefined hand error, please correct code'

def clear_screen(wait):
        print(f'\n(Screen will be cleared in {wait} seconds)')
        sleep(wait) # Waiting for 4 seconds to clear the screen
        os.system('clear') # Clearing the Screen


def get_older_name():

    try:
        with open('older_name.txt', 'r') as f:
            lines = f.readlines()
            return lines[0]
    except:
        with open('older_name.txt', 'w+') as f:
            return 'default'
    
def save_name(name):
    with open('older_name.txt', 'w+') as f:
        f.write(name)

def aplly_name(args):
    if args['name'] != False:
        save_name(args['name'])
        return args['name']

    print(f'Before start playing choose your name:')
    name =  input()

    if name == '':
        name = get_older_name()

    save_name(name)

    return name

def read_args():
    args = list(argv)
    arg = {'name': False, 'score': False}

    for a in range(1, len(args)):
        if args[a].isnumeric() and arg['score'] == False:
            arg['score'] = int(args[a])
            if arg['score'] > 100:
                arg['score'] = 100
        elif arg['name'] == False:
            arg['name'] = args[a]

    return arg


def check_max_score_reached(pcScore,myScore, maxScore):
    if maxScore != False:
        if pcScore == maxScore:
            print('Max score reached. You have lost. Sad face!')
            clear_screen(10)
            exit()
        elif myScore == maxScore:
            print('Max score reached. You have won. Congratulations!')
            clear_screen(10)
            exit()

def play(player, computer):
    win = player.show_winner(computer)
    my_hand = player.show_play()
    pc_hand = computer.show_play()
    if win == 'W':
        print(f'You won!!! Your hand ({mapping_hands(my_hand)}) is stronger then the computers ({mapping_hands(pc_hand)})')
        clear_screen(5)
    elif win == 'L':
        print(f'You lost!!! Your hand ({mapping_hands(my_hand)}) is weaker then the computers ({mapping_hands(pc_hand)})')
        clear_screen(5)
    else:
        print(f'You draw!!! Your hand ({mapping_hands(my_hand)}) is equal to the computers ({mapping_hands(pc_hand)})')
        clear_screen(5)
    return win

def instructions():
    print("\nWinning Rules of the Rock paper scissor game as follows: \n"
                                    +"rock vs paper->paper wins \n"
                                    + "rock vs scissor->rock wins \n"
                                    +"paper vs scissor->scissor wins \n")
    clear_screen(10)


def read_input():
    while True:
        print("Enter choice \n 0 for rock \n 1 for paper \n 2 for scissor \n 3 for instructions \n 4 for exit ")

        players_choice =  input()

        if players_choice == '0' or players_choice == '1' or players_choice == '2' or players_choice == '3' or players_choice == '4':
            return int(players_choice)
        else:
            print('please choose from one of the valid options')

def updateScore(pcScore,myScore,winner):

    if winner == 'W':
        myScore += 1
    elif winner == 'L':           
        pcScore += 1
    print(f'PC Score: {pcScore}\nMy Score: {myScore}\n')
    return pcScore, myScore

pcScore = 0
myScore = 0
player = Gameplay()
computer = Gameplay()
args = read_args()
name = aplly_name(args)
print(f"""Your name is: {name} and the max score is: {args['score']}""")

while True:
    option = read_input()
    computer.set_play_random()

    if option == 0 or option == 1 or option == 2:
        player.set_play(option)
        winner = play(player, computer)
        pcScore, myScore = updateScore(pcScore,myScore,winner)
        check_max_score_reached(pcScore, myScore, args['score'])
    elif option == 3:
        instructions()
    else:
        break



'''
tratar show resultado a cada iteracao
classes
funcao startswith
testes
'''

