import sys
import time

class Draw:
    def __init__(self):
        """Initializes the value of the parachute to draw

        Args: 
            self (Draw): an instance of draw
        """
        self.parachute = ['  ___',
                          ' /___\\',
                         ' \\   /',
                         '  \\ /',
                          '   0',
                          '  /|\\',
                          '  / \\',
                          '',
                          '^^^^^^^']

    def cutLine(self, guessBool):
        """removes a line from the parachute if the guess is incorrect

        Args: 
            self (Draw): an instance of draw
        """
        if guessBool == False:
            del self.parachute[0]
        else:
            return

 