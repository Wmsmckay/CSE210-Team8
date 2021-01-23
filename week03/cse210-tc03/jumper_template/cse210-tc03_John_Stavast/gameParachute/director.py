from gameParachute.console import Console
from gameParachute.draw import Draw
from gameParachute.guess import Guess


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        hunter (Hunter): An instance of the class of objects known as Hunter.
        rabbit (Rabbit): An instance of the class of objects known as Rabbit.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.guess = Guess()
        self.keep_playing = True
        self.draw = Draw()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the hunter to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self.guess.underlines()
        self.console.drawParachute(self.draw.parachute)
        userGuess = self.console.read_letter("Guess a letter [a-z]: ")
        self.guess.get_Guess(userGuess)
        
    def do_updates(self):
        """Updates the important game information for each round of play.
        This means that a line of the parachute will either be removed or not.

        Args:
            self (Director): An instance of Director.
        """
        guessBool = self.guess.change_Message()
        self.draw.cutLine(guessBool)
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, it allows another guess or it shows the ending result.

        Args:
            self (Director): An instance of Director.
        """
        keepPlaying = self.guess.end_game(self.draw.parachute)
        self.keep_playing = keepPlaying[0]
        if keepPlaying[1] == 1:
            self.console.lostGame()
        elif keepPlaying[1] == 2:
            self.console.celebrate()