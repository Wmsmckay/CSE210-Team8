from game.actor import Actor

class Score(Actor):
    """
    This class extends actor and updates the score for the player.

    Author: McKay Williams

    Args:
        self (score): an instance of the score class.

    """

    def updateScore(self):
        """
        Gets the text and pulls the score from the end of it. After that it 
        updates the score by 50 points and adds it back to the text.
        """
        
        oldText = super().get_text()
        oldText = oldText.split()
        score = oldText[len(oldText) - 1]
        score = int(score)
        score += 50
        score = str(score)
        oldText[len(oldText) - 1] = score
        str1= " "
        super().set_text(str1.join(oldText))
