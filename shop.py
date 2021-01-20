# -- All functions related to shop -- #
# --- Import Libraries --- #
from colorama import Fore, Back, Style
import random, math
from time import sleep

# -- Import My Modules -- #
from misc import *

class Shop:
	""" This object will have the inventory of stock. It'll be updated with new items and new stock """
	def __init__(self, items, access):
		self.items = items
		self.access = access # So I can easily access the index when buying

	def add(self, item, stock):
		self.items.update({item:stock})
		self.access.append(item)
	def update(self, item, stock):
		current = self.items.get(item)
		current += stock
		self.items[item] = current
	def sell(self, item, player):
		stock = self.items[item]
		if stock == 0:
			print(Fore.RED + "This item is sold out! Come back another time!")
			sleep(1)
		else:
			stock -= 1
			player.buyItem(item)
			self.items[item] = stock
	def buy(self, item, player):
		if item in self.items:
			player.sellItem(item)
			self.update(item, 1)
		else:
			player.sellItem(item)
			self.add(item, 1)
	def remove(self, item):
		del self.items[item]
		self.access.remove(item)

	def showStock(self):
		x = 1
		for item in self.items:
			if self.items[item] == 0:
				print(Fore.BLUE + "||  " + str(x) + ". " + item.name + " -- " + Fore.RED + "SOLD OUT" + Fore.BLUE + "  ||" )
			else:
				number = self.items.get(item)
				price = item.showPrice(x)
				print(price + "  -- " + str(number) + " left  ||" )

			x += 1
	def shopShipment(self):
		for stock in self.items:
			number = random.randint(0, 2)
			self.update(stock, number)
	""" These are the functions for buying and selling """
	def buyingInterface(self, player):
		flag = 1
		while flag == 1:
			clear()
			print(Fore.YELLOW + "||  -- Buying Items --  ||")
			print(Fore.BLUE + "You have " + Fore.YELLOW + str(player.credits) + " credits")
			self.showStock()
			space(1)
			print(Fore.GREEN + "What would you like to buy? Enter 0 to exit" + Fore.BLUE)
			choice = int(input())
			if choice == 0:
				flag = 0
			else:
				try:
					intent = self.access[(choice - 1)]
					self.sell(intent, player)
				except:
					print(Fore.RED + "Error!, not proper input")
					sleep(0.5)
	def sellingInterface(self, player):
		flag = 1
		while flag == 1:
			clear()
			print(Fore.YELLOW + "||  -- Selling Items --  ||")
			print(Fore.BLUE + "You have " + Fore.YELLOW + str(player.credits) + " credits")
			player.sellingInv()
			space(1)
			print(Fore.GREEN + "What would you like to sell? Enter 0 to exit" + Fore.BLUE)
			choice = int(input())
			if choice == 0:
				flag = 0
			else:
				try:
					intent = player.inventory[(choice - 1)]
					self.buy(intent, player)
				except:
					print(Fore.RED + "Error! Not proper input")
					sleep(0.5)
	def mainInterface(self, player):
		self.shopShipment()
		flag = 1
		while flag == 1:
			clear()
			print(Fore.YELLOW + "||  -- Trader --  ||")
			print(Fore.BLUE + "You have " + Fore.YELLOW + str(player.credits) + " credits")
			space(1)
			print(Fore.GREEN + "A rough man with many scars looks down at you. \nHe squints and takes a moment before recognizing you as a customer. \nHe smiles and proclaims " + Fore.CYAN + "'What can I do for ya today?'")
			space(1)
			print(Fore.YELLOW + "1. " + Fore.GREEN + "Buy Items")
			print(Fore.YELLOW + "2. " + Fore.GREEN + "Sell Items")
			print(Fore.YELLOW + "3. " + Fore.GREEN + "Leave")
			print()
			choice = int(input())
			try:
				if choice == 3:
					flag = 0
				elif choice == 1:
					self.buyingInterface(player)
				elif choice == 2:
					self.sellingInterface(player)
				else:
					print("Invalid input!")
			except:
				print("Error!")


