import random
from game.readfile import ReadFile

class Guess:

    def __init__(self):
        self.word = self.getNewWord()
        self.letterIndex = []
        self.fillBoard()


    # gets a new word for the game
    def getNewWord(self):
        self.readfile = ReadFile()
        wordList = self.readfile.createList()
        return random.choice(wordList)
        
        
    # sets the length of the board the same as the word length
    def fillBoard(self):
        for x in self.word:
            self.letterIndex.append("_")
        

    # changes the lines of the board to match the guess
    def guess(self, letter):
        goodGuess = False
        count = 0
        for char in self.word:
            if char == letter:
                self.letterIndex[count] = letter
                goodGuess = True
            count += 1
        return goodGuess
        

    def displayBoard(self):
        for x in range(len(self.letterIndex)):
            print(self.letterIndex[x], end=" ")
        print("\n")

    def winCondition(self):
        currentGuess = ""
        for char in self.letterIndex:
            currentGuess = currentGuess + char
        if currentGuess == self.word:
            print("You Win!!")
            return True
