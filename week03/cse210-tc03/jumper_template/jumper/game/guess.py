import random
from game.readfile import ReadFile

class Guess:
    """
    A code template for the guesses the player submits. The 
    responsibility of this class of objects is to determine 
    if the player's guess was correct and print out an updated
    game board.
    
    Stereotype:
        Information Holder
    Attributes:
        word (string): The word of Guess.
        letterIndex (list): Empty lines and letters that the player guesses.
    """


    def __init__(self):
        """
        Class constructor. Declares and initializes instance attributes.
        
        Args:
            self (Guess): An instance of Guess.
        """
        self.word = self.getNewWord()
        self.letterIndex = []
        self.fillBoard()


    def getNewWord(self):
        """
        Gets the new word from the list provided by the file.

        Args:
            self (Guess): An instance of Guess.
        """

        self.readfile = ReadFile()
        wordList = self.readfile.createList()
        return random.choice(wordList)
        
        
    def fillBoard(self):
        """
        Sets the length of the board that is the same length
        as the word.

        Args:
            self (Guess): an instance of Guess.
        """

        for x in self.word:
            self.letterIndex.append("_")
        

    # changes the lines of the board to match the guess
    def guess(self, letter):
        """
        Changes the lines of the board to match the guess.

        Args:
            self (Guess): an instance of Guess.
            letter (String): The guess from the player
        """
        goodGuess = False
        count = 0
        for char in self.word:
            if char == letter:
                self.letterIndex[count] = letter
                goodGuess = True
            count += 1
        return goodGuess
        

    def displayBoard(self):
        """
        Displays the board for the user.

        Args:
            self (Guess): an instance of Guess.
        """
        for x in range(len(self.letterIndex)):
            print(self.letterIndex[x], end=" ")
        print("\n")

    def winCondition(self):
        """
        Determines if the user has won the game.

        Args:
            self (Guess): an instance of Guess.
        """
        currentGuess = ""
        for char in self.letterIndex:
            currentGuess = currentGuess + char
        if currentGuess == self.word:
            return True
