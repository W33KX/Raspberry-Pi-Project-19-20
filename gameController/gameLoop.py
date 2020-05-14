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
        if otherUser.type == user.type:
            continue
        if checkXCollision(user, otherUser) and checkYCollision(user, otherUser):
            print("Colission: " + user.name + " And " + otherUser.name)
            #virus tegen wc rol => wc rol changeplayer
            if user.type == 0 and otherUser.type == 1:
                gameManager.changeplayer(user.name, user.type)
            elif user.type == 1 and otherUser.type == 0:
                gameManager.changeplayer(otherUser.name, otherUser.type)
            #wc rol tegen winkel kar => wc rol changeplayer en update score
            elif user.type == 0 and otherUser.type == 2:
                gameManager.incrementScore()
                gameManager.changeplayer(user.name, user.type)
            elif user.type == 2 and otherUser.type == 0:
                gameManager.incrementScore()
                gameManager.changeplayer(otherUser.name, otherUser.type)
            #virus tegen kar => reset score 
            elif user.type == 2 and otherUser.type == 1:
                gameManager.resetScore()
                gameManager.changeplayer(otherUser.name, otherUser.type)
            elif user.type == 1 and otherUser.type == 2:
                gameManager.resetScore()
                gameManager.changeplayer(user.name, user.type)
            break

def checkXCollision(user, otherUser):
    return otherUser.x < user.x + user.getDimension() and otherUser.x + otherUser.getDimension() > user.x

def checkYCollision(user, otherUser):
    return otherUser.y < user.y + user.getDimension() and otherUser.y + otherUser.getDimension() > user.y

def checkPlayerOutOfBounds(user, gameManager):
    if user.x >= gameManager.screenWidth or user.x <= 10:
        gameManager.changeplayer(user.name, user.type)