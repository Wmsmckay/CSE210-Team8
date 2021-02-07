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
            self (Directory): and instance of Director
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

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word.newList()
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

        self.buffer += self._input_service.get_letter()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking when the user has finished typing a word 
        and checking if that word is in the word list. It also means moving the 
        words down the screen for the user to type out.

        Args:
            self (Director): An instance of Director.
        """
        self.current_level = self._level.get_level()
        if len(self._word.get_words()) < 1:
            newLevel = self._level.get_level() + 1
            self.current_level = newLevel
            self._level.set_level(self.current_level)
            self._word.newList()
            self._word.set_difficulty(self.current_level)
        self._word.updateList(self._score.ifCorrect(self._word.get_words(), self.buffer))
        
        self._word.updateList(self._score.missed(self._word.get_words()))
                    
        # Check to see if buffer has been cleared
        if '*' in self.buffer:
            self.buffer = ''

        self._handle_word_velocity()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the user has typed a complete word 
        and awarding points for it. It also checks to see if the user has 
        used up all of their chances for playing. If not, it advances them to 
        the next level.


        Args:
            self (Director): An instance of Director.
        """
        
        # clear the screen buffer
        self._output_service.clear_screen(self.current_level)
        # draw all of the words
        self._output_service.draw_actors(self._word.get_words())
        # draw score
        self._output_service.draw_score(self._score.get_score())
        # draw the buffer
        self._output_service.draw_buffer(self.buffer)
        # refresh the screen
        self._output_service.flush_buffer()
        
    def _handle_word_velocity(self):
        """Handles the velocity of the word

        Args:
            self (Director): An instance of Director.
        """
        newList = self._word.get_words()
        for key, coords in newList.items():
            coords[1] += .05
        self._word.updateList(newList)
