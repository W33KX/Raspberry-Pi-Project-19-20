#!/bin/python3
#made with 4 spaced tabs
import sys
from gameManager import GameManager
import paho.mqtt.client as paho
from user import User
from time import sleep

gameManagerInstance = None
client = None

def getGameManagerInstance():
    global gameManagerInstance
    return gameManagerInstance

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed!")

def on_message(client, userdata, msg):
    mqttmsg = str(msg.payload)
    print(mqttmsg)
    
def on_publish(client, userdata, mid):
    print("mid: " + str(mid))

def setup():
    global client
    client = paho.Client(client_id="client-1",username="stef", password="stef", clean_session=True, userdata=None, protocol=paho.MQTTv31)
    client.on_subscribe= on_subscribe
    client.on_message= on_message
    client.on_publish= on_publish
    client.connect("rasberrypi.dnss.net", port=1883, keepalive=60)
    client.subscribe("newtopic/test", qos=1)
    global gameManagerInstance
    if gameManagerInstance is None:
        gameManagerInstance = GameManager(client)


def inputloop():
    global client
    client.loop_start()
    while True:
        try:
            for userId in gameManager.users:
                user = gameManager.users[userId]
                gameManager.changePlayerXPos(userId)
                #check collision
                checkcollission(user, gameManager)
                checkPlayerOutOfBounds(user, gameManager)
                print(user, flush=True)

            sleep(2)
        except:
            client.loop_stop()
            sys.exit()

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

def test(gameManagerInstance):
    playernames= ["test1", "test2", "test3", "test4"]
    for playername in playernames:
        gameManagerInstance.addPlayer(playername)
    print(gameManagerInstance)

if __name__ == '__main__':
    setup()
    gameManager = getGameManagerInstance()
    test(gameManager)
    inputloop()