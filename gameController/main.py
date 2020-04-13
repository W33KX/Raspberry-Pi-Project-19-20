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
    choice = randrange(3)
    if choice == PlayerType.WC_ROL.value:
        if len(types[PlayerType.WC_ROL]) == 0:

        else:
            if len(types[PlayerType.WC_ROL]) > len(types[PlayerType.VIRUS]):
                #add player to virus
            elif len(types[PlayerType.WC_ROL]) > len(winkel_kar):
                #add player to winkel kar
            else:
                #add player to wc rol
    elif choice == PlayerType.VIRUS.value:
        if len(types[PlayerType.VIRUS]) == 0:
            #add player to virus
        else:
            if len(types[PlayerType.VIRUS]) > len(types[PlayerType.WC_ROL]):
                #add player to wc rol
            elif len(types[PlayerType.VIRUS]) > len(types[PlayerType.WINKEL_KAR]):
                #add player to winkel kar
            else:
                #add player to virus
    else:
        if len(types[PlayerType.WINKEL_KAR]) == 0:

        else:
            if len(types[PlayerType.WINKEL_KAR]) > len(types[PlayerType.VIRUS]):
                #add player to virus
            elif len(types[PlayerType.WINKEL_KAR]) > len(types[PlayerType.WC_ROL]):
                #add player to wc rol
            else:
                #add player to winkel kar
    #add player to user list
    #player heeft zoizo een state die zegt welk type hij is

#do on kill or add in cart
def changeplayer(id):
    for type in PlayerType:
        if(users[id].type == type):
            #remove current 
            #add new to array
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

class PlayerType(Enum):
    WC_ROL = 0
    VIRUS = 1
    WINKEL_KAR = 2