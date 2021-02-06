
class Level:
    """The class constructor.
        
        Args:
            self (Levels): an instance of Levels.
        """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Levels): an instance of Levels.
        """
        self.score = 0
        self.level = 1
        self.word_length = 3
        self.word_count = 3
        self.velocity = 3

    def get_score(self, score):
        """
        (GETTER) Gets the score.

        ARGS: Level (self) an instance of  Level
              Score: The player's current score

        RETURNS: An integer. The player's score.
        """
        self.score = score

    def get_level(self):
        """
        (GETTER) Gets the level.

        ARGS: Level (self) an instance of  Level

        RETURNS: An integer. The player's level.
        """
        i = self.level
        while i < 8:
            if self.score > i * 15:
                self.level = i + 1
                self.set_word_length()
                self.set_word_count()
                self.get_velocity()
                i += 1
            elif i == 8:
                """
                HOW DO WE END THE GAME WHEN THEY WIN????
                """
            else:
                break
        return self.level

    def set_word_length(self):
        """
        (SETTER) Sets the word length

        ARGS: Level (self) an instance of  Level

        RETURNS: An integer. The length.
        """
        self.word_length += 1
        return self.word_length
        
    def set_word_count(self):
        """
        (SETTER) Sets the word count

        ARGS: Level (self) an instance of  Level

        RETURNS: An integer. The word count.
        """
        self.word_count += 1 
        return self.word_count 
    
    def get_velocity(self):
        """
        (SETTER) Sets the velocity

        ARGS: Level (self) an instance of  Level

        RETURNS: An integer. The velocity
        """
        self.velocity += 1
        return self.velocity