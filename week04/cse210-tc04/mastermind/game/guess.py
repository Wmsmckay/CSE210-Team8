class Guess:
    """
    The player's guess in the game. The responsibility of this class is to 
    keep track of the player's guess and the number's in them.
    
    Stereotype: 
        Information Holder

    Attributes:
        _pile (integer): The pile to remove from.
        _stones (integer): The number of stones to remove.
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Guess): an instance of Guess.
        """
        self._guess = guess

    def get_guess(self):
        """returns the player's guess
        Args:
            self (Guess): an instance of Guess.
        """
        return self._guess

    def set_guess(self, guess):
        self._guess = guess