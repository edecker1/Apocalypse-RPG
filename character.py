
# -- Import Statements -- #
from colorama import Fore, Back, Style
import random
import math
from time import sleep
import json
# -- My Modules -- #
from misc import *
from travel import *
from items import *

class Character:
	""" Base Character class used for enemies, players, and maybe survivors """
	def __init__(self, name, hp, maxHp):
		self.name = name
		self.hp = hp
		self.maxHp = maxHp
	def isAlive(self):
		if self.hp <= 0:
			return False
		else:
			return True
	@classmethod
	def fromJson(cls, jsonString):
		dictObj = json.loads(jsonString, object_hook = Character)
		return cls(*dictObj)


class Enemy(Character):
	""" This class will be the base for all enemies """
	def __init__(self, name, hp, maxHp, attacks, loot, xp):
		super().__init__(name, hp, maxHp)
		self.attacks = attacks
		self.loot = loot
		self.xp = xp
	def __iter__(self):
		return self
	def __next__(self):
		return self
	def __str__(self):
		text = Fore.RED + self.name
		return text
	def setHealth(self):
		""" This will set the health when this enemy is fought to some random exten """
		half = math.ceil(self.maxHp / 2)
		current = random.randint(half, self.maxHp)
		self.hp = current
	def chooseAttack(self):
		attack = random.choice(self.attacks)
		return attack
	def attacking(self, target, attack):
		""" Attack function in battle. Choose a random attack and do it """
		damage = attack.damage()
		damage -= target.armor.defense
		if damage == 0:
			# This way it at leasts does 1 damage
			damage = 1
		print(Fore.RED + self.name + Fore.MAGENTA + " " + attack.command + Fore.BLUE + " " + target.name + Fore.GREEN + " for " + Fore.RED + str(damage) + " damage" + Fore.GREEN + "!")
		sleep(1)
		target.hp -= damage
		if attack.infection != 0:
			infect = attack.infection
			disease = random.randint(1, infect)
			target.contamination += disease
	def expCalc(self, target):
		exp = random.randint(3, self.xp)
		#print(Fore.BLUE + "You " + Fore.GREEN + " have gained " + Fore.CYAN + str(exp) + " experience points!")
		target.experience += exp
		return exp


