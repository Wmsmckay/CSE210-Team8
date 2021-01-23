from game.draw import Draw
from game.guess import Guess

class Director:


    def __init__(self):
        self.draw = Draw()
        self.guess = Guess()
        self.keep_playing = True
        self.round = 4
        self.goodGuess = False

    def start_game(self):        
        
        while self.round > 0:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

        self.draw.deadJumper()
           

    def do_outputs(self):
        self.guess.displayBoard()
        self.draw.drawJumper()

    def get_inputs(self):
        playerguess = input("Guess a letter [a-z]: ")
        self.goodGuess = self.guess.guess(playerguess.lower())
        if self.goodGuess == False:
            self.round -= 1

    def do_updates(self):
        if self.guess.winCondition():
            exit()
        self.draw.updateJumper(self.goodGuess)
        self.goodGuess == False