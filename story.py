# --- Import Libraries --- #
from colorama import Fore, Back, Style
import random, math
from time import sleep
import json

# -- My Modules -- #
from misc import *
from saving import *

save = SaveSystem
# Lets see if i can encapsulate all story functions into one object
class Story:
	def intro(self):
		print(Fore.GREEN + "The world has been ravaged by a virus, infecting people at an alarmingly high rate...")
		sleep(2)
		space(1)
		print("Those who are infected are turned into the "+Fore.RED+"Living Dead"+Fore.GREEN+" when they die...")
		sleep(2)
		space(1)
		print("Although there have been some advancements to stop the virus, but it got out of control before a cure could be found...")
		sleep(2)
		space(1)
		print("The world has been destroyed as we once knew it. It is filled with the "+Fore.RED+"Undead"+Fore.GREEN+" and equally dangerous factions of survivors...")
		sleep(2)
		space(1)
		print("Do you have what it takes to survive?" + Fore.BLUE)
		sleep(2)
		space(1)
		x = input(">>  ")
	def pickJob(self, player, jobList):
		space(1)
		print(Fore.GREEN + "What kind of character are you, "+Fore.BLUE+player.name+Fore.GREEN+"?")
		x = 1
		for charType in jobList:
			print(Fore.YELLOW + str(x) + ". " + str(charType))
			x += 1
		print(Fore.BLUE + "")
		try:
			choice = int(input(">> "))
			chosen = jobList[(choice - 1)]
			player.job = chosen
			player.jobSet()
		except Exception as ex:
			print(ex)
			raise

	def createCharacter(self, player, jobs):
		space(1)
		print(Fore.GREEN + "What is your name?" + Fore.BLUE)
		names = input(">>  ")
		player.name = names
		print(Fore.GREEN + "Welcome, " + Fore.BLUE + player.name + Fore.GREEN + "!")
		sleep(1)
		self.pickJob(player, jobs)

	def mainMenu(self, player, save, jobs):
		flag = 1
		while flag == 1:
			clear()
			print(Fore.RED + " ### --- "+ Fore.GREEN + "Apocalypse: Zombie Survival RPG "+ Fore.RED +"--- ###")
			print(Fore.RED + " ### --- "+ Fore.GREEN + "     Can You Survive?    "+ Fore.RED +"--- ###")
			space(2)
			print(Fore.YELLOW + "1. " + Fore.WHITE + "New Game" )
			print(Fore.YELLOW + "2. " + Fore.WHITE + "Load Game" + Fore.BLUE )

			try:
				choice = int(input(">>  "))
				if choice == 1:
					flag = 0
					clear()
					self.intro()
					self.createCharacter(player, jobs)
					return None

				elif choice == 2:
					clear()
					load = save.loadScreen()
					return load
				else:
					print(Fore.RED + "Unrecognized input!")
					sleep(1)
			except Exception as ex:
				print(ex)
				raise


