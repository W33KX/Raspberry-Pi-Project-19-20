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

def checkcollission(userid, gameManager):
    user = gameManager.users[userId]
    for userId in gameManager.users:
        otherUser = gameManager.users[userId]
        if otherUser.x == user.x and otherUser.y == user.y and otherUser.type != user.type:
            gameManager.changeplayer(userId, user.type)
            break
