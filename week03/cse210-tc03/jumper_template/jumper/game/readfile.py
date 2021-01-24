
class ReadFile:

    def __init__ (self):
        self.wordList = self.createList()


    def createList(self):
        textFile = open("jumper/game/sampleWords.txt", "r")
        content = textFile.read()
        myList = content.split(", ")
        textFile.close()
        return myList