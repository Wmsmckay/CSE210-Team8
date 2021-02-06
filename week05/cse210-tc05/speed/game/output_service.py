import sys
from game import constants
from asciimatics.widgets import Frame
from game.level import Level

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
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, color)
        #self._screen.print_at("Hello" * (constants.MAX_X - 5) , 0, 0, color)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, color)
        
    def draw_actor(self, actor, value):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        text = actor
        level = self._level.get_level()
        x = value.get_x()
        y = value.get_y()
        #self._screen.print_at(actor, 1, 19, 7)
        self._screen.print_at("t", 5, 5, 7)
        #self._screen.print_at("Hello" * (constants.MAX_X - 5) , 0, 0, color7)
        #self._screen.print_at(text, 0, 19, level) # color changes with each level

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        self._screen.print_at(actors , 0, 0, 7)
        for actor, value in actors:
            self.draw_actor("actor", value)
            #self._screen.print_at("test" * (constants.MAX_X - 5) , 0, 0, 7)

    def draw_buffer(self, buffer):
        level = self._level.get_level()
        self._screen.print_at(buffer, 0, 20, level)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.refresh()    