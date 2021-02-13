from game.constants import MAX_X
from game.constants import MAX_Y
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
        
        paddles = cast["paddle"]
        bricks = cast["brick"]
        ball = cast["ball"][0]
        score = cast["score"][0]
        
        # breaks the bricks the ball runs into
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                ball.get_velocity().invert_y()
                bricks.remove(brick)
                # updates the score when a brick is removed
                score.updateScore()
                break      
        # bounces off the paddle
        for paddle in paddles:
            if ball.get_position().equals(paddle.get_position()):
                ball.get_velocity().invert_y()
                break
        # change direction of the ball off right wall        
        if ball.get_position().get_x() > MAX_X - 2:
            ball.get_velocity().invert_x()
        # change direction of the ball off the left wall    
        if ball.get_position().get_x() < 2:
            ball.get_velocity().invert_x()
        # change direction of the ball off the ceiling    
        if ball.get_position().get_y() < 2 :
            ball.get_velocity().invert_y()
        # ends the game if the paddle misses the ball        
        if ball.get_position().get_y() == MAX_Y - 1:
            quit()
            