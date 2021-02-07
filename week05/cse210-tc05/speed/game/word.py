import random
from game import constants
from game.actor import Actor
from game.coordinate import Coordinates

class Word(Actor):
    """
    This class handles the words for the game. It creates a list for every level
    and updates it as the player types them or they lose them. It also inherits from
    the Actor class.

    Stereotype:
        service provider.
        
    Args:
        Actor (Actor): inheritance from the actor class
    """

    def __init__(self):
        super().__init__()
        self._wordlist = []
        self._points = 0
        self._gameWords = {}
        self._level_difficulty = 1
        self._coordinates = Coordinates()
        
        
    def newList(self):
        """
        Initializes the list of words which will be used in the game based on difficulty.

        ARGS: Word (self) an instance of Word

        RETURNS: A list 
        """
            
        for word in constants.LIBRARY:
            self._wordlist.append(word)

            
        while len(self._gameWords) < 5:
            numberWord = random.randint(0,9999)
            if len(self._wordlist[numberWord]) == self._level_difficulty + 2:

                x = random.randint(1, constants.MAX_X - self._level_difficulty)
                y = random.randint(1, constants.MAX_Y - self._level_difficulty)
                self._coordinates.set_x(x)
                self._coordinates.set_y(y)
                position = [self._coordinates.get_x(), self._coordinates.get_y()]
        
                # Add the position and word to the dictionary
                self._gameWords.update({self._wordlist[numberWord] : position})
        
        return self._gameWords



    def get_words(self):
        """
        (GETTER) Retrieves the list of words to be used in the game.

        ARGS: Word (self) an instance of Word

        RETURNS: A list 
        """
        return self._gameWords
    
    def set_difficulty(self, current_level):
        """
        (SETTER) Initializes the difficuly.

        ARGS: Word (self) an instance of Word
              current_level: The player's current level

        RETURNS: An integer
        """
        self._level_difficulty = current_level

    def updateList(self, newList):
        """
        This updates the list when events changes the words inside.

        Args:
            Word (self): an instance of word.
            newList (list): a list of words.
        """

        self._gameWords = newList