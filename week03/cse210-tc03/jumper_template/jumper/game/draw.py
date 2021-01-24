class Draw:
    """
    A code template for the jumper of the game. This class's responsibility
    is to calculate changes to the jumper and then display them to the
    console.

    Stereotype:
        Information Holder

    Attributes:
        jumper (list): A list with the "image" of the jumper.
    """

    def __init__(self):
        """
        Class constructor. Declares and initializes instance attributes.
        
        Args:
            self (Draw): An instance of Draw.
        """
        self.jumper = ["  ___  "," /___\ "," \   / ","  \ /  ","   0   ", "  /|\  ","  / \  ","        ","^^^^^^^"]


    def drawJumper(self):
        """
        Prints out the jumper.

        Args:
            self (Draw): An instance of Draw.
        """
        for x in self.jumper:
            print(x)

    def updateJumper(self, guess):
        """
        Updates the condition of the jumper's parachute.

        Args:
            self (Draw): An instance of Draw.
            guess (boolean): Whether the player's guess was good.
        """

        if guess:
            pass
        else:
            self.jumper.remove(self.jumper[0])


    def deadJumper(self):
        """
        Prints out the jumper if the player loses  the game.

        Args:
            self (Draw): An instance of Draw
        """
        
        self.jumper = ["   x   ", "  /|\  ","  / \  ","        ","^^^^^^^"]
        self.drawJumper()
