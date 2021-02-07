from game import constants
from game.coordinate import Coordinates

class Actor:
    """ 
    The base class for all of the movable things within the game (the words)
    Its responsibilities include keeping track of: appearance, position, and velocity.

    Stereotype: Information Holder

    Attributes:
    """

    def __init__(self):

        """
        The class constructor.

        ARGS: Actor (self) and instance of Actor
        """
        self._text = " " # The variable for the word to move on the screen
        self._position = Coordinates()
        self._velocity = Coordinates()
        self._level = 0

    def get_position(self):
        """
        (GETTER) Gets the actors position variable

        ARGS: Actor (self) an instance of Actor

        RETURNS: A point. The position of the actor.
        """
        return self._position

    def get_velocity(self):
        """
        (GETTER) Gets the actors velocity variable

        ARGS: Actor (self) an instance of Actor

        RETURNS: A point. This represents the actor's speed
        """
        return self._velocity

    def get_text(self):
        """
        (GETTER) Gets the text variable that will represent the actor

        ARGS: Actor (self) an instance of Actor

        RETURNS: A string. This represents what the actor will look like.
        """
        return self._text

    def get_level(self):
        """
        (GETTER) Gets the players level variable

        ARGS: Actor (self) an instance of Actor

        RETURNS: An integer. The level of the player.
        """
        return self._level

    def move_next(self, x, y):
        """
        Moves the actor to its next position according to its current position and velocity.

        ARGS: Actor (self) an instance of Actor

        RETURNS: A point. The actor's new position.
        """     
        x = self._position.get_x()
        y = self._position.get_y()
        x = x
        y = y - 1
        position = Coordinates(x, y)
        self._position = position

    # def check_at_bottom(self, lives):
    #     """
    #     Checks to see if the word has reached the bottom of the screen. Deletes a life if it reaches the bottom.

    #     ARGS: Actor (self) an instance of Actor
    #           lives: the lives the player has

    #     RETURNS: An integer. The lives the player has left.
    #     """        
    #     if y == 0:
    #         lives = lives - 1
    #     return lives

    def set_position(self, position):
        """
        (SETTER) Sets the actors position to the updated position and stores it in the self._position variable.

        ARGS: Actor (self): an instance of Actor
              position (a point): The given position from move_next

        RETURNS: A point. The new position of the actor.
        """
        self._position = position

    def set_velocity(self, velocity):
        """
        (SETTER) Sets the actors velocity to the updated velocity and stores it in the self._velocity variable.

        ARGS: Actor (self): an instance of Actor
              velocity (a point): The given velocity

        RETURNS: A point. The new velocity of the actor.
        """
        self._velocity = velocity

    def set_text(self, text):
        """
        (SETTER) Sets and updates the text that the actor will appear as to self._text

        ARGS: Actor (self): an instance of Actor
              text (a string): The given word or value the actor will appear as

        RETURNS: A string. The new text of the actor.
        """
        self._text = text
    
    def set_level(self, level):
        """
        (SETTER) Sets and updates the level to self._level

        ARGS: Actor (self): an instance of Actor
              level (an integer): The level the player is on

        RETURNS: An integer. The player's level
        """
        self._level = level
