#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk,Image
import time
import random

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

#def score(score):
#	text = smallfont.render("Score: "+str(score), True black)
#	gameDisplay.blit(text, [0,0])

window = Tk()
window.title('Corona-Hamster Game')

hoogte_scherm = window.winfo_screenheight()
breedte_scherm = window.winfo_screenwidth()

x_coordinaat = (breedte_scherm/2) - (breedte_window/2)
y_coordinaat = (hoogte_scherm/2) - (hoogte_window/2)

canvas = Canvas(window, width=breedte_scherm, height=hoogte_scherm)
canvas.pack()

window.geometry("%dx%d+%d+%d" % (breedte_window, hoogte_window, x_coordinaat, y_coordinaat))
window.resizable(width=False,height=False)

fotov = Image.open("virus.png")
fotov = fotov.resize((120,120), Image.ANTIALIAS)
fotov = ImageTk.PhotoImage(fotov)
foto_virus = canvas.create_image(Xwaarde_virus,Ywaarde_virus, anchor=NE, image=fotov)

fotospeler = Image.open("wcrol.png")
fotospeler = fotospeler.resize((100,100), Image.ANTIALIAS)
fotospeler = ImageTk.PhotoImage(fotospeler)
fotospeler_1 = canvas.create_image(Xwaarde_speler1,Ywaarde_speler1, anchor=NE, image=fotospeler)
fotospeler_2 = canvas.create_image(Xwaarde_speler2,Ywaarde_speler2, anchor=NE, image=fotospeler)

winkelkar = Image.open("chart.png")
winkelkar = winkelkar.resize((150,150), Image.ANTIALIAS)
winkelkar = ImageTk.PhotoImage(winkelkar)
winkelkar_foto = canvas.create_image(Xwaarde_spelerwinkelkar,Ywaarde_spelerwinkelkar, anchor=NE, image=winkelkar)

class Wcrol:
 def __init__(self,canvas):
  self.canvas = canvas
  self.id = canvas.create_image(Xwaarde_speler1,Ywaarde_speler1,anchor=NE, image=fotospeler)
  self.canvas.move(self.id,200,100)
  start = [-3,-2,-1,0,1,2,3]
  #random richting -> momenteel nog
  random.shuffle(start)
  self.x = start[0]
  self.y=-1

#coords geeft een array terug van [x1,y1,x2,y2]
 def draw(self):
  self.canvas.move(self.id,self.x,self.y)
  pos = self.canvas.coords(self.id)
  print(pos)

  #de wcrol moet begrensd worden ter hoogte van de X en Y assen
  if pos[0]<=100:
   self.x=1
  if pos[1]<=0:
   self.y = 1
  if pos[0]>=1000:
   self.x=-1
  if pos[1]>=500:
   self.y=-3

rol1 = Wcrol(canvas)

while True:
 rol1.draw()
 window.update_idletasks()
 time.sleep(0.01)
 window.update()

window.mainloop()
