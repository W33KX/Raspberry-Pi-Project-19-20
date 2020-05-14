from enum import Enum

class PlayerType(Enum):
    WC_ROL = 0
    VIRUS = 1
    WINKEL_KAR = 2

class User:
    def __init__(self, piName):
        self.name = piName
        self.id = 0
        self.x = 0
        self.y = 0
        self.type = PlayerType.WC_ROL
        self.playerDimensions = { str(PlayerType.WC_ROL): 100, str(PlayerType.VIRUS): 120, str(PlayerType.WINKEL_KAR): 150 }
    
    def setId(self, id):
        self.id = id

    def moveX(self, amount):
        self.x = self.x + amount

    def moveY(self, amount):
        self.y = self.y + amount

    def resetPos(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def setType(self, type):
        self.type = type
    
    def getDimension(self):
        return self.playerDimensions[str(self.type)]

    #toString methode
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)