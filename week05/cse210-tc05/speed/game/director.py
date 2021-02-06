from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.level import Level

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        word (Word): A list of words for the level.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        level (Level): The current level.
    """

    def __init__(self, input_service, output_service):
        """
        The class constructor.

        Args:
            sefl (Directory): and instance of Director.
            input_service (Input_service): an instacne of the input service.
            output_service (Output_service): and instance of the output_serivce.
        """
        self._level = Level()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._word = Word()
        self.buffer = ''
        self.current_level = 1
        self.lives = 5

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)








    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the user's input for what letters are typed.

        Args:
            self (Director): An instance of Director.
        """

        self.buffer = self._input_service.get_letter()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        that means checking when the user has finished typing a word and checking 
        if that word is in the word list. It also means moving the words down the
        screen for the user to type out.


        Args:
            self (Director): An instance of Director.
        """
        # check to see if the level has been completed
        if self._score.ifCorrect(self._word.get_words, self.buffer):
            self._score.update_score()
            self._word.remove_word(self.buffer)

        # Check to see if buffer has been cleared
        if '*' in self.buffer:
            self.buffer = ''

        self._handle_word_velocity()
        


        #self._handle_body_collision()
        #self._handle_food_collision()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.


        that means checking if the user has typed a complete word and awarding
        points for it. It also checks to see if the user has used up all of their
        chances for playing. If not, it advances them to the next level.

        Args:
            self (Director): An instance of Director.
        """

        

        # check to see how many lives are left
        if self.lives < 1:
            print('Game Over')
            exit()

        # update the current level
        self.current_level = self._level.get_level()
        # clear the screen buffer
        self._output_service.clear_screen()

        # draw all of the words
        self._output_service.draw_actor(self._word.get_words)
        # draw the buffer
        self._output_service.draw_actor(self.buffer)
        # refresh the screen
        self._output_service.flush_buffer()
        








    def _handle_word_velocity(self):
        """Handles collisions between the snake's head and body. Stops the game 
        if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._snake.get_head()
        body = self._snake.get_body()
        for segment in body:
            if head.get_position().equals(segment.get_position()):
                self._keep_playing = False
                break

    def _handle_food_collision(self):
        """Handles collisions between the snake's head and the food. Grows the 
        snake, updates the score and moves the food if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._snake.get_head()
        if head.get_position().equals(self._food.get_position()):
            points = self._food.get_points()
            for n in range(points):
                self._snake.grow_tail()
            self._score.add_points(points)
            self._food.reset() 