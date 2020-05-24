from random import randrange
from enum import Enum
from user import User

class PlayerType(Enum):
    WC_ROL = 0
    VIRUS = 1
    WINKEL_KAR = 2

class GameManager:
    def __init__(self, client):
        self.users = {}
        self.types = {}
        self.score = 0
        self.types[PlayerType.WC_ROL] = []
        self.types[PlayerType.VIRUS] = []
        self.types[PlayerType.WINKEL_KAR] = []
        self.screenWidth = 1000
        self.screenHeight = 600
        self.internalPlayerId = 0
        self.mqttClient = client

    def sendMessage(self, topic, message):
        self.mqttClient.publish(topic, message)

    def addPlayerToType(self, type, piName):
        self.users[piName].setId(self.internalPlayerId)
        if self.internalPlayerId + 1 > 9:
            self.internalPlayerId = 0
        else:
            self.internalPlayerId = self.internalPlayerId + 1
        self.users[piName].setType(type)
        if type == PlayerType.WC_ROL:
            self.users[piName].resetPos(x = 120 , y = randrange(70, self.screenHeight - 70, 70))
        elif type == PlayerType.WINKEL_KAR:
            self.users[piName].resetPos(x = int(self.screenWidth) / 2, y = int(self.screenHeight) / 2)
        else:
            self.users[piName].resetPos(x = self.screenWidth - 25 , y= randrange(70, self.screenHeight - 70, 70))
        if not self.users[piName] in self.types[type]:
            self.types[type].append(self.users[piName])
        #send message user created/changed user object
        mqttmsg = "change;{};{};{}".format(piName, self.users[piName].id, int(self.users[piName].type.value))
        self.sendMessage("project/changeplayer", mqttmsg)

    def addPlayer(self, piName):
        #add player to user list
        self.users[piName] = User(piName)
        choice = randrange(3)
        if choice == PlayerType.WC_ROL.value:
            if len(self.types[PlayerType.WC_ROL]) == 0:
                #add player to wc rol
                self.addPlayerToType(PlayerType.WC_ROL, piName)
            else:
                if len(self.types[PlayerType.WC_ROL]) > len(self.types[PlayerType.VIRUS]):
                    #add player to virus
                    self.addPlayerToType(PlayerType.VIRUS, piName)
                elif len(self.types[PlayerType.WC_ROL]) > len(self.types[PlayerType.WINKEL_KAR]):
                    #add player to winkel kar
                    self.addPlayerToType(PlayerType.WINKEL_KAR, piName)
                else:
                    #add player to wc rol
                    self.addPlayerToType(PlayerType.WC_ROL, piName)
        elif choice == PlayerType.VIRUS.value:
            if len(self.types[PlayerType.VIRUS]) == 0:
                #add player to virus
                self.addPlayerToType(PlayerType.VIRUS, piName)
            else:
                if len(self.types[PlayerType.VIRUS]) > len(self.types[PlayerType.WC_ROL]):
                    #add player to wc rol
                    self.addPlayerToType(PlayerType.WC_ROL, piName)
                elif len(self.types[PlayerType.VIRUS]) > len(self.types[PlayerType.WINKEL_KAR]):
                    #add player to winkel kar
                    self.addPlayerToType(PlayerType.WINKEL_KAR, piName)
                else:
                    #add player to virus
                    self.addPlayerToType(PlayerType.VIRUS, piName)
        else:
            if len(self.types[PlayerType.WINKEL_KAR]) == 0:
                self.addPlayerToType(PlayerType.WINKEL_KAR, piName)
            else:
                if len(self.types[PlayerType.WINKEL_KAR]) > len(self.types[PlayerType.VIRUS]):
                    #add player to virus
                    self.addPlayerToType(PlayerType.VIRUS, piName)
                elif len(self.types[PlayerType.WINKEL_KAR]) > len(self.types[PlayerType.WC_ROL]):
                    #add player to wc rol
                    self.addPlayerToType(PlayerType.WC_ROL, piName)
                else:
                    #add player to winkel kar
                    self.addPlayerToType(PlayerType.WINKEL_KAR, piName)
        

    #do on kill or add in cart
    def changeplayer(self, id, newType):
        for type in PlayerType:
            if(self.users[id].type == type):
                #remove current 
                self.types[type].remove(self.users[id])
                #add new to array
                self.addPlayerToType(newType, id)
                break

    def changePlayerYPos(self, id, isUp):
        #get player
        user = self.users[id]
        if user.type == PlayerType.WINKEL_KAR:
            if isUp:
                user.moveX(-20 if user.x > 400 else 0)
            else:
                user.moveX(20 if user.x < 660 else 0)
            return
        #add up or down to pos
        if isUp:
            user.moveY(-20 if user.y > 20 else 0)
        else:
            user.moveY(20 if user.y <= (self.screenHeight - 20) else 0)
        #dispache move
        self.sendMessage("project/position", "position;{};{};{};{}".format(user.x, user.y, user.name, user.id))

    #do elke gameloop in een thread
    def changePlayerXPos(self, id):
        #get player
        user = self.users[id]
        #add left(virus) or right(wc_rol) to pos
        if user.type == PlayerType.VIRUS:
            user.moveX(-20)
        elif user.type == PlayerType.WC_ROL:
            user.moveX(20)
        #dispache move
        self.sendMessage("project/player", "position;{};{};{};{}".format(user.x, user.y, user.name, user.id))

    def incrementScore(self):
        self.score = self.score + 1
        #send mqtt message for score
        self.sendMessage("project/score", "score;"+str(self.score))
    
    def resetScore(self):
        self.score = 0
        #send mqtt message for score
        self.sendMessage("project/score", "score;"+str(self.score))
    
    def sendSummary(self):
        pinames = self.users.keys()
        self.sendMessage("project/changeplayer", "summary;{}".format(";".join(pinames)))
