from random import randint


class Gameplay:

    def __init__(self):
        self.play = randint(0,2)

    def set_play(self, play):
        self.play = play

    def set_play_random(self):
        self.play = randint(0,2)

    def show_winner(self, player):
        if self.play == player.play:
            return 'D'
        elif self.play == 0:
            if player.play == 1:  
                return 'L'
            elif player.play == 2: 
                return 'W'
        elif self.play == 1:        
            if player.play == 0:    
                return 'W'
            elif player.play == 2:  
                return 'L'
        else:                       
            if player.play == 0:    
                return 'L'
            elif player.play == 1:  
                return 'W'
    
    def show_play(self):
        return self.play