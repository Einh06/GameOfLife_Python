#!/usr/bin/python

# file that handle UI display (in console) for the project the game of life

from engine import World
from Tkinter import *

import os, time

def quickSimulation():
		"""
		Lunch a quick simulation.
		"""

		world = World()
		print(world)
		while True:
			time.sleep(1)
			world.iterate()
			print(world)


def advanceSimulation():
	"""
	Lunch an advance simulation.
	"""
	pass

def detail():
	"""
	Show the detail regarding the game of life.
	"""

	print("Who cares?!")

def credits():
	"""
	Show the credits of the game of life.
	"""

	print("Who cares?!")

def checkMainOption(choice):
	"""
	Check the choice done in the main option and continue in concequences.
	"""

	if choice == 1:
		quickSimulation()
	elif choice == 2:
		advanceSimulation()
	elif choice == 3:
		detail()
	elif choice == 4:
		credits()
	else:
		exit()


print("Welcome to the game of life")

print("1 - Quick simulation")
print("2 - Advance simulation")
print("3 - Regarding the game of life")
print("4 - Credits")
print("5 - Quit")

inp = input()

while inp:

	if int(inp) < 0 or int(inp) > 5:
		print("Option between 0 and 5")
	else:
		checkMainOption(inp)

	inp = input()

