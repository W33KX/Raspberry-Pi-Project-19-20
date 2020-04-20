#!/bin/python3
#made with 4 spaced tabs
from random import randrange
from enum import Enum

users = {}
types = {}
types[PlayerType.WC_ROL] = []
types[PlayerType.VIRUS] = []
types[PlayerType.WINKEL_KAR] = []

def addPlayer(piName):
    #add player to user list
    users[piName] = User(piName)
    choice = randrange(3)
    if choice == PlayerType.WC_ROL.value:
        if len(types[PlayerType.WC_ROL]) == 0:
            #add player to wc rol
            addPlayerToType(PlayerType.WC_ROL, piName)
        else:
            if len(types[PlayerType.WC_ROL]) > len(types[PlayerType.VIRUS]):
                #add player to virus
                addPlayerToType(PlayerType.VIRUS, piName)
            elif len(types[PlayerType.WC_ROL]) > len(winkel_kar):
                #add player to winkel kar
                addPlayerToType(PlayerType.WINKEL_KAR, piName)
            else:
                #add player to wc rol
                addPlayerToType(PlayerType.WC_ROL, piName)
    elif choice == PlayerType.VIRUS.value:
        if len(types[PlayerType.VIRUS]) == 0:
            #add player to virus
            addPlayerToType(PlayerType.VIRUS, piName)
        else:
            if len(types[PlayerType.VIRUS]) > len(types[PlayerType.WC_ROL]):
                #add player to wc rol
                addPlayerToType(PlayerType.WC_ROL, piName)
            elif len(types[PlayerType.VIRUS]) > len(types[PlayerType.WINKEL_KAR]):
                #add player to winkel kar
                addPlayerToType(PlayerType.WINKEL_KAR, piName)
            else:
                #add player to virus
                addPlayerToType(PlayerType.VIRUS, piName)
    else:
        if len(types[PlayerType.WINKEL_KAR]) == 0:
            addPlayerToType(PlayerType.WINKEL_KAR, piName)
        else:
            if len(types[PlayerType.WINKEL_KAR]) > len(types[PlayerType.VIRUS]):
                #add player to virus
                addPlayerToType(PlayerType.VIRUS, piName)
            elif len(types[PlayerType.WINKEL_KAR]) > len(types[PlayerType.WC_ROL]):
                #add player to wc rol
                addPlayerToType(PlayerType.WC_ROL, piName)
            else:
                #add player to winkel kar
                addPlayerToType(PlayerType.WINKEL_KAR, piName)

#do on kill or add in cart
def changeplayer(id, newType):
    for type in PlayerType:
        if(users[id].type == type):
            #remove current 
            types[type].remove(users[id])
            #add new to array
            addPlayerToType(newType, id)
            #dispach new creation of type
            break

def changePlayerYPos(id, isUp):
    #get player
    #add up or down to pos
    #save
    #dispache move

#do elke gameloop in een thread
def changePlayerXPos(id):
    #get player
    #add left(virus) or right(wc_rol) to pos
    #save
    #dispache move

def addPlayerToType(type, piName):
    users[piName].setType(type)
    types[type].append(users[piName])

class PlayerType(Enum):
    WC_ROL = 0
    VIRUS = 1
    WINKEL_KAR = 2