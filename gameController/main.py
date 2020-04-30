#!/bin/python3
#made with 4 spaced tabs
from random import randrange
from enum import Enum
from user import User
from threading import Thread
import clientThreading 

gameManagerInstance = None

class PlayerType(Enum):
    WC_ROL = 0
    VIRUS = 1
    WINKEL_KAR = 2

class GameManager:
    def __init__(self):
        self.users = {}
        self.types = {}
        self.types[PlayerType.WC_ROL] = []
        self.types[PlayerType.VIRUS] = []
        self.types[PlayerType.WINKEL_KAR] = []

    def addPlayer(self, piName):
        #add player to user list
        self.users[piName] = User(piName)
        choice = randrange(3)
        if choice == PlayerType.WC_ROL.value:
            if len(self.types[PlayerType.WC_ROL]) == 0:
                #add player to wc rol
                addPlayerToType(PlayerType.WC_ROL, piName)
            else:
                if len(self.types[PlayerType.WC_ROL]) > len(self.types[PlayerType.VIRUS]):
                    #add player to virus
                    addPlayerToType(PlayerType.VIRUS, piName)
                elif len(self.types[PlayerType.WC_ROL]) > len(winkel_kar):
                    #add player to winkel kar
                    addPlayerToType(PlayerType.WINKEL_KAR, piName)
                else:
                    #add player to wc rol
                    addPlayerToType(PlayerType.WC_ROL, piName)
        elif choice == PlayerType.VIRUS.value:
            if len(self.types[PlayerType.VIRUS]) == 0:
                #add player to virus
                addPlayerToType(PlayerType.VIRUS, piName)
            else:
                if len(self.types[PlayerType.VIRUS]) > len(self.types[PlayerType.WC_ROL]):
                    #add player to wc rol
                    addPlayerToType(PlayerType.WC_ROL, piName)
                elif len(self.types[PlayerType.VIRUS]) > len(self.types[PlayerType.WINKEL_KAR]):
                    #add player to winkel kar
                    addPlayerToType(PlayerType.WINKEL_KAR, piName)
                else:
                    #add player to virus
                    addPlayerToType(PlayerType.VIRUS, piName)
        else:
            if len(self.types[PlayerType.WINKEL_KAR]) == 0:
                addPlayerToType(PlayerType.WINKEL_KAR, piName)
            else:
                if len(self.types[PlayerType.WINKEL_KAR]) > len(self.types[PlayerType.VIRUS]):
                    #add player to virus
                    addPlayerToType(PlayerType.VIRUS, piName)
                elif len(self.types[PlayerType.WINKEL_KAR]) > len(self.types[PlayerType.WC_ROL]):
                    #add player to wc rol
                    addPlayerToType(PlayerType.WC_ROL, piName)
                else:
                    #add player to winkel kar
                    addPlayerToType(PlayerType.WINKEL_KAR, piName)

    #do on kill or add in cart
    def changeplayer(self, id, newType):
        for type in PlayerType:
            if(self.users[id].type == type):
                #remove current 
                self.types[type].remove(self.users[id])
                #add new to array
                addPlayerToType(newType, id)
                #dispach new creation of type
                break

    def changePlayerYPos(self, id, isUp):
        #get player
        user = self.users[id]
        #add up or down to pos
        if isUp:
            user.moveY(-10)
        else:
            user.moveY(10)
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
        #save
        #dispache move

    def addPlayerToType(self, type, piName):
        self.users[piName].setType(type)
        self.types[type].append(self.users[piName])

def setup():
    global gameManagerInstance
    if gameManagerInstance is None:
        gameManagerInstance = GameManager()

def getGameManagerInstance():
    global gameManagerInstance
    return gameManagerInstance

def gameloop():
        while True:
            enter = input("Press Enter to End")
            if len(enter) > -1:
                break

if __name__ == '__main__':
    setup()
    #create thread for mqtt and game loop
    gameloopThread = Thread(gameloop)
    mqttThread = Thread(clientThreading.MQTT)