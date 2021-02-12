import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        #marquee = cast["marquee"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        ball = cast["ball"]
        # marquee.set_text("")
        # for brick in bricks:
        #     if ball.get_position().equals(brick.get_position()):
        #         print(ball.get_position())
        
        # print(ball.get_position())
                
        #         velocity_get = ball.get_velocity()
        #         x2 = velocity_get.get_x()
        #         x2 *= -1
        #         ball.set_velocity(x2)
        # ##### Collision with paddle
        # when ball == paddlevelocity * -1     