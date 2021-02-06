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

    def get_score(self):
        """
        (GETTER) Gets the current score.

        ARGS: Score (self) an instance of Score

        RETURNS: An integer. The player's score
        """

        return self._score

    def ifCorrect(self, wordList, buffer):
        """
        This function 
        """
        for key in wordList:
            if buffer == key:
                self.update_score(len(key))
                del wordList[key]
        return wordList
 

    def update_score(self, newScore):
        """
        Updates the self._score variable if the player has any more points.

        ARGS: Score (self): an instance of Score
              newScore (an integer): the new points to add to the new score

        RETURNS: An integer. The new score
        """
        self.set_score(self._score + newScore)

    def set_score(self, score):
        """
        (SETTER) Sets the updated score of the player self._score variable.

        ARGS: Score (self): an instance of Score
              score (a point): the player's score

        RETURNS: An integer. The new score
        """
        self._score = score 