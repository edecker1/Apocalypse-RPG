import pickle
import datetime
from character import *
from misc import *

class SaveSystem:
	""" This will allow me to save and load characters """
	def __init__(self):
		pass
	def loadScreen(self):
		clear()
		print(Fore.GREEN + "What save would you like to load?")
		try:
			with open('savefile1', 'rb') as f:
				loads = pickle.load(f)
				player1 = loads[0]
				try:
					date1 = loads[2]
				except:
					date1 = "Not Dated"
				f.close()
		except:
			player1 = None
		try:
			with open('savefile2', 'rb') as f:
				loads1 = pickle.load(f)
				player2 = loads1[0]
				try:
					date2 = loads1[2]
				except:
					date2 = "Not dated"
				f.close()
		except:
			player2 = None

		if player1 != None:
			print((Fore.YELLOW + "-- Save #1 -- \nName: " + Fore.WHITE + player1.name + Fore.YELLOW + "\nLevel: " + Fore.WHITE + "{level} \nHealth: {hp}/{maxHp} \nLast Saved: {time}").format(name=player1.name, level=player1.level, hp=player1.hp, maxHp=player1.maxHp, time=date1))
		else:
			print(Fore.YELLOW + "-- Save #1 -- \nName: " + Fore.WHITE + "None" + Fore.YELLOW + "\nLevel: " + Fore.WHITE + "0")
		
		space(1)
		
		if player2 != None:
			text = (Fore.YELLOW + "-- Save #2 -- \nName: " + Fore.WHITE + player2.name + Fore.YELLOW + "\nLevel: " + Fore.WHITE + "{level} \nHealth: {hp}/{maxHp}\nLast Saved: {time}").format(name=player2.name, level=player2.level, hp=player2.hp, maxHp=player2.maxHp, time=date2)
			print(text)
		else:
			print(Fore.YELLOW + "-- Save #2 -- \nName: " + Fore.WHITE + "None" + Fore.YELLOW + "\nLevel: " + Fore.WHITE + "0")

		space(1)
		print(Fore.GREEN + "Which would you like to load? Type [ " + Fore.YELLOW + "0" + Fore.GREEN + " ] to go back." + Fore.BLUE)
		space(1)
		choice = int(input(">>  "))
		try:
			if choice == 1:
				return 1
			elif choice == 2:
				return 2
			elif 0:
				print(Fore.GREEN + "Going back...")
				sleep(1)
				clear()
				return None
			else:
				print(Fore.RED + "Unrecognized input!")
				return None
		except Exception as ex:
			print(ex)
			raise
	def save(self, data, world):
		# self, name, hp, maxHp, contamination, inventory, weapon, armor, credits, coordinates, level, cap, experience, job, strength, dexterity, endurance
		clear()
		now = datetime.datetime.now()
		month = now.strftime("%B")
		day = now.strftime("%d")
		year = now.strftime("%Y")
		hour = now.strftime("%I")
		minute = now.strftime("%M")
		period = now.strftime("%p")
		#date = "{}-{}-{} -- {}:{}".format(now.month, now.day, now.year, now.hour, now.minute)
		date = ("{} {}, {}  {}:{} {}".format(month, day, year, hour, minute, period))
		print("Date is: " + date)
		flag = 1
		while flag == 1:
			print(Fore.GREEN + "Save to "+Fore.YELLOW+"Save File 1 "+Fore.GREEN+"or "+Fore.YELLOW+"Save File 2 "+Fore.GREEN+"?"+Fore.BLUE)
			space(1)
			choice = int(input(">>  "))
			try:
				if choice == 1:
					flag = 0
					with open('saveFile1', 'wb') as f:
						pickle.dump([data, world, date], f)
						f.close()
				elif choice == 2:
					flag = 0
					with open('saveFile2', 'wb') as f:
						pickle.dump([data, world, date], f)
						f.close()
				else:
					print(Fore.RED + "Unrecongized input")
			except Exception as ex:
				print(ex)
				raise
		print("Progress has been saved!")
		sleep(1)
	def load(self, x):
		try:
			if x == 1:
				f = open('saveFile1', 'rb')
				player = pickle.load(f)
				f.close()
				print("Load successful")
				sleep(1)
				return player
			elif x == 2:
				f = open('saveFile2', 'rb')
				player = pickle.load(f)
				f.close()
				print("Load successful")
				sleep(1)
				return player
			else:
				print(Fore.RED + "ERROR!")
			sleep(1)
		except Exception as ex:
			print(ex)
			raise
