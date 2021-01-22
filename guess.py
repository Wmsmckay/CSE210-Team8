import random
class guess:
    def __init__(self):
        self.Wordlist = ["word","list","number"]
        self.spacelist = []
        self.pickedWord = "1"
        self.letterguess = "1"
        self.guessedletters = []
        
        self.pickWord()
        self.print_values()


    def pickWord(self):
        random_number = random.randint(1,len(self.Wordlist)-1)
        self.pickedWord= self.Wordlist[random_number]
        for letter in self.pickedWord:
            self.spacelist.append("_ ")

    def update_list(self,guessed):
        i = 0
        self.guessedletters.append(guessed)
        for letter in self.pickedWord:
            if letter == guessed:
                self.spacelist[i] = guessed
            
        else:
            return False
        i = i+1
        
        return True
    def print_values(self):
        i = 0
        for letter in self.spacelist:
            print(self.spacelist[i], end=" ")
            i=i+1
        print()
        print("Guessed letters:")
        for letter in self.guessedletters:
           print(f"{letter}", end=" ")
            
