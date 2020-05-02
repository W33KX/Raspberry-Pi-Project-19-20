#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

class GameConsole:
	##################PRIVATE VARIABLES###################
	__seven_seg_pins = [17, 27, 22, 10, 9, 11, 5]
	__digit_pins = [23, 24, 25, 8]
	__mode_leds = [7, 1, 12]
	__up_button = 6
	__down_button = 26

	__player_number = 0
	__current_mode = 0
	__current_text = [" ", " ", " ", " "]
	__current_DCM = [24,24,24,24]
	__current_digit = 0

	__truthtable_7seg =
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


	#__________________PRIVATE FUNCTIONS__________________
	###################INITIALIZE PROGRAM#################
	def __init__ (self):
		try:
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(__seven_seg_pins, GPIO.OUT)
			GPIO.setup(__digit_pins, GPIO.OUT)
			GPIO.setup(__mode_leds, GPIO.OUT)
			GPIO.setup(__up_button, GPIO.IN)
			GPIO.setup(__down_button, GPIO.IN)
			print ("WARNING!\nThis code is under development, use at own risk.")
		except Exception as e:
			print ("Initialize failed, cleaning up recourses\nError:\n" + str(e))
			release_recources()

	########################SET LEDS######################
	def __set_leds (self):
		try:
			for i, led in enumerate(__mode_leds):
				if (i+1 == __current_mode):
					GPIO.output(__mode_leds[i], True)
				else:
					GPIO.output(__mode_leds[i], False)
		except Exception as e:
			print ("Writing to mode leds failed\nError:\n" + str(e))

	#######################SET DISPLAY####################
	def __set_display (self, digit):
		try:
			#code will be continued
		except Exception as e:
			print ("Writing to display failed\nError:\n" + str(e))

	#################TRANSLATE & ENCODE MESSAGE###########
	def __translate (self):
		for i in __current_text:
			if (i.isdigit()):
				__current_DCM[ = int(i)
			elif (i = "A"):
				__current_DCM = 10
                        elif (i = "B"):
                                __current_DCM = 10
                        elif (i = "C"):
                                __current_DCM = 10
                        elif (i = "D"):
                                __current_DCM = 10
                        elif (i = "E"):
                                __current_DCM = 10
                        elif (i = "F"):
                                __current_DCM = 10
                        elif (i = "G"):
                                __current_DCM = 10
                        elif (i = "H"):
                                __current_DCM = 10
                        elif (i = "I"):
                                __current_DCM = 10
                        elif (i = "J"):
                                __current_DCM = 10
                        elif (i = "O"):
                                __current_DCM = 10
                        elif (i = "P"):
                                __current_DCM = 10
                        elif (i = "S"):
                                __current_DCM = 10
                        elif (i = "A"):
                                __current_DCM = 10
			else:
				__current_DCM[i] = __truthtable_7seg[len(__truthtable_7seg)]

	#__________________PUBLIC FUNCTIONS___________________
	#######################SET PLAYER#####################
	def set_player (self, number):
		if (number.isdigit()):
			__player_number = number
		else:
			print ("Player was not set as a number")

	########################SET MODE######################
	def set_mode (self, number):
		if (number.isdigit()):
			if (number < 0 or number > 3):
				print ("Mode number was set too high or too low")
			else:
				__current_mode = number
		else:
			print ("Mode was not set as a number")

	######################GET UP-BUTTON###################
	def get_up_button (self):
		try:
			return GPIO.input(__up_button)
		except Exception as e:
			print ("Read unsuccessful\nError:\n" + str(e))
			return False

	#####################GET DOWN-BUTTON##################
	def get_down_button (self):
		try:
			return GPIO.input(__down_button)
		except Exception as e:
			print ("Read unsuccessful\nError\n" + str(e))
			return False

	#####################DISPLAY PLAYER###################
	def display_player (self):
		if (__player_number > 0):
			print ("You need to set the player number first")
		else:
			__current_text = [" ", " ", "P", str(__player_number)]
	#####################DISPLAY TEXT#####################
	def display_text (self, input_text):
		if (isisnstance(input_text, str)):
			if (len(input_text) < 0 or len(input_text) > 4):
				print ("Text input was too long or too short")
			else:
				__temp_list = list(input_text.split())
				for item in __temp_list:
					if (not item.isdigit()):
						item.upper()
				if (len(__temp_list) < 4)):
					for (item in range((4-len(__temp_list)):
						__temp_list.append(" ")
		else:
			print ("Text input was not set as string")

	########################UPDATE########################
	def update (self):
		__current_digit = __current_digit + 1
		if (__current_digit >= 4)
			__current_digit = 0

	###################RELEASE RECOURCES##################
	def release_recources (self):
		try:
			GPIO.cleanup()
			print ("All cleaned up")
		except RuntimeWarning:
			print ("Well that was a f*cking lie -_-")
		except Exception as e:
			print ("Error release:\n" + str(e))

#########################END OF CODE################################
