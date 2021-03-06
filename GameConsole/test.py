#!/usr/bin/python3

# 7SEG PINOUT:
# 	A = GPIO17
# 	B = GPIO27
# 	C = GPIO22
# 	D = GPIO10
# 	E = GPIO09
# 	F = GPIO11
# 	G = GPIO05

# 	DP1 = GPIO23
# 	DP2 = GPIO24
# 	DP3 = GPIO25
# 	DP4 = GPIO08

# MODES PINOUT:
# 	MODE1:
# 		RED 	= GPIO07
# 	MODE2:
# 		YELLOW 	= GPIO01
# 	MODE3:
# 		GREEN	= GPIO12

# BUTTONS PINOUT:
# 	UP	= GPIO16
# 	DOWN	= GPIO20

import RPi.GPIO as GPIO
import time

class GameConsole:
        truthtable_7seg =
            [[1,1,1,1,1,1,0],	#0
            [0,1,1,0,0,0,0],	#1
            [1,1,0,1,1,0,1],	#2
            [1,1,1,1,0,0,1],	#3
            [0,1,1,0,0,1,1], 	#4
            [1,0,1,1,0,1,1], 	#5
            [1,0,1,1,1,1,1],	#6
            [1,1,1,0,0,0,0],	#7
            [1,1,1,1,1,1,1],	#8
            [1,1,1,1,0,1,1],	#9
            [1,1,1,0,1,1,1],	#A
            [0,0,1,1,1,1,1],	#b
            [1,0,0,1,1,1,0],	#C
            [0,1,1,1,1,0,1],	#d
            [1,0,0,1,1,1,1],	#E
            [1,0,0,0,1,1,1],	#F
            [1,0,1,1,1,1,1],	#G
            [0,1,1,0,1,1,1],	#H
            [0,1,1,0,0,0,0],	#I
            [0,1,1,1,1,0,0],	#J
            [1,1,1,1,1,1,0],	#O
            [1,1,0,0,1,1,1],	#P
            [1,0,1,1,0,1,1], 	#S
            [0,1,1,1,1,1,0]]	#U

        sevenSeg = []
        def __init__ (self):
                try:
                        GPIO.setmode(GPIO.BCM)


        def release_recources (self):
                gpio.cleanup()

