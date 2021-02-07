import sys
from game import constants
from asciimatics.widgets import Frame
from game.level import Level
from game.coordinate import Coordinates

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """
        
        self._level = Level()
        self._screen = screen
        
    def clear_screen(self, color):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 

        self._level.set_level(color)
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, color)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, color)
        self._screen.print_at("Level: " + str(color), 51, 0, 7)
        
    def draw_actor(self, actor, value):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        text = actor
        level = self._level.get_level()
        x = round(value[0])
        y = round(value[1])
        self._screen.print_at(actor, x, y, level)

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        for actor, value in actors.items():
            self.draw_actor(actor, value)

    def draw_buffer(self, buffer):
        """Renders the buffer text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        level = self._level.get_level()
        self._screen.print_at("Buffer: ", 1, 20, 7)
        self._screen.print_at(buffer, 9, 20, level)


    def draw_score(self, score):
        """Renders the given score text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.print_at("Score: " + str(score), 1, 0, 7)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.refresh()    