import random
from game import constants
from game.actor import Actor
from game.coordinate import Coordinates

class Word(Actor):
    def __init__(self):
        super().__init__()
        self._wordlist = []
        self._points = 0
        self._gameWords = {}
        self._level_difficulty = 0
        
        
    def newList(self):
        """
        Initializes the list of words which will be used in the game based on difficulty.

        ARGS: Word (self) an instance of Word

        RETURNS: A list 
        """
        readinFile = open('speed/game/words.txt','r')

        for word in readinFile.read().split():
            self._wordlist.append(word)
        
        while len(self._gameWords) < 5:
            numberWord = random.randint(0,9999)
            if len(self._wordlist[numberWord]) == self._level_difficulty + 4:
                #self._gameWords.append(self._wordlist[numberWord])
                x = random.randint(1, constants.MAX_X - self._level_difficulty)
                y = random.randint(1, constants.MAX_Y - self._level_difficulty)
                position = Coordinates(x, y)

                # set the word's position in the actor
                #self.set_position(position)

                # Add the word to the dictionary
                self._gameWords.append(self._wordlist[numberWord])
                # add the position of the word to it's entry in the dictionary
                self._gameWords[self._wordlist[numberWord].append(position)]
                #self._gameWords[self._wordlist[numberWord]].set_text(self._wordlist[numberWord])
                # What is this?
                # self._gameWords = self._wordlist[numberWord]
        
        
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
        self.level_difficulty = current_level

    def updateList(self, newList):
        self._gameWords = newList