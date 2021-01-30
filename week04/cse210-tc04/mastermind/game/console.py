import random

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
     
    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            integer: The user's input as an integer.
        """
        return int(input(prompt))
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)

    def prGreen(self, textIn):
        """Sets the value to green
        Args: 
            self (Draw): an instance of draw
        """
        return "\033[92m {}\033[00m" .format(textIn)


    def prRed(self, textIn):
        """Sets the value to red
        Args: 
            self (Draw): an instance of draw
        """
        return "\033[91m {}\033[00m" .format(textIn)

    def prCyan(self, textIn):
        """Sets the value to cyan 
        Args: 
            self (Draw): an instance of draw
        """
        return "\033[96m {}\033[00m" .format(textIn)
    
    def display_board(self, board):
        """
        This method prints out the board to the console. It takes
        in the board and splits it by player to color coordinate 
        them with the color of the player's name.
        """

        x = board.split()
        p1 = []
        p2 = []
        str1 = " "
        str2 = " "
        count = 0
        for i in x:
            if count < 4:
                p1.append(i)
            else:
                p2.append(i)
            count += 1
        print(self.prCyan("\n --------------------"))
        print(self.prRed(str1.join(p1)))
        print(self.prGreen(str2.join(p2)))
        print(self.prCyan("--------------------\n"))