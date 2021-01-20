# --- Import Libraries --- #
from colorama import Fore, Back, Style, init 
init(convert=True)
from time import sleep
import os
import random
import math
import sys
import copy

# -- Import My Modules -- #
from misc import *
from story import *
from character import *
from shop import *
from travel import * 
from saving import *
from objects import *


def main():
	global me
	global bazaar
	global world
	global battle
	global jobs
	global story
	global save
	start = story.mainMenu(me, save, jobs)
	if start == None:
		pass
	else:
		try:
			loads = save.load(start)
			me = loads[0]
			world = loads[1]
		except:
			print("ERROR LOADING")
	while me.isAlive():
		x = me.menu(battle, world)
		if x is None:
			pass
		else:
			try:
				clear()
				print(Fore.GREEN + "Saving...")
				sleep(1)
				save.save(me, world)
				print("Progress saved")
				sleep(1)
			except Exception as ex:
				print(ex)
				raise
				print("ERROR SAVING")
				sleep(1)

	x = input(">>  ")

main()
