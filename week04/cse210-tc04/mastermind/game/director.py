from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Board): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        guess (Guess): An instance of the class of objects known as Guess.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._guess = None
        self._roster = Roster()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            player.player_number = n
            self._roster.add_player(player)
            self._board._prepare(player)
        
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        updatedBaord = self._board.display_board()

        self._console.display_board(updatedBaord)

        # get next play and their guess
        player = self._roster.get_current()
        if player.player_number == 0:
            print(self._console.prRed(f"{player.get_name()}'s turn:"))
        else:
            print(self._console.prGreen(f"{player.get_name()}'s turn:"))
        # player is asked to guess a 4 digit number
        playerGuess = self._console.read_number(" What is your guess? ")
        # call guess() and set playerGuess value into the guess class
        self._guess = Guess(playerGuess)
        # instantiate value of the guess to the current player
        player.set_guess(self._guess.get_guess())

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        # gets current player
        player = self._roster.get_current()
        # places current player's guess into variable move
        # calls apply method in board and does needed updates with the current user's guess
        self._board.update_board(player)
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the guess is correct and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        
        # check the value of the current guess with the random number prepared in board
        self._keep_playing = self._board.winCondition(self._roster.get_current())
        # changes the player for the next round of the game
        self._roster.next_player()

     
       