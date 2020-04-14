#!/usr/bin/python3
import RPi.GPIO as gpio
import time
import atexit

class GameConsole:
	def __init__ (self):
		

	def release_recources (self):
		gpio.cleanup()
