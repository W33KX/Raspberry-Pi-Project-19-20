from main import getGameManagerInstance
from user import User
from time import sleep

def Loop(gameManager):
    print(gameManager)
    while True:
        for userId in gameManager.users:
            user = gameManager.users[userId]
            gameManager.changePlayerXPos(userId)
            #check collision
            checkcollission(user, gameManager)
            checkPlayerOutOfBounds(user, gameManager)
            print(user, flush=True)

        sleep(2)

def checkcollission(user, gameManager):
    for userId in gameManager.users:
        otherUser = gameManager.users[userId]
        if otherUser.x == user.x and otherUser.y == user.y and otherUser.type != user.type:
            #virus tegen wc rol => wc rol changeplayer
            #wc rol tegen winkel kar => wc rol changeplayer en update score
            #virus tegen kar => reset score 
            gameManager.changeplayer(user.name, user.type)
            break

def checkPlayerOutOfBounds(user, gameManager):
    if user.x >= gameManager.screenWidth or user.x <= 10:
        gameManager.changeplayer(user.name, user.type)