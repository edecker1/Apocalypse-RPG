# --- Import Libraries --- #
from colorama import Fore, Back, Style
import random, math
from time import sleep
# -- Import My Modules -- #
from misc import *
from character import *

class Attack:
	""" This class will be the base for attacks without weapons """
	def __init__(self, name, command, qDice, die, chance, infection):
		self.name = name
		self.command = command
		self.qDice = qDice 
		self.die = die
		self.chance = chance
		self.infection = infection
	def damage(self):
		total = 0
		for x in range(self.qDice):
			diceRoll = random.randint(1, self.die)
			total += diceRoll
		return total

class Battle:
	""" This will be the main driving object to determine battle """
	def __init__(self, enemies, loot, credits, xp, killCount):
		self.enemies = enemies
		self.loot = loot
		self.credits = credits
		self.xp = xp
		self.killCount = killCount
	def add(self, enemy):
		""" This will take an array so that you can bring in mulitple enemies """
		self.enemies.append(enemy)
	def delete(self, enemy, player):
		""" Deletes enemy and prints out death message """
		print(Fore.RED + enemy.name + Fore.GREEN + " has been killed!")
		self.killCount += 1
		winnings = random.choice(enemy.loot)
		if winnings == "Nothing":
			pass
		elif winnings == "Credits":
			credit = random.randint(1, 10)
			self.credits += credit
			#print(Fore.GREEN + "You found " + Fore.BLUE + str(credit) + " credits" + Fore.GREEN + "!")
			player.credits += credit
		else:
			player.inventory.append(winnings)
			self.loot.append(winnings)
			#print(Fore.BLUE + "You " + Fore.GREEN + "found a " + Fore.BLUE + str(winnings.name) + Fore.GREEN + "!")
		self.xp += enemy.expCalc(player)
		self.enemies.remove(enemy)
		sleep(1)
	def deathCheck(self, player):
		""" Checks if any enemies died at end of turn. May get rid of for more efficient means """
		for enemy in self.enemies:
			if enemy.isAlive() == False:
				self.delete(enemy, player)
	def enemySetup(self):
		""" This sets up the enemy health """
		for enemy in self.enemies:
			enemy.setHealth()
	def hud(self, player):
		""" The HUD for battles """
		print(Fore.GREEN + "Name: " + Fore.BLUE + player.name)
		print(Fore.GREEN + "Health: " + Fore.YELLOW + str(player.hp) + Fore.GREEN + " / " + Fore.YELLOW + str(player.maxHp))
		print(Fore.GREEN + "Contamination: " + Fore.YELLOW + str(player.contamination) + Fore.GREEN + " %")
		print(Fore.CYAN + " -- Versus -- ")
		for villain in self.enemies:
			print(Fore.RED + villain.name + Fore.GREEN + " -- " + Fore.MAGENTA + str(villain.hp) + " health")
	def gameOver(self, player):
		""" Game Over Page """
		clear()
		print(Fore.RED + "You have died!")
		if player.isAlive() == False:
			print("You were killed!")
		if player.isZombie() == True:
			print(Fore.MAGENTA + "You were turned into a zombie! \nYou have now become one of the mindless monsters you spent so long fighting...")
		print(Fore.BLUE + "")
		x = input(">>  ")
	def fleeScreen(self):
		""" Screen When Fleeing """
		clear()
		print(Fore.BLUE + "You have fleed!")
		print(+Fore.BLUE+"You"+Fore.GREEN+" are safe... for now."+Fore.BLUE)

		choice = input(">>  ")
	def victory(self, player):
		""" Victory page """
		clear()
		print(Fore.BLUE + "You are victorious!")
		player.levelCheck()
		print(Fore.BLUE + "You"+Fore.GREEN+" have defeated all of "+Fore.BLUE+"your"+Fore.GREEN+" enemies! "+Fore.BLUE+"You"+Fore.GREEN+" are safe... for now."+Fore.BLUE)
		print("You gained " + Fore.WHITE + "{}" + Fore.BLUE + " experience points!".format(self.xp))
		if not self.loot:
			pass
		else:
			for item in self.loot:
				print("You found a [ {} ]!".format(item.name))
		print("\nYou found "+str(self.credits)+" credits!")

		choice = input("\n>>  ")
	def start(self, player):
		""" Thsi will set up the battle """
		clear()
		print(Fore.BLUE + "You " + Fore.GREEN + "enter " + Fore.RED + "battle" + Fore.GREEN + "!")
		sleep(1)
		self.enemySetup()
		self.loot.clear()
		self.credits = 0
	def attackHit(self, player):
		""" This will decicde if the attack goes through
			This will either take the player object or the attack object
			return False if it misses, return True if it hits
			 """
		chance = random.randint(1, 100)
		# If the player 
		if (isinstance(player, Player)):
			if self.weapon == '':
				# If nothing equipped, flat chance of 80
				if chance > 80:
					return False
				else:
					return True
			else:
				if chance > self.weapon.chance:
					return False
				else:
					return True
		# For enemies I will put through the attack itself.
		else:
			if chance > player.chance:
				return False
			else:
				return True
	def flee(self, flag):
		""" Action for player to try and flee
		Will be increasingly hard for more enemies
		1 - 60 %
		2 - 70 %
		3 - 80 %
		4 - 90 %
		5 - impossible 
		"""
		enemyCount = ( len(self.enemies) - 1 )
		difficulty = 60 + (10 * enemyCount)
		chance = random.randint(1, 100)
		if chance > difficulty:
			print(Fore.GREEN + "You have successfully fleed!")
			sleep(1)
			self.enemies.clear()
			flag == 1
		else:
			print(Fore.RED + "You tried fleeing but you fail!")
			sleep(1)
		return flag
	def chooseTarget(self):
		""" This function will choose the target for the player """
		print(Fore.GREEN + "Who will you attack?")
		x = 1
		for villain in self.enemies:
			print(Fore.YELLOW + str(x) + ". " + Fore.RED + villain.name)
			x += 1
		print(Fore.BLUE + "")
		try:
			choice = int(input(">> "))
			choice -= 1
			targ = self.enemies[choice]
			return targ
		except:
			print(Fore.RED + "Invalid input! Choosing first target")
			return self.enemies[0]

	def playerTurn(self, player, flag):
		""" Player's Turn """
		clear()
		print(Fore.GREEN + "It's "+Fore.BLUE+"your"+Fore.GREEN+" turn!")
		self.hud(player)
		space(1)
		print(Fore.GREEN + "What would you like to do?")
		print(Fore.YELLOW + "1. Attack")
		print("2. Run Away")
		count = len(self.enemies)
		print(Fore.BLUE + "")
		try:
			choice = int(input(">>  "))
			if choice == 1:
				if count == 1:
					current = self.enemies[0]
					player.attacking(current)
					self.deathCheck(player)
					return None
				else:
					current = self.chooseTarget()
					player.attacking(current)
					self.deathCheck(player)
					return None
			elif choice == 2:
				flag = self.flee(flag)
				return flag
			else:
				print(Fore.RED+"Invalid Input!")
				print("You falter!")
				sleep(1)
				return None
		except Exception as ex:
			print(ex)
			raise

	def enemyTurn(self, player):
		""" Enemy turn """
		clear()
		print(Fore.GREEN + "It's the "+Fore.RED+"enemy's"+Fore.GREEN+" turn!")
		self.hud(player)
		sleep(0.5)
		for enemy in self.enemies:
			space(1)
			print(Fore.RED + enemy.name + Fore.MAGENTA + " attacks!")
			ability = enemy.chooseAttack()
			hit = self.attackHit(ability)
			if hit == False:
				print(Fore.RED + enemy.name + "'s attack misses!")
				sleep(1)
			else:
				enemy.attacking(player, ability)
				sleep(1)
				if player.isAlive() == False:
					self.gameOver(player)
					break
		sleep(1)
	def combat(self, player):
		""" The main combat loop. Continues as long as (1) player is alive and (2) there are enemies left """
		self.start(player)
		flag = 0
		loopFlag = 1
		while loopFlag == 1:
			x = self.playerTurn(player, flag)
			if x == None:
				pass
			else:
				flag == x
			if not self.enemies:
				loopFlag = 0
				if flag == 0:
					self.victory(player)
				else:
					self.fleeScreen()
				break
			self.enemyTurn(player)
			if player.isAlive() == False or player.isZombie() == True:
				loopFlag = 0
				self.gameOver(player)
				break
	def encounter(self, upLimit, enemyList, player):
		""" This will be the function when searched locations get ambushed """
		number = random.randint(1, upLimit)
		""" This function adds enemies to the battle based on the random number of enemies generated. It'll loop through until it gets an enemy object that isn't already in the battle list """
		for x in range(number):
			flag = 1
			while flag == 1:
				current = random.choice(enemyList)
				if current in self.enemies:
					pass
				else:
					self.add(current)
					flag = 0
		# Now that enemies are added, we need to do combat
		self.combat(player)
	def eliminate(self, number, enemyList, player):
		""" This function will be for warzones """
		if number < 5:
			limit = number
		else:
			limit = 5

		count = random.randint(1, limit)
		for x in range(count):
			flag = 1
			while flag == 1:
				current = random.choice(enemyList)
				if current in self.enemies:
					pass
				else:
					self.add(current)
					flag = 0
		# Now that enemies are added, we need to do combat
		self.combat(player)
		return self.killCount



