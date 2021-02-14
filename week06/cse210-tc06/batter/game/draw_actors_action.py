from game.action import Action

class DrawActorsAction():
    """
    This class makes sure that all actions are drawn to the screen.

    Authors:
        John Stavast
        Christine Helfrinch

    Stereotype:
        Controller
    
    """

    def __init__(self, output_service):
        self._output_service = output_service


    def execute(self, cast):
        """Executes drawing the actor's action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        for actors in cast.values():                
            self._output_service.draw_actors(actors)
        self._output_service.flush_buffer()