# -- Functions related to the map and travelling -- #
from colorama import Fore, Back, Style
import random, math
from time import sleep
# -- My Modules -- #
from misc import *

# So we will do a  base class for all locations. Then the most common: Searchable and explorable locations. Then a location you have to fight your way through. Finally, a 
# friendly location class

# NOTE: Cannot do the same locations for map it looks like because they all just reference the same object. Need to remember
# -- Base Class -- #
class Place:
	def __init__(self, name, description):
		self.name = name
		self.description = description
	
# -- Searchable and Explorable Location -- #
class Location(Place):
	def __init__(self, name, description, clear, search, limit, enemy, loot, encounter, maxE):
		super().__init__(name, description)
		self.clear = clear
		self.search = search
		self.limit = limit
		self.enemy = enemy
		self.loot = loot
		self.encounter = encounter
		self.maxE = maxE
	def searchPerc(self):
		perc = math.ceil((self.search / self.limit) * 100)
		if perc >= 75:
			text = Fore.GREEN + str(perc) + Fore.GREEN + " %"
			return text
		elif perc >= 35 and perc < 75:
			text = Fore.YELLOW + str(perc) + Fore.GREEN + " %"
			return text
		elif perc >= 15 and perc < 35:
			text = Fore.RED + str(perc) + Fore.GREEN + " %"
			return text
		elif perc < 15:
			text = Fore.MAGENTA + str(perc) + Fore.GREEN + " %"
			return text
	def __str__(self):
		searchPercentage = self.searchPerc()
		if self.clear is False:
			text = Fore.WHITE + "Name: " + Fore.YELLOW + self.name + Fore.WHITE + "\nDescription: " + Fore.YELLOW + self.description + Fore.WHITE + "\nSearched: " + searchPercentage
		else:
			text = Fore.WHITE + "Name: " + Fore.GREEN + self.name + Fore.WHITE + "\nDescription: " + Fore.YELLOW + self.description + Fore.WHITE + "\nSearched: " + searchPercentage
		return text
	def searched(self, player, battle):
		if self.clear is True:
			print(Fore.RED + "You have already completely searched this area!")
			sleep(0.5)
		else:
			# Test if ambushed
			chance = random.randint(1, 100)
			# Skill Bonus
			bonus = math.ceil(player.dexterity / 3)
			chance -= bonus
			if chance > self.encounter:
				print(Fore.RED + "You have been ambushed!")
				sleep(1)
				battle.encounter(self.maxE, self.enemy, player)
			else:
				self.search += 1
				loots = random.choice(self.loot)
				if loots == "Nothing":
					print(Fore.GREEN + "You found " + Fore.BLUE + "nothing" + Fore.GREEN + "!")
				elif loots == "Credits":
					credit = random.randint(1, 20)
					print(Fore.GREEN + "You found " + Fore.BLUE + str(credit) + " credits" + Fore.GREEN + "!")
					player.credits += credit
				else:
					print(Fore.GREEN + "You found a " + Fore.BLUE + loots.name + Fore.GREEN + "!")
					player.inventory.append(loots)
				sleep(1)
				if self.search == self.limit:
					print(Fore.BLUE + "You have completely searched this area!")
					self.clear = True
					sleep(1)

# -- Battle Location -- #
class Warzone(Place):
	def __init__(self, name, description, clear, heads, enemy, prize):
		super().__init__(name, description)
		self.clear = clear
		self.heads = heads
		self.enemy = enemy
		self.prize = prize
	def __str__(self):
		if self.clear is False:
			text = Fore.WHITE + "Name: " + Fore.MAGENTA + self.name + Fore.WHITE + "\nDescription: " + Fore.YELLOW + self.description + Fore.WHITE + "\nEnemies: " + Fore.RED + str(self.heads) + " Left"
		else:
			text = Fore.WHITE + "Name: " + Fore.GREEN + self.name + Fore.WHITE + "\nDescription: " + Fore.YELLOW + self.description + Fore.WHITE + "\nEnemies: " + Fore.RED + str(self.heads) + " Left"
		return text
	def searched(self, player, battle):
		if self.clear is True:
			print(Fore.RED + "You have already completely cleared this area!")
			sleep(0.5)
		else:
			# self, number, enemyList, player
			total = battle.eliminate(self.heads, self.enemy, player)
			self.heads -= total
			print(Fore.GREEN + "You killed " + Fore.RED + str(total) + " enemys" + Fore.GREEN + "!")
			sleep(1)
			if self.heads == 0:
				print(Fore.BLUE + "You have cleared out the area!")
				print(Fore.GREEN + "You found a " + self.prize.name + "!")
				player.inventory.append(self.prize)
				self.clear = True
				sleep(1)


# -- Friendly Places -- #
# I will do specific ones for this one
# A home base will be it's own file and functions
class Trader(Place):
	def __init__(self, name, description, inv):
		super().__init__(name, description)
		self.inv = inv
	def __str__(self):
		text = Fore.WHITE + "Name: " + Fore.GREEN + self.name + Fore.WHITE + "\nDescription: " + Fore.GREEN + self.description
		return text


