from main import getGameManagerInstance
from user import User
from time import sleep

def Loop():
    gameManager = getGameManagerInstance()
    while True:
        for userId in gameManager.users:
            gameManager.changePlayerXPos(userId)
            #check collision
        sleep(2)
