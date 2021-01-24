from game.draw import Draw
from game.guess import Guess

class Director:
    """
    A code template for a person who directs the game. The responsibility
    of this class of objects is to control the sequence of plsy
    
    Stereotype:
        Controller
    
    Attributes:
        draw (Draw): An instance of the class of objects knows as Draw.
        guess (Guess): An instance of the class of objects known as Guess.
        keep_playing (boolean): Whether or not the game can continue.
        round (integer): A count for how many rounds of the game are played
        goodGuess (boolean): Whether the guess was good or not.

    """


    def __init__(self):
        """
        The class constructor.

        Args:
            self (Director): an instance of Director.

        """

        self.draw = Draw()
        self.guess = Guess()
        self.keep_playing = True
        self.round = 4
        self.goodGuess = False

    def start_game(self):        
        """
        Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.round > 0:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

        self.draw.deadJumper()
           

    def do_outputs(self):
        """
        Outputs the important game information for each round of play. In 
        this case, it displays the board and prints out the jumper.

        Args:
            self (Director): An instance of Director.
        """
        self.guess.displayBoard()
        self.draw.drawJumper()

    def get_inputs(self):
        """
        Gets the inputs at the beginning of each round of play. In this case,
        that means getting a guess from the player and checking to see if it
        is a good guess.

        Args:
            self (Director): An instance of Director.
        """
        playerguess = input("Guess a letter [a-z]: ")
        self.goodGuess = self.guess.guess(playerguess.lower())
        if self.goodGuess == False:
            self.round -= 1

    def do_updates(self):
        """
        Updates the important game information for each round of play.
        This means that a line of the parachute will either be removed or not.
        It also if the game has been won or not.
        
        Args:
            self (Director): An instance of Director.
        """
        if self.guess.winCondition():
            exit()
        self.draw.updateJumper(self.goodGuess)
        self.goodGuess == False