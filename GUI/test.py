#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk,Image
import time
import random
import paho.mqtt.client as paho

hoogte_window=600
breedte_window=1000

#Coordinaten van het foto's
#Virus
Xwaarde_virus=975
Ywaarde_virus=250
#Speler1
Xwaarde_speler1=120
Ywaarde_speler1=100
#Speler2
Xwaarde_speler2=120
Ywaarde_speler2=450
#Winkelkar
Xwaarde_spelerwinkelkar=(breedte_window/2)+50
Ywaarde_spelerwinkelkar=(hoogte_window/2)-50

window = Tk()
window.title('Corona-Hamster Game')

hoogte_scherm = window.winfo_screenheight()
breedte_scherm = window.winfo_screenwidth()

x_coordinaat = (breedte_scherm/2) - (breedte_window/2)
y_coordinaat = (hoogte_scherm/2) - (hoogte_window/2)

canvas = Canvas(window, width=breedte_scherm, height=hoogte_scherm)
spelers=dict()

canvas.pack()

window.geometry("%dx%d+%d+%d" % (breedte_window, hoogte_window, x_coordinaat, y_coordinaat))
window.resizable(width=False,height=False)

Label(window,text="0",compound=CENTER).pack()


fotov = Image.open("virus.png")
fotov = fotov.resize((120,120), Image.ANTIALIAS)
fotov = ImageTk.PhotoImage(fotov)
#foto_virus = canvas.create_image(Xwaarde_virus,Ywaarde_virus, anchor=NE, image=fotov)

fotospeler = Image.open("wcrol.png")
fotospeler = fotospeler.resize((100,100), Image.ANTIALIAS)
fotospeler = ImageTk.PhotoImage(fotospeler)
#fotospeler_1 = canvas.create_image(Xwaarde_speler1,Ywaarde_speler1, anchor=NE, image=fotospeler)
#fotospeler_2 = canvas.create_image(Xwaarde_speler2,Ywaarde_speler2, anchor=NE, image=fotospeler)

winkelkar = Image.open("chart.png")
winkelkar = winkelkar.resize((150,150), Image.ANTIALIAS)
winkelkar = ImageTk.PhotoImage(winkelkar)

imageList = [fotospeler, fotov, winkelkar]
score=0
scoreText = canvas.create_text(500, 20, text=str(score), font="Times 20 bold")

def setScore(_score):
 global score
 score=_score
 global scoreText
 canvas.delete(scoreText)
 scoreText = canvas.create_text(500, 20, text="Score: "+str(score), font="Times 20 bold")


def addSpeler(piname, _type, _id):
 if spelers[piname] != None:
  spelers[piname].remove()
 spelers[piname] = Wcrol(canvas, _id, imageList[int(_type)])

def moveSpeler(piname, x, y):
 spelers[piname].move(x, y)

def on_message(client, userdata, msg):
 message = msg.payload.decode("utf-8").split(";")
 print(msg.topic + " " + str(msg.payload))
 if message[0] == "change":
  addSpeler(message[1], message[3], message[2])
 if message[0] == "position":
  moveSpeler(message[3], message[1], message[2])
 if message[0] == "score":
  setScore(message[1])

def on_subsrcibe(client,userdat, mid, qos):
 print("subscibed")


client = paho.Client()
client.on_message=on_message
client.on_subscribe=on_subsrcibe
client.username_pw_set("stef","stef")
client.connect("rasberrypi.ddns.net", port=1883, keepalive=60)
client.subscribe("project/#", qos=1)


class Wcrol:
 def __init__(self,canvas,_id,_image):
  self.canvas = canvas
  self.id = canvas.create_image(0,0,anchor=NE, image=_image)
  self.textId = canvas.create_text(0,0, fill="black", text=str(_id))
  self.playerGuiID=_id
  self.x = 0
  self.y = 0

#coords geeft een array terug van [x1,y1,x2,y2]
 def draw(self):
  self.canvas.coords(self.id,self.x,self.y)
  self.canvas.coords(self.textId, int(float(self.x))+5, self.y)

  #de wcrol moet begrensd worden ter hoogte van de X en Y assen
 def move(self, x, y):
  self.x=x
  self.y=y
 
 def remove(self):
  self.canvas.delete(self.id)
  self.canvas.delete(self.textId)

while True:
 for name in spelers:
  spelers[name].draw()
 window.update_idletasks()
 client.loop()
 time.sleep(0.01)
 window.update()

window.mainloop()
client.loop_stop()
