
class ReadFile:
    """
    A template for reading in a file. The contets are added to a list
    for the game to expand it's possible words.

    Stereotype:
        Service Provider	
    
    Attributes:
        wordList (list): A list of the words from the file.
    """

    def __init__ (self):
        """
        Class constructor. Declares and initializes instance attributes.
        
        Args:
            self (ReadFile): An instance of ReadFile.
        """
        self.wordList = self.createList()


    def createList(self):
        """
        Reads the contents of a specific file and puts the contents into
        a list seperated by commas. That list is returned.

        Args:
            self (ReadFile): An instance of ReadFile.
        """
        textFile = open("jumper/game/sampleWords.txt", "r")
        content = textFile.read()
        myList = content.split(", ")
        textFile.close()
        return myList