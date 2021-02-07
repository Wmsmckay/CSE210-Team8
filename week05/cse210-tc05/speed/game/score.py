class Score:
    """ 
    This class will control the player's score

    Stereotype: Information Holder

    Attributes:
    """

    def __init__(self):

        """
        The class constructor.

        ARGS: Score (self) and instance of Score
        """
        self._score =  0
        self.life = 5

    def get_score(self):
        """
        (GETTER) Gets the current score.

        ARGS: Score (self) an instance of Score

        RETURNS: An integer. The player's score
        """

        return self._score

    def ifCorrect(self, wordList, buffer):
        """
        Updates the wordList.

        ARGS: Score (self): an instance of Score
              wordList (dictionary): the word and 
              buffer (string): input provided by user

        RETURNS: A dictionary. The updated wordList
        """
        for key in [key for key in wordList if key == buffer]: 
            self.update_score(len(wordList[key]) + 1)
            del wordList[key]
            
        return wordList
 

    def update_score(self, newScore):
        """
        Updates the self._score variable if the player has any more points.

        ARGS: Score (self): an instance of Score
              newScore (an integer): the new points to add to the new score
        """
        self.set_score(self._score + newScore)

    def set_score(self, score):
        """
        (SETTER) Sets the updated score of the player self._score variable.

        ARGS: Score (self): an instance of Score
              score (a point): the player's score
        """
        self._score = score 


    def loseLife(self):
        """
        This method removed lives from the player and checks to see if they
        have died. If they diee (lose all lives) then the game ends.

        Args:
            self (score): an instance of score.
        """
        if self.life <= 0:
            print("Darn, you died!")
            exit()
        
        self.life -= 1

    def missed(self, wordList):
        """
        This function checks to see if a word was not typed before it 
        got to the bottom of the screen. If it was missed then it removes 
        a life from the player.

        Args:
            self (score): an instance of score.
            wordlist (list): a list of words and their coordinates.
        """

        deletedKey = ''

        for key, value in wordList.items():
            if value[1] >= 20:
                deletedKey = key
                self.loseLife()

        for key in [key for key in wordList if key == deletedKey]: 
            del wordList[key]
            
        return wordList