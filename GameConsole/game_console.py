#!/usr/bin/python3
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import random

__piname = ""

def on_message(client, userdata, msg):
	global __piname
	MSG = msg.payload.decode("utf-8")
	test = MSG.split(';')
	if (test[0] == "change"):
		temp = test[1:]
		if (temp[0] != __piname):
			return
		try:
			set_mode(int(temp[2]))
			current_piname = str(temp[0])
			set_player(int(temp[1]))
		except Exception as e:
			print (e)
	elif(MSG[0:7] == "summary"):
		allpinames = MSG.split(';')[1:]

	##################PRIVATE VARIABLES###################
__seven_seg_pins = [17, 27, 22, 10, 9, 11, 5]
__digit_pins = [23, 24, 25, 8]
__mode_leds = [12, 7, 1]
__up_button = 6
__down_button = 26
client = mqtt.Client(client_id="client-4", clean_session=True, userdata=None, protocol=mqtt.MQTTv31)

__player_number = 0
__current_mode = 0
__current_text, allpinames = [" ", " ", " ", " "],[]
__current_DCM = [24,24,24,24]
__current_digit = 0
__truthtable_7seg = [
	[1,1,1,1,1,1,0],	#0
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
	[0,1,1,1,1,1,0],	#U
	[0,0,0,0,0,0,0]]	#Empty

client.on_message = on_message
client.username_pw_set("stef", "stef")
client.connect("rasberrypi.ddns.net", port=1883, keepalive=60)
client.subscribe("project/changeplayer")

	#__________________PRIVATE FUNCTIONS__________________
	###################RELEASE RECOURCES##################
def release_recources ():
	try:
		GPIO.cleanup()
		print ("All cleaned up")
	except RuntimeWarning:
		print ("Well that was a f*cking lie -_-")
	except Exception as e:
		print ("Error release:\n" + str(e))


	######################SEND BUTTONS####################
def __publish_button (channel):
	global client
	global __current_mode
	print ("My mode: " + str(__current_mode))
	if (channel == __up_button):
		client.publish("project/controller", str("up;" + __piname))
	elif (channel == __down_button):
		client.publish("project/controller", str("down;" + __piname))

	###################INITIALIZE PROGRAM#################
try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(__seven_seg_pins, GPIO.OUT)
	GPIO.setup(__digit_pins, GPIO.OUT)
	GPIO.setup(__mode_leds, GPIO.OUT)
	GPIO.setup(__up_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(__down_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(__up_button, GPIO.FALLING, callback=__publish_button, bouncetime=100)
	GPIO.add_event_detect(__down_button, GPIO.FALLING, callback=__publish_button, bouncetime=100)

	client.publish("project/controller", "getsummary")
	random.seed()
	print ("WARNING!\nThis code is under development, use at own risk.")
	tempname = str(random.randrange(100, 999))
	__piname = "pi" + tempname
	print ("Name of Pi= " + __piname)
	client.publish("project/controller", "*jesus has left the chat*")
	client.publish("project/controller", str("hello;"+__piname))

except Exception as e:
	print ("Initialize failed, cleaning up recourses\nError:\n" + str(e))
	release_recources()

	########################SET LEDS######################
def __set_leds ():
	try:
		for i, led in enumerate(__mode_leds):
			if (i == __current_mode):
				GPIO.output(__mode_leds[i], True)
				#print ("led nr {} is nu aan".format(str(i)))
			else:
				GPIO.output(__mode_leds[i], False)
		#print (__current_mode)
	except Exception as e:
		print ("Writing to mode leds failed\nError:\n" + str(e))

	#######################SET DISPLAY####################
def __set_display (digit):
	try:
		for i, digit_pin in enumerate(__digit_pins):
			if (digit == i):
				GPIO.output(__digit_pins[i], False)
				for j,segment in enumerate(__seven_seg_pins):
					GPIO.output(__seven_seg_pins[j], __truthtable_7seg[__current_DCM[digit]][j])
					#continue
			else:
				GPIO.output(__digit_pins[i], True)
	except Exception as e:
		print ("Writing to display failed\nError:\n" + str(e))

	#################TRANSLATE & ENCODE MESSAGE###########
def __translate ():
	global __current_DCM
	for idx,txt  in enumerate(__current_text):
		if (txt.isdigit()):
			__current_DCM[idx] = int(txt)
		elif (txt == "A"):
			__current_DCM[idx] = 10
		elif (txt == "B"):
			__current_DCM[idx] = 11
		elif (txt == "C"):
			__current_DCM[idx] = 12
		elif (txt == "D"):
			__current_DCM[idx] = 13
		elif (txt == "E"):
			__current_DCM[idx] = 14
		elif (txt == "F"):
			__current_DCM[idx] = 15
		elif (txt == "G"):
			__current_DCM[idx] = 16
		elif (txt == "H"):
			__current_DCM[idx] = 17
		elif (txt == "I"):
			__current_DCM[idx] = 18
		elif (txt == "J"):
			__current_DCM[idx] = 19
		elif (txt == "O"):
			__current_DCM[idx] = 20
		elif (txt == "P"):
			__current_DCM[idx] = 21
		elif (txt == "S"):
			__current_DCM[idx] = 22
		elif (txt == "U"):
			__current_DCM[idx] = 23
		else:
			__current_DCM[idx] = len(__truthtable_7seg)-1

	#__________________PUBLIC FUNCTIONS___________________
	#######################SET PLAYER#####################
def set_player (number):
	global __player_number
	__player_number = number
	display_player()
	__translate()

	########################SET MODE######################
def set_mode (number):
	global __current_mode
	if (number < 0 or number > 3):
		print ("Mode number was set too high or too low")
	else:
		__current_mode = number

	#####################DISPLAY PLAYER###################
def display_player ():
	global __current_text
	__current_text = [" ", " ", "P", str(__player_number)]
	__translate()

	#####################DISPLAY TEXT#####################
def display_text (input_text):
	if (isisnstance(input_text, str)):
		if (len(input_text) < 0 or len(input_text) > 4):
			print ("Text input was too long or too short")
		else:
			__temp_list = list(input_text.split())
			for item in __temp_list:
				if (not item.isdigit()):
					item.upper()
			if (len(__temp_list) < 4):
				for item in range(4-len(__temp_list)):
					__temp_list.append(" ")
			__translate()
	else:
		print ("Text input was not set as string")
	########################UPDATE########################
def update():
	global __current_digit
	__current_digit = __current_digit + 1
	if (__current_digit > 3):
		__current_digit = 0
	__set_leds()
	__set_display(__current_digit)
	time.sleep(0.005)

client.loop_start()
while (True):
	update()
	#print ("looped")
###########################END OF CODE################################
