class User:
    def __init__(self, piName):
        self.name = piName
        self.x = 0
        self.y = 0
        self.type = PlayerType.WC_ROL
    
    def moveX(amount):
        self.x = self.x + amount

    def moveY(amount):
        self.y = self.y + amount

    def resetPos(x = 0, y = 0):
        self.x = x
        self.y = y
    def setType(type):
        self.type = type

class PlayerType(Enum):
    WC_ROL = 0
    VIRUS = 1
    WINKEL_KAR = 2