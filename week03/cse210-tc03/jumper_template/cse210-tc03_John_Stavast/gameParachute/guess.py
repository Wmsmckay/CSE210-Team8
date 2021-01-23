import random
from gameParachute.draw import Draw



class Guess:
    """A code template for a happless but lovable hunter with rhotacism. The 
    responsibility of this class of objects is to move from location to 
    location in pursuit of the Rabbit.
    
    Stereotype:
        Information Holder

    Attributes:
        word (string): The word of Guess.
        guess (list): The letters that are guess correctly.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Guess): An instance of Guess.
        """
        wordList = ['hello', 'everybody', 'little', 'nonsense']
        self.word = random.choice(wordList)
        self.guessUnderlines = [] 
        self.userGuess = ''
        self.round = 1
    
    def underlines(self):
        """Gets the random word and creates the correct number of underlines

        Args:
            self (Guess): an instance of Guess
        """
        if self.round == 1:
            for l in self.word:
                self.guessUnderlines.append('_ ')
            self.round += 1
        print()    
        print(''.join(self.guessUnderlines) + '\n')
    
    def addLetterToUnderline(self, letter, index):
        """Gets the guessed letter and associated index and sets them in the array

        Args:
            self (Guess): an instance of Guess
        """
        self.guessUnderlines[index] = letter + ' '

    def get_Guess(self, userGuess):
        self.userGuess = userGuess

    def change_Message(self):
        """Gets a letter from the user.

        Args:
            self (Guess): An instance of Guess.
        
        Returns:
            string: A message to the user.
        """
        i = 0
        x = 0
        for l in self.word:
            if self.userGuess == l:
                self.addLetterToUnderline(self.userGuess, i)
                i += 1
                x += 1
            else:
                i += 1
        if x > 0:
            return True
        else:
            return False

    def listToString(self):
        strResult = ''.join(self.guessUnderlines)
        strResult = strResult.replace(' ', '')
        return strResult

    def end_game(self, inputVal):
        if len(inputVal) == 5:
            valReturn = [False, 1]
            return valReturn   
        elif self.word == self.listToString():
            valReturn = [False, 2]
            return valReturn
        else:
            valReturn = [True,'', 0]
            return valReturn

    
