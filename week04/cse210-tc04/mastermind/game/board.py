import random

class Board:
    """
    The responsibility of the board is to keep track of the 
    values that the players are trying to guess and to check
    how much of their guess is right.
    """

    def __init__(self):
        """
        This initiates the board with a for the players.
        """
        self.items = {}

    def _prepare(self, player):
        """
        prepares the game by getting a number for each player.

        Args:
            self (Board): an instance of Board.
        """

        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self.items[name] = [code, guess, hint]

    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """

        guess = str(guess)
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def winCondition(self, player):
        name = player.get_name()
        code = self.items[name][0]
        guess = self.items[name][1]
        if int(code) == guess:
            print("\n--------------------")
            for player in self.items:
                print("Player " + player + ": " + str(self.items[player][1])
                + ", Correct Answer: " + str(self.items[player][0]) )
            print("--------------------\n")
            print(name + " won!")
            exit()
        return True
        

    def update_board(self, player):
        """
        This method updates the board to save the current game state

        Args:
            self: an instance of Board.
            player: the current player.
        """

        name = player.get_name()
        code = self.items[name][0]
        guess = player.get_guess()
        self.items[name][1] = guess
        self.items[name][2] = self._create_hint(code, guess)

    def display_board(self):
        """
        The job of this method is to get the board details and return them to be formatted and printed out.
        """

        boardStr = ""
        for player in self.items:
            boardStr += ("Player " + player + ": " + str(self.items[player][1]) 
                + ", " + str(self.items[player][2]) + "\n")
        return boardStr