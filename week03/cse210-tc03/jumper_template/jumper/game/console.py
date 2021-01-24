class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text input and display text output. It also
    provides methods to provide color while printing results.
    
    Stereotype:
        Service Provider, Interfacer
    Attributes:
        prompt (string): The prompt to display on each line.
    """
    def prRed(self, textIn):
        """Sets the value to red
        Args: 
            self (Draw): an instance of draw
        """
        return "\033[91m {}\033[00m" .format(textIn)
    
    def prGreen(self, textIn):
        """Sets the value to green
        Args: 
            self (Draw): an instance of draw
        """
        return "\033[92m {}\033[00m" .format(textIn)

    def prYellow(self, textIn):
        """Sets the value to yello
        Args: 
            self (Draw): an instance of draw
        """
        return "\033[93m {}\033[00m" .format(textIn)

    def prCyan(self, textIn):
        """Sets the value to cyan 
        Args: 
            self (Draw): an instance of draw
        """
        return "\033[96m {}\033[00m" .format(textIn)

    def prGrey(self, textIn):
        """Sets the value to grey
        Args: 
            self (Draw): an instance of draw
        """
        return "\033[90m {}\033[00m" .format(textIn)

    def prLPurple(self, textIn):
        """Sets the value to purple
        Args: 
            self (Draw): an instance of draw
        """
        return "\033[94m {}\033[00m" .format(textIn)
    
    # used in director.get_updates
    def read_letter(self, prompt):
        """Gets users guess.
        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
        Returns:
            string: The user's input as a string.
        """
        return str(input(prompt))
    
    # used in director.get_updates
    def drawParachute(self, parachute):
        """Draws the parachute and applies the desired color
        Args: 
            self (Draw): an instance of draw
        """
        for i in parachute:
            if i == '  ___' or i == ' /___\\' or i == ' \\   /' or i == '  \\ /':
                print(self.prGreen(i))
            elif i == '   0':
                print(self.prYellow(i))
            elif i == '  /|\\':
                print(self.prCyan(i))
            elif i == '  / \\':
                print(self.prGrey(i))
            elif i == '':
                print()
            else:
                print(self.prLPurple(i))
                print()
                break 

    #used in director.do_outoupts
    def lostGame(self): 
        """Draws the result when the player loses the game
        Args: 
            self (Draw): an instance of draw
        """
        self.parachute = ['x', '_', '_,', '########']
        losingResult = str(self.prRed(self.parachute[0]) + self.prCyan(self.parachute[1]) + self.prGrey(self.parachute[2])).replace(' ', '')
        print()
        print('You lost the game. Ouch!')
        print()
        print('   ' + losingResult)
        print(self.prGreen(self.parachute[3]))

    # used in director.do_outputs
    def celebrate(self):
        """Draws the result when the player wins the game
        Args: 
            self (Draw): an instance of draw
        """
        print()
        print('   ' + (self.prCyan('  \\') + self.prYellow('0') + self.prCyan('/')).replace(' ', ''))
        print(self.prCyan('   |'))
        print(self.prGrey('  / \\'))
        print(self.prGreen('#######'))
        print
        print(self.prGreen('                                                      __________    ________'))
        print(self.prGreen('|            |    |    |\\        |    |\\        |    |             |        \\'))
        print(self.prGreen('|            |    |    | \\       |    | \\       |    |             |         |'))
        print(self.prGreen('|            |    |    |  \\      |    |  \\      |    |             |         |'))
        print(self.prGreen('|     /\\     |    |    |   \\     |    |   \\     |    |______       |________/'))
        print(self.prGreen('|    /  \\    |    |    |    \\    |    |    \\    |    |             |    \\ '))    
        print(self.prGreen('|   /    \\   |    |    |     \\   |    |     \\   |    |             |     \\'))
        print(self.prGreen('|  /      \\  |    |    |      \\  |    |      \\  |    |             |      \\ '))
        print(self.prGreen('| /        \\ |    |    |       \\ |    |       \\ |    |             |       \\ '))
        print(self.prGreen('|/          \\|    |    |        \\|    |        \\|    |__________   |        \\ \n'))