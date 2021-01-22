class draw:
    def __init__(self):
        self.Character = ["   ___  ","  /___\\ ","  \\   / ","   \\ /  ","    0   ","   /|\\  ","   / \\  ","^^^^^^^^^^"]

        self.draw_character()

    def draw_character(self):
        for drawing in self.Character:
            print(f"{drawing} \n")
        pass
    
    def update_character(self,guess):
        if guess:
            pass
        else:
            del self.Character[0]
        pass

