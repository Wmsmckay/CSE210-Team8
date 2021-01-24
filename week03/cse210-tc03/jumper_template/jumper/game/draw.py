class Draw:

    def __init__(self):
        self.jumper = ["  ___  "," /___\ "," \   / ","  \ /  ","   0   ", "  /|\  ","  / \  ","        ","^^^^^^^"]


    def drawJumper(self):
        for x in self.jumper:
            print(x)

    def updateJumper(self, guess):
        if guess:
            pass
        else:
            self.jumper.remove(self.jumper[0])


    def deadJumper(self):
        
        self.jumper = ["   x   ", "  /|\  ","  / \  ","        ","^^^^^^^"]
        self.drawJumper()