class Player(Character):
	""" This Class is for the player object. Will have all functions related to player actions """
	def __init__(self, name, hp, maxHp, contamination, inventory, weapon, armor, credits, coordinates, level, cap, experience, job, strength, dexterity, endurance):
		super().__init__(name, hp, maxHp)
		self.contamination = contamination
		self.inventory = inventory
		self.weapon = weapon
		self.armor = armor
		self.credits = credits
		self.coordinates = coordinates
		self.level = level
		self.cap = cap
		self.experience = experience
		self.job = job
		self.strength = strength
		self.dexterity = dexterity
		self.endurance = endurance
	def __str__(self):
		return Fore.BLUE + self.name
	def __repr__(self):
		return 'Player(Name: {}, hp: {} / {}, contamination: {}%, inventory: {}, weapon: {}, armor: {}, credits: {}, coordinates: {}, level: {}, cap: {}, experience: {}, job: {}, strength: {}, dexterity: {}, endurance: {})'.format(self.name, self.hp, self.maxHp, self.contamination, self.inventory, self.weapon, self.armor, self.credits, self.coordinates, self.level, self.cap, self.experience, self.job, self.strength, self.dexterity, self.endurance)
	def isZombie(self):
		if self.contamination >= 100:
			return True
		else:
			return False
	def levelCheck(self):
		if self.experience >= (self.cap[self.level]):
			print(Fore.BLUE + "You" + Fore.GREEN + " have leveled up!")
			self.experience -= self.cap[self.level]
			self.level += 1
	def jobSet(self):
		self.strength = self.job.strength
		self.dexterity = self.job.dexterity
		self.endurance = self.job.endurance
	def returnHealth(self):
		perc = math.ceil( ((self.hp / self.maxHp) * 100) )
		if perc >= 75:
			text = Fore.GREEN + str(self.hp) + Fore.GREEN + " / " + str(self.maxHp)
			return text
		elif perc >= 35 and perc < 75:
			text = Fore.YELLOW + str(self.hp) + Fore.GREEN + " / " + str(self.maxHp)
			return text
		elif perc >= 15 and perc < 35:
			text = Fore.RED + str(self.hp) + Fore.GREEN + " / " + str(self.maxHp)
			return text
		elif perc < 15:
			text = Fore.MAGENTA + str(self.hp) + Fore.GREEN + " / " + str(self.maxHp)
			return text
	def returnCont(self):
		perc = self.contamination
		if perc < 25:
			text = Fore.GREEN + str(self.contamination) + " %"
			return text
		elif perc >= 26 and perc < 65:
			text = Fore.YELLOW + str(self.contamination) + Fore.GREEN + " %"
			return text
		elif perc >= 66 and perc < 95:
			text = Fore.RED + str(self.contamination) + Fore.GREEN + " %"
			return text
		elif perc >= 95:
			text = Fore.MAGENTA + str(self.contamination) + Fore.GREEN + " %"
			return text
	""" Functions Related to Items """
	def useItem(self, item):
		if (isinstance(item, Usable)):
			if item.attribute == 'hp':
				difference = (self.hp + item.benefit)
				if difference <= self.maxHp:
					self.hp += item.benefit
					print(Fore.BLUE + "You healed for " + Fore.GREEN + str(item.benefit) + Fore.BLUE + "!") 
					self.inventory.remove(item)
				else:
					self.hp = self.maxHp
					print(Fore.BLUE + "You completely healed!") 
					self.inventory.remove(item)

			elif item.attribute == 'c':
				difference = (self.contamination - item.benefit)
				if difference >= 0:
					self.contamination -= item.benefit
					print(Fore.BLUE + "You decontaminated by " + Fore.GREEN + str(item.benefit) + "%" + Fore.BLUE + "!")
					self.inventory.remove(item)
				else:
					self.contamination = 0
					print(Fore.BLUE + "You are completely decontaminated!") 
					self.inventory.remove(item)
		else:
			print(Fore.RED + "You cannot use that item!")
	def unequip(self, item):
		if (isinstance(item, Weapon)):
			self.inventory.append(item)
			self.weapon = ''
		elif (isinstance(item, Armor)):
			self.inventory.append(item)
			self.armor = ''
		elif (item == ''):
			pass
		else:
			print(Fore.RED + "Cannot uneqip item!")
	def equipItem(self, item):
		if item in self.inventory:
			if (isinstance(item, Weapon)):
				self.inventory.remove(item)
				self.unequip(self.weapon)
				self.weapon = item
			elif (isinstance(item, Armor)):
				self.inventory.remove(item)
				self.unequip(self.armor)
				self.armor = item
			else:
				print(Fore.RED + "Cannot equip this item!")
		else:
			print(Fore.RED + "You do not have this item in your inventory!")
	def showInv(self):
		print(Fore.BLUE + "|| -- Inventory -- || ")
		x = 1
		if not self.inventory:
			print(Fore.RED + "You do not have anything in your inventory!")
		else:
			for item in self.inventory:
				print(Fore.GREEN + str(x) + ". " + str(item))
				x += 1
	def sellingInv(self):
		x = 1
		if not self.inventory:
			print(Fore.RED + "You do not have anything in your inventory!")
		else:
			for item in self.inventory:
				print(item.sellPrice(x))
				x += 1 
	def showEquipped(self):
		# Check weapon then armor
		space(1)
		if self.weapon == '':
			print(Fore.GREEN + "Weapon: " + Fore.RED + "Nothing Equipped")
		else:
			print(Fore.GREEN + "Weapon: " + Fore.BLUE + str(self.weapon.name))
		space(1)
		if self.armor == '':
			print(Fore.GREEN + "Armor: " + Fore.RED + "Nothing Equipped")
		else:
			print(Fore.GREEN + "Armor: " + Fore.BLUE + str(self.armor.name))
	""" Functions Related to Shop """
	def buyItem(self, item):
		cost = item.price()
		if self.credits < cost:
			print(Fore.RED + "Not enough money!")
		else:
			self.credits -= cost
			self.inventory.append(item)
			print(Fore.BLUE + "You bought " + Fore.GREEN + item.name + Fore.BLUE + " for " + Fore.YELLOW + str(cost) + " credits" + Fore.BLUE + "!") 
	def sellItem(self, item):
		if item in self.inventory:
			print(Fore.BLUE + "Sold " + item.name + " for " + str(item.value) + " credits!")
			self.inventory.remove(item)
			self.credits += item.value
		else:
			print(Fore.RED + "Item not in inventory!")
	""" Functions related to inventory management """
	def equipScreen(self):
		flag = 1
		while flag == 1:
			clear()
			self.showEquipped()
			self.showInv()
			space(1)
			print(Fore.GREEN + "Which item would you like to equip? Type "+Fore.YELLOW+"0"+Fore.GREEN+" to go back")
			print(Fore.BLUE + "")
			choice = int(input(">>  "))
			try:
				if choice == 0:
					flag == 0
					break
				else:
					index = choice - 1
					target = self.inventory[index]
					self.equipItem(target)
			except Exception as ex:
				 print(ex)
				 raise
	def useScreen(self):
		flag = 1
		while flag == 1:
			clear()
			self.showInv()
			print(Fore.GREEN + "Which item would you like to use? Type "+Fore.YELLOW+"0"+Fore.GREEN+" to go back")
			print(Fore.BLUE + "")
			space(1)
			choice = int(input(">>  "))
			try:
				if choice == 0:
					flag == 0
					break
				else:
					target = self.inventory[(choice - 1)]
					self.useItem(target)
			except Exception as ex:
				 print(ex)
				 raise
	def inventoryScreen(self):
		flag = 1
		while flag == 1:
			clear()
			self.showInv()
			self.showEquipped()
			space(1)
			print(Fore.GREEN + "What would you like to do?")
			print(Fore.YELLOW + "1. "+Fore.WHITE+"Equip Item")
			print(Fore.YELLOW + "2. "+Fore.WHITE+"Use Item")
			print(Fore.YELLOW + "3. "+Fore.WHITE+"Go back")
			print(Fore.BLUE + "")

			try:
				choice = int(input(">>  "))
				if choice == 3:
					flag = 0
					break
				elif choice == 1:
					self.equipScreen()
				elif choice == 2:
					self.useScreen()
			except Exception as ex:
				 print(ex)
				 raise
	""" Traveling Functions """
	def getLoc(self, world):
		return world[self.coordinates]
	def locHUD(self, world):
		current = self.getLoc(world)
		print(current)
	def travel(self, direction):
		if direction.lower() == 'n':
			if self.coordinates < 10:
				print(Fore.RED + "Cannot travel further North!")
				sleep(0.5)
			else:
				self.coordinates -= 10
				print(Fore.BLUE + "You travelled North!")
				sleep(0.5)
		elif direction.lower() == 's':
			if self.coordinates > 40:
				print(Fore.RED + "Cannot travel further South!")
				sleep(0.5)
			else:
				self.coordinates += 10
				print(Fore.BLUE + "You travelled South!")
				sleep(0.5)
		elif direction.lower() == 'w':
			if (self.coordinates % 10) == 1:
				print(Fore.RED + "Cannot travel further West!")
				sleep(0.5)
			else:
				self.coordinates -= 1
				print(Fore.BLUE + "You travelled West!")
				sleep(0.5)
		elif direction.lower() == 'e':
			if (self.coordinates % 10) == 8:
				print(Fore.RED + "Cannot travel further East!")
				sleep(0.5)
			else:
				self.coordinates += 1
				print(Fore.BLUE + "You travelled East!")
				sleep(0.5)
		else:
			print(Fore.RED + "Invalid input")
			sleep(0.5)
	""" Battle Functions """
	def attacking(self, target):
		try:
			damage = self.weapon.damage()
		except:
			damage = random.randint(1, 3)
		# Stat Bonus
		bonus = math.ceil(self.strength / 3)
		damage += bonus 
		if self.weapon == '':
			print(Fore.BLUE + self.name + Fore.MAGENTA + " punches" + Fore.RED + " " + target.name + Fore.GREEN + " for " + Fore.RED + str(damage) + " damage" + Fore.GREEN + "!")
		else:
			print(Fore.BLUE + self.name + Fore.MAGENTA + " " + self.weapon.action + Fore.RED + " " + target.name + Fore.GREEN + " with " + Fore.BLUE + "[ " + self.weapon.name +" ]"+Fore.GREEN+" for " + Fore.RED + str(damage) + " damage" + Fore.GREEN + "!")
		sleep(1)
		target.hp -= damage

	""" Main Functions """
	def hud(self, world):
		print(Fore.WHITE + "Name: " + Fore.BLUE + self.name)
		print(Fore.WHITE + "Level: " + Fore.GREEN + str(self.level))
		healthText = self.returnHealth()
		print(Fore.WHITE + "Health: " + healthText)
		contaminationText = self.returnCont()
		print(Fore.WHITE + "Contamination: " + contaminationText)
		self.locHUD(world)
		space(1)
	def travelMenu(self, world):
		clear()
		flag = 1
		while flag == 1:
			clear()
			self.hud(world)
			print(Fore.GREEN + "Where do you want to go to?")
			print("Type "+Fore.YELLOW+"'n'"+Fore.GREEN+" to go north, "+Fore.YELLOW+"'s'"+Fore.GREEN+" to go south, "+Fore.YELLOW+"'e'"+Fore.GREEN+" to go east, "+Fore.YELLOW+"'w'"+Fore.GREEN+" to go west, "+Fore.RED+"0"+Fore.GREEN+" to stop")
			print("" + Fore.BLUE)
			choice = input(">>  ")

			try:
				if choice == '0':
					flag = 0
				else:
					self.travel(choice)
			except:
				print("error")
	def menu(self, battle, world):
		clear()
		self.hud(world)
		current = self.getLoc(world)
		print(Fore.GREEN + "What would you like to do?")
		print(Fore.YELLOW + "1. " + Fore.WHITE + "Travel")
		print(Fore.YELLOW + "2. " + Fore.WHITE + "View Inventory")
		if isinstance(current, Trader):
			print(Fore.YELLOW + "3. " + Fore.WHITE + "Trade")
		elif isinstance(current, Location):
			print(Fore.YELLOW + "3. " + Fore.WHITE + "Search")
		else:
			print(Fore.YELLOW + "3. " + Fore.WHITE + "Raid")
		print(Fore.YELLOW + "4. " + Fore.WHITE + "Save")
		print(" " + Fore.BLUE)
		choice = int(input(">>  "))
		try:
			if choice == 1:
				clear()
				self.hud(world)
				self.travelMenu(world)
			elif choice == 2:
				clear() 
				self.hud(world)
				self.inventoryScreen()
			elif choice == 3:
				if isinstance(current, Trader):
					current.inv.mainInterface(self)
				else:
					current.searched(self, battle)
			elif choice == 4:
				clear()
				return 1 
				
			else:
				print("Invalid input")

		except Exception as ex:
			print(ex)
			raise
		
class Job:
	""" This will give bonuses to the player, but mainly be used for survivors when they are implemented """
	def __init__(self, name, description, strength, dexterity, endurance):
		self.name = name
		self.description = description
		self.strength = strength
		self.dexterity = dexterity
		self.endurance = endurance
	def __str__(self):
		text = Fore.WHITE + self.name + Fore.GREEN + " ---> " + Fore.MAGENTA + self.description
		return text

