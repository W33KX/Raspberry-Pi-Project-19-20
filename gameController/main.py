#!/bin/python3
#made with 4 spaced tabs
from random import randrange
from enum import Enum
from user import User
import sys
import multiprocessing

gameManagerInstance = None

class PlayerType(Enum):
    WC_ROL = 0
    VIRUS = 1
    WINKEL_KAR = 2

class GameManager:
    def __init__(self):
        self.users = {}
        self.types = {}
        self.score = 0
        self.types[PlayerType.WC_ROL] = []
        self.types[PlayerType.VIRUS] = []
        self.types[PlayerType.WINKEL_KAR] = []
        self.screenWidth = 1000
        self.screenHeight = 600
        
    def addPlayerToType(self, type, piName):
        self.users[piName].setType(type)
        if type == PlayerType.WC_ROL:
            self.users[piName].resetPos(x = 10 , y = randrange(10, self.screenHeight - 10))
        elif type == PlayerType.WINKEL_KAR:
            self.users[piName].resetPos(x = self.screenWidth / 2, y = self.screenHeight / 2)
        else:
            self.users[piName].resetPos(x = self.screenWidth - 10 , y= randrange(10, self.screenHeight - 10))
        self.types[type].append(self.users[piName])

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
                #dispach new creation of type
                break

    def changePlayerYPos(self, id, isUp):
        #get player
        user = self.users[id]
        #add up or down to pos
        if isUp:
            user.moveY(-10 if user.y >= 10 else 0)
        else:
            user.moveY(10 if user.y <= (self.screenHeight - 10) else 0)
        #save
        #dispache move

    #do elke gameloop in een thread
    def changePlayerXPos(self, id):
        #get player
        user = self.users[id]
        #add left(virus) or right(wc_rol) to pos
        if user.type == PlayerType.VIRUS:
            user.moveX(-10)
        elif user.type == PlayerType.WC_ROL:
            user.moveX(10)
        #dispache move
    
    def incrementScore():
        self.score = self.score + 1
        #send mqtt message for score
    
    def resetScore():
        self.score = 0
        #send mqtt message for score

def setup():
    global gameManagerInstance
    if gameManagerInstance is None:
        gameManagerInstance = GameManager()

def getGameManagerInstance():
    global gameManagerInstance
    return gameManagerInstance

def inputloop(gameloopThread, mqttThread):
        while True:
            # continue
            enter = input("Press Enter to End")
            if len(enter) > -1:
                gameloopThread.terminate()
                mqttThread.terminate()
                sys.exit()
                break

def test(gameManagerInstance):
    playernames= ["test1", "test2", "test3", "test4"]
    for playername in playernames:
        gameManagerInstance.addPlayer(playername)
    print(gameManagerInstance)

if __name__ == '__main__':
    setup()
    #create thread for mqtt and game loop
    import clientThreading 
    import gameLoop
    gameManager = getGameManagerInstance()
    test(gameManager)
    gameloopThread = multiprocessing.Process(target=gameLoop.Loop, args=(gameManager,))
    gameloopThread.deamon = True
    gameloopThread.start()
    mqttThread = multiprocessing.Process(target=clientThreading.MQTT, args=(gameManager,))
    mqttThread.deamon = True
    mqttThread.start()
    inputloop(gameloopThread, mqttThread)