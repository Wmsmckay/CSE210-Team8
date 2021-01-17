'''
This program is for playing a game called HiLo. To play
a card is drawn and the user guesses if the next card 
to be drawn will be higher or lower than the first card.
If the player guesses right, they get 100 points. If they
guess wrong then they lose 75 points. The game goes until
the player's score goes negative or the player quits.

Improvments to the game that we made are:
    - Ask for the player's name
    - If the cards are the same, the player gets a 
        100,000,000 point bonus
    - When the game ends, the player gets a personalized
        exit message
    - For testing, there is an "admin" acount that gives
        a starting score of 10,000
'''



from random import randrange 


class Deal:
    def __init__(self):
        self.card = randrange(1,53)
        self.score = 0


    def new_card (self):
        # chagne the value of card to new random
        self.card = randrange(1,53)

    def compare (self, n):
        # compare player's guess
        # get new rand number
        # handle score
        second_card = randrange(1,53)
        print("Second card is: ", second_card)

        # if the cards are the same then give the player a jackpot
        if self.card == second_card:
            self.score += 100000000
            print("You hit the Jackpot! Woo!!")

        # if the player guesses correcly give them 100 points
        elif n == 'h' and self.card <= second_card:
            self.score += 100
        elif n == 'l' and self.card >= second_card:
            self.score += 100
        
        # If the player guesses incorrectly subtract 75 points
        else:
            self.score -= 75


class HiLo:
    def start_game(self):
        deal = Deal()
        play_again = True
        username = input("What is your name? ")

        # This username if for testing/fun.
        if username == "Admin":
            deal.score = 10000
        while play_again and deal.score >= 0:
            print("\nThe card is: ", deal.card)
            guess = input("Higher or lower? [h/l] ")

            # we handle the user input here in a while looo
            # to make sure that the user can only respond 
            # with h or l. 
            while guess != "h" or guess != "l":
                if guess == "h" or guess =="l":
                    break
                print("Please input [h/l] ")
                guess = input("Higher or lower? [h/l] ")
            deal.compare(guess)
            print(username, " score is: ", deal.score)
            if deal.score > 0:

                # Right here you can try to add in a way to
                # handle the incorrect user input. We only
                # want to user to be able to respond with
                # y or n.
                keep_playing = input("Keep playing? [y/n] ")
                if keep_playing == 'y':
                    play_again = True
                    deal.new_card()
                else:
                    play_again = False
                    print("Thanks for a good time ;)")
                    break
            else:
                print("Thanks for a good time", username, ";)")
                break




# game start
if __name__ == '__main__':
    game = HiLo()
    game.start_game()


    