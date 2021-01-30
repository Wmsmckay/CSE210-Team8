import random

class Board:
    """
    The responsibility of the board is to keep track of the 
    values that the players are trying to guess and to check
    how much of their guess is right.
    """

    def __init__(self, player1, player2):
        self._prepare(player1)
        self._prepare(player2)
        self.items = []

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

    hint = ""
    for index, letter in enumerate(guess):
        if code[index] == letter:
            hint += "x"
        elif letter in code:
            hint += "o"
        else:
            hint += "*"
    return hint

    def _winCondition(self, code, guess):
        if code = guess:

    def update_board(self, player):
        name = player.get_name()
        code = self.items[name][0]
        guess = self.items[name][1]
        self.items[name][2] = _create_hint(code, guess)

    def display_board(self, player1, player2):
        print("--------------------")
        for player in items:
        print("Player " + player + ": " + [player][1] 
            + ", " + [player][2])
        print("--------------------")
