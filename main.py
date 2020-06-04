from colorama import Fore, Back, Style
from time import sleep
import os, random, math, sys

# Function to clear the screen
def clear():
  os.system( 'clear' )
# Space Function
def space():
  print("")
# Reset Function
def reset():
  clear()
  HUD()
  space()

# searched value #
y = 0

def searchedValue(loc):
  x = map.get(loc)
  global y
  for locs in totalLocations:
    if locs.name == x:
      z = locs.searched
      if z== 0: 
        y = 100
      else:
        y = round(((searched[myPlayer.coordinate] / z) * 100), 1)

#character name + stats
class Player:
  def __init__(self):
    self.name = 'Main Character'
    self.hp = 100
    self.contamination = 0
    self.attack = 5
    self.inventory = ['Sharp Stick', 'Bandage', 'Casual Clothes']
    self.usableItem = []
    self.equippedWeapon = []
    self.weapons = []
    self.equippedArmor = []
    self.armor = []
    self.coordinate = 13
    self.location = 'a'
    self.locDescription = 'a'
    self.killed = 0
    self.credits = 0
    self.searchs = 0
    self.failed = 0
    self.succeed = 0
    self.travels = 0
    self.damageTaken = 0
    self.damageGiven = 0
    self.itemsSold = 0
    self.itemsUsed = 0
    self.armorStat = 1



myPlayer = Player()

# Function to start Game
def startGame():
  print(Fore.GREEN + "Welcome to the " + Fore.RED + "Zombie Apocalypse" + Fore.GREEN + "!")
  space() 
  sleep(1)
  print(Fore.GREEN + "The world has been ravaged by an infectious plague that has turned most of the world's population into" + Fore.RED + " mindless flesh eaters")
  space() 
  sleep(3)
  print(Fore.GREEN + "With most of the world destroyed, you must survive by scavenging this desolate city")
  space()
  space()
  sleep(3)
  print(Fore.GREEN + "What is your name? ")
  myPlayer.name = input(Fore.BLUE + ">>  ")
  myPlayer.name = myPlayer.name.upper()
  space()
  print(Fore.GREEN + "Welcome " + Fore.BLUE + "{}".format(myPlayer.name))
  print(Fore.GREEN + "Do you have what it takes to " + Fore.RED + "survive?")
  sleep(2)
  clear()

# HUD
def HUD():
  global y
  print(Fore.GREEN + "Name: " + Fore.BLUE + "{}".format(myPlayer.name))
  if myPlayer.hp >= 65:
    print(Fore.GREEN + "Health: " + Fore.BLUE + str(myPlayer.hp) + Fore.GREEN + "/" + Fore.BLUE + '100')
  elif myPlayer.hp >= 25 and myPlayer.hp < 64:
    print(Fore.GREEN + "Health: " + Fore.YELLOW + str(myPlayer.hp) + Fore.GREEN + "/" + Fore.BLUE + '100')
  else:
    print(Fore.GREEN + "Health: " + Fore.RED + str(myPlayer.hp) + Fore.GREEN + "/" + Fore.BLUE + '100')
  print(Fore.GREEN + "Credits: " + Fore.BLUE + str(myPlayer.credits))
  if myPlayer.contamination <= 49:
    print(Fore.GREEN + "Contamination: " + Fore.BLUE + str(myPlayer.contamination) + Fore.GREEN + "%")
  elif myPlayer.contamination >= 50 and myPlayer.contamination < 75:
    print(Fore.GREEN + "Contamination: " + Fore.YELLOW + str(myPlayer.contamination) + Fore.GREEN + "%")
  else:
    print(Fore.GREEN + "Contamination: " + Fore.RED + str(myPlayer.contamination) + Fore.GREEN + "%")
  getLoc(myPlayer.coordinate)
  print(Fore.GREEN + "Location: " + Fore.YELLOW + myPlayer.location)
  print(Fore.GREEN + "Description: " + Fore.LIGHTYELLOW_EX + myPlayer.locDescription)
  searchedValue(myPlayer.coordinate)
  if y < 25:
    print(Fore.GREEN + "Searched: " + Fore.RED + str(y) + Fore.GREEN + "%")
  elif y > 25 and y < 60:
    print(Fore.GREEN + "Searched: " + Fore.YELLOW + str(y) + Fore.GREEN + "%")
  else:
    print(Fore.GREEN + "Searched: " + Fore.LIGHTYELLOW_EX + str(y) + Fore.GREEN + "%")

# -- Items -- #
# Weapons #
class weapon:
  def __init__(self, name, attack, value):
    self.name = name 
    self.attack = attack
    self.value = value
# Items #
class item:
  def __init__(self, name, attribute, value, point):
    self.name = name
    self.attribute = attribute
    self.value = value 
    self.point = point

# Armor #
class armor:
  def __init__(self, name, armor, value):
    self.name = name
    self.armor = armor
    self.value = value

# Armor List #
casual = armor('Casual Clothes', 1, 5)
work = armor("Worker's Clothes", 3, 30)
leather = armor('Reinforced Leather Clothes', 5, 50)
police = armor('Police Armor', 7, 300)
army = armor("Military Armor", 12, 1000)
shinobi = armor("Jonin Uniform", 10, 1500)
akatsuki = armor ("Akatsuki Robes", 15, 3000)

armorList = [casual, work, leather, police, army, akatsuki]
# Weapon List #
stick = weapon('Sharp Stick', 6, 5)
bow = weapon('Longbow', 15, 150)
xbow = weapon('Crossbow', 17, 200)
pistol = weapon('Pistol', 20, 250)
sledge = weapon('Sledgehammer', 25, 400)
rifle = weapon('Rifle', 35, 600)
xsaw = weapon('Chainsaw', 50, 1500)
plasma = weapon('Plasma Sword', 60, 2500)
knife = weapon('Knife', 7, 50)
axe = weapon('Rusty Axe', 9, 75)
sword = weapon('Sword', 11, 100)

# Searched Weapons #
katana = weapon('Katana', 13, 130)
dagger = weapon('Dagger', 9, 75)
hammer = weapon('Hammer', 10, 120)
crowb = weapon('Crowbar', 11, 110)
bbat = weapon('Broken Bat', 6, 30)
bat = weapon('Bat', 9, 100)
nbat = weapon('Nailed Bat', 13, 100)
kunai = weapon('Kunai', 14, 100)
sasuke = weapon('The Kusanagi', 55, 3000)
minato = weapon('Flying Raijin Kunai', 40, 3000)
ar = weapon('Assault Rifle', 45, 900)
smg = weapon('Submachine Gun', 40, 800)
de = weapon('Desert Eagle', 30, 1000)


weaponsList = [stick, bow, xbow, pistol, sledge, rifle, xsaw, plasma, knife, sword, axe, katana, dagger, hammer, crowb, bbat, bat, nbat, kunai, sasuke, minato, ar, smg, de]

# Item List #
bandage = item('Bandage', 'hp', 100, 10)
pain = item('Pain Medicine', 'hp', 200, 15)
virusOne = item('Virus Killer', 'c', 100, 10)
virusTwo = item('Virus Killer X', 'c', 150, 20)
firstAid = item('First Aid Kit', 'h', 250, 25)

# Search Items #
cheese = item('Cheese', 'hp', 20, 4)
bread = item('Slice of Toast', 'hp', 10, 2)
doctors = item("Doctor's Kit", 'hp', 500, 35)

usableList = [bandage, pain, virusOne, virusTwo, firstAid, cheese, bread, doctors]

totalItemList = [stick, bow, xbow, pistol, sledge, rifle, xsaw, plasma, knife, sword, axe, bandage, pain, virusOne, virusTwo, firstAid, katana, dagger, hammer, crowb, bbat, bat, nbat, kunai, sasuke, minato, ar, smg, de, cheese, bread, doctors, casual, work, leather, police, army, akatsuki]

# Locations
class Location:
  def __init__(self, name, description, chance, searched, loot):
    self.name = name
    self.description = description
    self.chance = chance
    self.searched = searched
    self.loot = loot

highway = Location('Empty Highway', 'A section of highway littered with abandoned cars and dead bodies', 60, 9, ['Cheese', 'Submachine Gun', 'Bat', 'Broken Bat', 'Dagger', 'Crowbar', 'Map', 'Nothing', 'Nothing'])
highwayZ = Location('Infested Highway', "A section of highway that's been overrun with zombies. Better be careful...", 75, 7, ['Akatsuki Robes', 'Military Armor', 'The Kusanagi', 'Kunai', 'Cheese', 'First Aid Kit', 'Virus Killer X', "Doctor's Kit"])
highwayS = Location('Claimed Highway', "A section of highway that's been claimed by a group of survivors. They don't look very friendly...", 75, 7, ['Nothing', 'Assault Rifle', 'Desert Eagle', 'Military Armor', 'Police Armor', 'Pain Medicine', 'First Aid Kit'])
hospital = Location('Ruined Hospital', 'What was once a place of hope and healing is now a graveyard that serves as a home for flesh-eating monsters', 85, 10, ['Pain Medicine', "Doctor's Kit", 'First Aid Kit', 'Bandage', 'Dagger', 'Katana', 'Map'])
gun = Location('Overrun Gun Shop', 'The dead have taken residence here despite their lack of interest in firepower', 80, 5, ['Desert Eagle', 'Assault Rifle', 'Rifle', 'Pistol', 'Submachine Gun', 'Map'])
rubble = Location('Destroyed Building', 'Just a mess of rubble, debris, and shattered hope', 40, 7, ['Cheese', 'Slice of Toast', 'Sharp Stick', 'Broken Bat', 'Nothing', 'Nothing'])
hive = Location('Zombie Hive', 'What seems like a breeding ground for these monsters', 85, 12, ["Doctor's Kit", 'The Kusanagi', 'Flying Raijin Kunai', 'Kunai', 'First Aid Kit', 'Assault Rifle', 'Desert Eagle', 'Submachine Gun', 'Map'])
supply = Location('Supply Spot', 'A left over spot that is not too picked over or destroyed', 70, 15, ['Virus Killer', 'Kunai', 'Pistol', 'Bat', 'Katana', 'Pain Medicine', 'Nailed Bat', 'Map', 'Nothing'])
traders = Location('Survivors Hub', 'A spot where the last few survivors have come together.', 0, 0, [])
quest1 = Location("Survior's Enclave", "You've heard rumors of survivors gathering here, but you don't see anyone... strange...", 0, 5, ['Evidence', 'Nothing', 'Nothing'])

totalLocations = [highway, gun, rubble, hive, quest1, supply, traders]
map = {1: 'Zombie Hive', 2: 'Empty Highway', 3: 'Supply Spot', 4: 'Destroyed Building', 11: "Survior's Enclave", 12:'Empty Highway', 13: 'Survivors Hub', 14: 'Destroyed Building', 21:'Overrun Gun Shop', 22: 'Empty Highway', 23: 'Zombie Hive', 24: 'Ruined Hospital', 31: 'Empty Highway', 32: 'Empty Highway', 33: 'Empty Highway', 34: 'Empty Highway', 41: 'Zombie Hive', 42: 'Empty Highway', 43: 'Overrun Gun Shop', 44: 'Supply Spot', 51: 'Ruined Hospital', 52: 'Empty Highway', 53: 'Supply Spot', 54: 'Zombie Hive'}

searched = {1: 0, 2: 0, 3: 0, 4: 0, 11: 0, 12: 0, 13: 0, 14: 0, 21: 0, 22: 0, 23: 0, 24: 0, 31: 0, 32: 0, 33: 0, 34: 0, 41: 0, 42: 0, 43: 0, 44: 0, 51: 0, 52: 0, 53: 0, 54: 0}

# Get location
def getLoc(loc):
  x = map.get(loc)
  for location in totalLocations:
    if x == location.name:
      myPlayer.location = location.name 
      myPlayer.locDescriptuon = location.description
  

maps = 0
# Options function
def optionsHUD():
  print(Fore.GREEN + "What would you like to do?")
  print(Fore.YELLOW + '[A]' + Fore.GREEN + " Travel")
  if myPlayer.coordinate == 13: 
    print(Fore.YELLOW + '[B]' + Fore.GREEN + " Trade")
  else: 
    print(Fore.YELLOW + '[B]' + Fore.GREEN + " Search")
  print(Fore.YELLOW + '[C]' + Fore.GREEN + " Check Inventory")
  print(Fore.YELLOW + '[D]' + Fore.GREEN + " Check Stats")
  if maps ==1:
    print(Fore.YELLOW + '[E]' + Fore.GREEN + " Look at Map") 
  space()
  choice = input(Fore.BLUE + ">> ")

  if choice.upper() == 'A':
    clear()
    HUD()
    space()
    travel()
  elif choice.upper() == 'B' and myPlayer.coordinate == 13:
    trading()
  elif choice.upper() == 'B' and myPlayer.coordinate != 13:
    search()
  elif choice.upper() == 'C':
    clear()
    HUD() 
    space()
    checkInventory()
  elif choice.upper() == 'D':
    checkStats()
  elif choice.upper() == 'E' and maps == 1:
    showMap()
  else:
    print(Fore.RED + "Did not recognize input. Try again")
    sleep(1)
    reset() 
    optionsHUD()

# Check Stats #
def checkStats():
  clear()
  print(Fore.GREEN + "Name: " + Fore.BLUE + myPlayer.name)
  print(Fore.GREEN + "Health: " + Fore.BLUE + str(myPlayer.hp))
  print(Fore.GREEN + "Contamination: " + Fore.BLUE + str(myPlayer.contamination) + Fore.GREEN + "%")
  print(Fore.GREEN + "Zombies Killed: " + Fore.BLUE + str(myPlayer.killed))
  print(Fore.GREEN + "Times Traveled: " + Fore.BLUE + str(myPlayer.travels))
  print(Fore.GREEN + "Times Searched: " + Fore.BLUE + str(myPlayer.searchs))
  if myPlayer.searchs > 0: print(Fore.GREEN + "Successful Search Rate: " + Fore.BLUE + str(round((myPlayer.succeed / myPlayer.searchs) * 100)) + Fore.GREEN + "%")
  if not myPlayer.equippedWeapon:
    print(Fore.GREEN + "Equipped Weapon: " + Fore.RED + "None")
  else:
    print(Fore.GREEN + "Equipped Weapon: " + Fore.BLUE + str(myPlayer.equippedWeapon))
  print(Fore.GREEN + "Attack Power: " + Fore.BLUE + str(myPlayer.attack))
  if not myPlayer.equippedWeapon:
    print(Fore.GREEN + "Equipped Armor: " + Fore.RED + "None")
  else:
    print(Fore.GREEN + "Equipped Armor: " + Fore.BLUE + str(myPlayer.equippedArmor))
  print(Fore.GREEN + "Armor: " + Fore.BLUE + str(myPlayer.armorStat))
  print(Fore.GREEN + "Total Damage Taken: " + Fore.BLUE + str(myPlayer.damageTaken))
  print(Fore.GREEN + "Total Damage Given: " + Fore.BLUE + str(myPlayer.damageGiven))
  print(Fore.GREEN + "Credits: " + Fore.BLUE + str(myPlayer.credits))
  print(Fore.GREEN + "Items Traded In: " + Fore.BLUE + str(myPlayer.itemsSold))
  print(Fore.GREEN + "Items Used: " + Fore.BLUE + str(myPlayer.itemsUsed))
  print(Fore.GREEN + "Inventory: ")
  if not myPlayer.inventory:
      print(Fore.RED + "You have nothing!")
  else:
    n= 1
    for item in myPlayer.inventory:
      print(Fore.YELLOW + str(n) + ". " + Fore.BLUE + item)
      n = n + 1
  space()
  space() 
  print(Fore.GREEN + "Enter any key to go back")
  choice = input(Fore.BLUE + ">> ")
  if myPlayer.hp > 0:
    reset()
    optionsHUD()
  else:
    sys.exit() 

#------------------------------------------------------#
# All functions related to traveling
#------------------------------------------------------#

# Travel
def travel():
  print(Fore.GREEN + "Where would you like to go?")
  print(Fore.YELLOW + "[N]" + Fore.GREEN + " for " + Fore.YELLOW + "North")
  print(Fore.YELLOW + "[S]" + Fore.GREEN + " for " + Fore.YELLOW + "South")
  print(Fore.YELLOW + "[E]" + Fore.GREEN + " for " + Fore.YELLOW + "East")
  print(Fore.YELLOW + "[W]" + Fore.GREEN + " for " + Fore.YELLOW + "West")
  print(Fore.RED + "[0]" + Fore.GREEN + " to " + Fore.YELLOW + "Stop Traveling")
  space()
  choice = input(Fore.BLUE + ">> ")

  # Going North #
  if choice.upper() == 'N':
    if (myPlayer.coordinate < 10):
      print(Fore.RED + "You cannot go any farther north!")
      sleep(2)
      reset()
      ambush()
      travel()
    else:
      myPlayer.coordinate = myPlayer.coordinate - 10
      myPlayer.travels = myPlayer.travels + 1
      reset()
      travel() 
  
  # Going South #
  elif choice.upper() == 'S':
    if (myPlayer.coordinate > 50):
      print(Fore.RED + "You cannot go any farther south!")
      sleep(2)
      reset()
      ambush()
      travel()
    else:
      myPlayer.coordinate = myPlayer.coordinate + 10
      myPlayer.travels = myPlayer.travels + 1
      reset()
      travel()
  
  # Going West #
  elif choice.upper() == 'W':
    if (myPlayer.coordinate == 11 or myPlayer.coordinate == 21 or myPlayer.coordinate == 31 or myPlayer.coordinate == 41 or myPlayer.coordinate == 51 or myPlayer.coordinate == 1):
      print(Fore.RED + "You cannot go any farther west!")
      sleep(2)
      reset()
      ambush()
      travel()
    else:
      myPlayer.coordinate = myPlayer.coordinate - 1
      myPlayer.travels = myPlayer.travels + 1
      reset()
      travel()

    # Going East #
  elif choice.upper() == 'E':
    if (myPlayer.coordinate == 14 or myPlayer.coordinate == 24 or myPlayer.coordinate == 34 or myPlayer.coordinate == 44 or myPlayer.coordinate == 54 or myPlayer.coordinate == 4):
      print(Fore.RED + "You cannot go any farther east!")
      sleep(2)
      reset()
      ambush()
      travel()
    else:
      myPlayer.coordinate = myPlayer.coordinate + 1
      myPlayer.travels = myPlayer.travels + 1
      reset()
      travel()
  
  # Error #
  else:
    reset() 
    optionsHUD()
# ENcounter chance #
def ambush():
  chance = random.randint(1,100)
  if chance <= 20:
    print(Fore.RED + "You've been ambushed!")
    sleep(2)
    space()
    encounter() 
  else: pass
#------------------------------------------------------#
# All functions related to searching and inventory 
#------------------------------------------------------#

# Check Inventory
def checkInventory():
  backList()
  properList()
  print(Fore.GREEN + "Your inventory is: ")
  # if Empty #
  if not myPlayer.inventory:
    print(Fore.RED + "You have nothing in your inventory!")
  else:
    for item in myPlayer.inventory:
      print (Fore.BLUE + item)
  # Equipped Item #
  print(Fore.GREEN + "Equipped weapon:")
  # If not equipped #
  if not myPlayer.equippedWeapon:
    print(Fore.RED + "You have nothing equipped!")
  else:
    for item in myPlayer.equippedWeapon:
      print (Fore.BLUE + item)
  # Equipped Armor #
  print(Fore.GREEN + "Equipped armor:")
  # If not equipped #
  if not myPlayer.equippedArmor:
    print(Fore.RED + "You have nothing equipped!")
  else:
    for item in myPlayer.equippedArmor:
      print (Fore.BLUE + item)
  # Menu to go back #
  space() 
  print(Fore.GREEN + "What would you like to do?")
  print (Fore.YELLOW + "[A]" + Fore.GREEN + " Use item")
  print (Fore.YELLOW + "[B]" + Fore.GREEN + " Equip Weapon")
  print (Fore.YELLOW + "[C]" + Fore.GREEN + " Equip Armor")
  print (Fore.YELLOW + "[D]" + Fore.GREEN + " Go back")
  space()
  choice = input(Fore.BLUE + ">> ")

  if choice.upper() == 'A':
    reset()
    print(Fore.GREEN + "Usable items:")
    # If none #
    if not myPlayer.usableItem:
      print(Fore.RED + "You do not have any items you can use!")
    else:
      n= 1
      for item in myPlayer.usableItem:
        print(Fore.YELLOW + str(n) + ". " + Fore.BLUE + item)
        n = n + 1
      
    # Choice Menu #
    space() 
    print(Fore.GREEN + "Type the number of the item you would like to use or 0 to go back.")
    choice = input(Fore.BLUE + ">> ")

    if choice == '0':
      reset() 
      backList()
      checkInventory()
    else:
      try:
        usable = myPlayer.usableItem[(int(choice) - 1)]
        myPlayer.itemsUsed = myPlayer.itemsUsed + 1
        useItem(usable)
      except:
        print(Fore.RED + "Unrecognized input!")
        sleep(1)
        backList()
        reset() 
        checkInventory()

  elif choice.upper() == 'B':
    reset()
    print(Fore.GREEN + "Weapons:")
    # If none #
    if not myPlayer.weapons:
      print(Fore.RED + "You do not have any items you can equip!")
    else:
      n= 1
      for item in myPlayer.weapons:
        print(Fore.YELLOW + str(n) + ". " + Fore.BLUE + item)
        n = n + 1
      
    # Choice Menu #
    space() 
    print(Fore.GREEN + "Type the number of the item you would like to equip or 0 to go back.")
    choice = input(Fore.BLUE + ">> ")

    if choice == '0':
      reset() 
      backList()
      checkInventory()
    else:
      try:
        weapon = myPlayer.weapons[(int(choice) - 1)]
        weapon = format(weapon)
        equipItem(weapon)
        print(Fore.BLUE + "You" + Fore.GREEN + " have equipped a " + Fore.YELLOW + "[" + weapon + "]")
        sleep(1)
        backList()
        reset() 
        checkInventory()
      except:
        print(Fore.RED + "Unrecognized input!")
        sleep(1)
        backList()
        reset() 
        checkInventory()
  elif choice.upper() == 'C':
    reset()
    print(Fore.GREEN + "Armor:")
    # If none #
    if not myPlayer.armor:
      print(Fore.RED + "You do not have any items you can equip!")
    else:
      n= 1
      for item in myPlayer.armor:
        print(Fore.YELLOW + str(n) + ". " + Fore.BLUE + item)
        n = n + 1
      
    # Choice Menu #
    space() 
    print(Fore.GREEN + "Type the number of the item you would like to equip or 0 to go back.")
    choice = input(Fore.BLUE + ">> ")

    if choice == '0':
      reset() 
      backList()
      checkInventory()
    else:
      try:
        armor = myPlayer.armor[(int(choice) - 1)]
        armor = format(armor)
        equipArmor(armor)
        print(Fore.BLUE + "You" + Fore.GREEN + " have equipped a " + Fore.YELLOW + "[" + armor + "]")
        sleep(1)
        backList()
        reset() 
        checkInventory()
      except:
        print(Fore.RED + "Unrecognized input!")
        sleep(1)
        backList()
        reset() 
        checkInventory()
  elif choice.upper() == 'D':
    reset()
    optionsHUD()
  else:
    print(Fore.RED + "Unrecognized input!")
    sleep(1)
    backList() 
    reset()
    checkInventory()

# Search function #
def search():
  myPlayer.searchs = myPlayer.searchs + 1
  # Encounter chance #
  x = map.get(myPlayer.coordinate)
  if x == 'rubble':
    z = rubble.chance
  elif x == 'hive':
    z = hive.chance
  elif x == 'supply':
    z = supply.chance
  elif x == 'highway':
    z = highway.chance
  elif x == 'hospital':
    z = hospital.chance
  elif x == 'gun':
    z = gun.chance
  
  #Actual search
  if y == 100:
    reset() 
    print (Fore.RED + "You have already completely searched this area!")
    myPlayer.searchs = myPlayer.searchs - 1
    sleep(2)
    reset()
    optionsHUD()
  else:
    reset() 
    print(Fore.GREEN + "You are searching " + Fore.YELLOW + myPlayer.location + Fore.GREEN + "!")
    sleep(1)
    print("...")
    space()
    sleep(1)
    print("...")
    sleep(1)
    space()
    print("...")
    sleep(.5)
    space()
    chance = random.randint(1,100)
    beat = 100 - z
    if (chance <= beat):
      searched[myPlayer.coordinate] += 1
      print(Fore.GREEN + "You have " + Fore.YELLOW + "successfully " + Fore.GREEN + "searched the area!")
      loot()
      myPlayer.succeed = myPlayer.succeed + 1
    else:
      print(Fore.GREEN + "You have " + Fore.RED + "unsuccessfully " + Fore.GREEN + "searched the area!")
      myPlayer.failed = myPlayer.failed + 1
      sleep(2)
      encounter()

    sleep(2)
    reset()
    optionsHUD()

# Loot #
def loot():
  global maps
  x = map.get(myPlayer.coordinate)
  for loc in totalLocations:
    if loc.name == x:
      z = loc.loot
  
  loot = random.choice(z)
  if loot == 'Map':
    print(Fore.GREEN + "You have found a " + Fore.BLUE + "[Map]" + Fore.GREEN + "!")

    maps = 1
  elif loot == 'Nothing':
    print(Fore.BLUE + "You " + Fore.GREEN + "found nothing!")
  elif loot == 'Evidence':
    print(Fore.BLUE + "You " + Fore.GREEN + "found evidence of there being survivors here but no one is here... strange...")
  else:
    print(Fore.GREEN + "You got a " + Fore.YELLOW + loot)
    myPlayer.inventory.append(loot)

# check loop #
def properList():
  for item in myPlayer.inventory:
    for weapon in weaponsList:
      if item == weapon.name:
        myPlayer.weapons.append(item)
    for potion in usableList:
      if item == potion.name:
        myPlayer.usableItem.append(item)
    for armor in armorList:
      if item == armor.name:
        myPlayer.armor.append(item)

# CLears the Lists #
def backList():
  myPlayer.weapons.clear()
  myPlayer.usableItem.clear()
  myPlayer.armor.clear()

# Equip Item #
def equipItem(weapon):
  if not myPlayer.equippedWeapon:
    myPlayer.equippedWeapon.append(weapon)
    myPlayer.inventory.remove(weapon)
  else: 
    old = myPlayer.equippedWeapon[0]
    myPlayer.inventory.append(old)
    myPlayer.equippedWeapon.clear()
    myPlayer.equippedWeapon.append(weapon)
    myPlayer.inventory.remove(weapon)
  
  for x in totalItemList:
    if x.name == weapon:
      myPlayer.attack = x.attack

# Equip Armor #
def equipArmor(armor):
  if not myPlayer.equippedArmor:
    myPlayer.equippedArmor.append(armor)
    myPlayer.inventory.remove(armor)
  else: 
    old = myPlayer.equippedArmor[0]
    myPlayer.inventory.append(old)
    myPlayer.equippedArmor.clear()
    myPlayer.equippedArmor.append(armor)
    myPlayer.inventory.remove(armor)
  
  for x in armorList:
    if x.name == armor:
      myPlayer.armorStat = x.armor


# Use Item #
def useItem(item):
  myPlayer.inventory.remove(item)
  for potion in usableList:
    if item == potion.name:
      if potion.attribute == 'hp':
        if (myPlayer.hp + potion.point) > 100:
          myPlayer.hp = 100
          print(Fore.GREEN + "You used " + Fore.YELLOW + "[" + potion.name + "]" + Fore.GREEN + " to heal!")
          sleep(1)
          reset()
          checkInventory()
        else:
          myPlayer.hp = myPlayer.hp + potion.point
          print(Fore.GREEN + "You used " + Fore.YELLOW + "[" + potion.name + "]" + Fore.GREEN + " to heal!")
          sleep(1)
          reset()
          checkInventory()
      else:
        if (myPlayer.contamination - potion.point) < 0:
          myPlayer.contamination = 0
          print(Fore.GREEN + "You used " + Fore.YELLOW + "[" + potion.name + "]" + Fore.GREEN + " to decontaminate yourself!")
          sleep(1)
          reset()
          checkInventory()
        else:
          myPlayer.contamination = myPlayer.contamination - potion.point
          print(Fore.GREEN + "You used " + Fore.YELLOW + "[" + potion.name + "]" + Fore.GREEN + " to decontaminate yourself!")
          sleep(1)
          reset()
          checkInventory()

#------------------------------------------------------#
# All functions related to trade post
#------------------------------------------------------#
shopList = {'Knife':knife.value, 'Rusty Axe': axe.value, 'Sword': sword.value, 'Bandage': bandage.value, 'Virus Killer': virusOne.value, 'Virus Killer X': virusTwo.value, 'Longbow': bow.value, 'Crossbow': xbow.value, 'Pain Medicine': pain.value, 'First Aid Kit': firstAid.value, 'Pistol': pistol.value, 'Sledgehammer': sledge.value, 'Rifle':rifle.value, 'Chainsaw':xsaw.value, 'Plasma Sword':plasma.value}

buyList = ['Knife', 'Rusty Axe', 'Sword', 'Bandage', 'Virus Killer', 'Virus Killer X', 'Longbow', 'Crossbow', 'Pain Medicine', 'First Aid Kit', 'Pistol', 'Sledgehammer', 'Rifle', 'Chainsaw', 'Plasma Sword']

intro = 0
# Trading #
def trading():
  clear()
  global intro
  if intro != 1:
    print(Fore.CYAN + "Welcome, " + Fore.BLUE + str(myPlayer.name) + Fore.CYAN + "!")
    sleep(1)
    print("Here we have ourselves a little shop! Look around and see if anything tickles your fancy!")
    sleep(1)
    print("You can also trade in items for credits if you wish!")
    sleep(2)
    space()
    intro = 1
  else:
    print(Fore.CYAN + "Welcome to the shop! How can I help you?")
    sleep(0.5)
    space()
  print(Fore.GREEN + "What would you like to do?")
  print(Fore.YELLOW + '[A]' + Fore.GREEN + " Buy")
  print(Fore.YELLOW + '[B]' + Fore.GREEN + " Sell")
  print(Fore.YELLOW + '[C]' + Fore.GREEN + " Leave")
  space() 
  choice = input(Fore.BLUE + ">> ")

  if choice.upper() == 'A':
    buyingInterface()
  
  elif choice.upper() == 'B':
    sellingInterface()

  else:
    reset()
    optionsHUD()

# Buying Inteface #
def buyingInterface():
  clear()
  print(Fore.GREEN + "Credits: " + Fore.BLUE + str(myPlayer.credits))
  space() 
  print(Fore.GREEN + "The Shop's Inventory and Price:")
  n = 1
  for item, price in shopList.items():
    print(Fore.YELLOW + str(n) + ". " + Fore.CYAN + item + " |---------| " + Fore.MAGENTA + str(price) + " credits")
    n= n + 1
  space()
  print(Fore.GREEN + "Type the number of the item you would like to purchase.")
  print(Fore.GREEN + "Type " + Fore.YELLOW + "0" + Fore.GREEN + " if you would like to go back.")
  space() 
  choice = input(Fore.BLUE + ">> ")
  if choice == '0':
    clear()
    sleep(0.25)
    trading()
  else:
    try:
      boughtItem = buyList[int(choice)-1]
      buy(boughtItem)
    except:
      print(Fore.RED + "Unrecognized input!")
      clear() 
      buyingInterface()

    
# Selling Interface #
def sellingInterface():
  clear()
  print(Fore.GREEN + "Credits: " + Fore.BLUE + str(myPlayer.credits))
  space() 
  print(Fore.GREEN + "Your inventory:")
  if not myPlayer.inventory:
    print(Fore.RED + "You do not have any items in your inventory!")
    space() 
    print(Fore.GREEN + "What would you like to do?")
    print(Fore.YELLOW + "[A]" + Fore.GREEN + " Go back")
    space()
    choice = input(Fore.BLUE + ">> ")
    sleep(1)
    trading()
      
  else:
    n= 1
    for item in myPlayer.inventory:
      print(Fore.YELLOW + str(n) + ". " + Fore.BLUE + item)
      n = n+1
    space() 
    print(Fore.GREEN + "What would you like to do?")
    print(Fore.YELLOW + "[A]" + Fore.GREEN + " Go back")
    print(Fore.GREEN + "To " + Fore.YELLOW + "sell" + Fore.GREEN + ", type in the number of the item you'd wish to sell.")
    space()
    choice = input(Fore.BLUE + ">> ")
    if choice.upper() == 'A':
      sleep(0.5)
      trading()
    else:
      try:
        sellItem = myPlayer.inventory[(int(choice) - 1)]
        sell(sellItem)
        myPlayer.itemsSold = myPlayer.itemsSold + 1
      except:
        print(Fore.RED + "There is no item there!")
      sleep(1)
      sellingInterface()

# Buy #
def buy(item):
  for x in totalItemList:
    if x.name == item:
      if myPlayer.credits >= x.value:
        myPlayer.inventory.append(item)
        myPlayer.credits = myPlayer.credits - x.value
        print(Fore.BLUE + "You " + Fore.GREEN + "bought a " + Fore.YELLOW + "[" + item + "]" + Fore.GREEN + "!")
        sleep(1)
        clear()
        buyingInterface()
      else:
        print(Fore.RED + "You don't have enough credits!")
        sleep(1)
        clear()
        buyingInterface()
# Sell #
def sell(item):
  for x in totalItemList:
    if x.name == item:
      myPlayer.credits = myPlayer.credits + math.ceil(x.value/2)
      myPlayer.inventory.remove(item)

#------------------------------------------------------#
# All functions related to combat
#------------------------------------------------------#

class enemy:
  def __init__(self, name, hp):
    self.name = name
    self.hp = 0
  
# Zombie Enemies #
base = enemy('Zombie', 0)
tough = enemy('Big Zombie', 0)
speed = enemy('Quick Zombie', 0)

# Survivor Enemies #
thug = enemy('Thug', 0)
scavenger = enemy('Scavenger', 0)
leader = enemy('Gang Leader', 0)

zombieAttacks = ['bite', 'scratch', 'yell', 'charge', 'spit']

# Encounter #
def encounter():
  reset()
  print(Fore.GREEN + "An " + Fore.RED + "enemy " + Fore.GREEN + "has appeared!")
  sleep(.5)
  space()
  print(Fore.RED + "Prepare to defend yourself!")
  sleep(1)
  chance = random.randint(1,3)
  if chance == 1:
    enemy = base
    base.hp = random.randint(5,50)
    base.hp = base.hp + healthBoost()
    print(Fore.GREEN + "This " + Fore.RED + "Zombie " + Fore.GREEN + "appears to be weak and frail!")
    sleep(2)
    battle(base)
  elif chance == 2:
    enemy = tough
    tough.hp = random.randint(30,120)
    tough.hp = tough.hp + healthBoost()
    print(Fore.GREEN + "This " + Fore.RED + "Zombie " + Fore.GREEN + "appears to be one of the stronger ones!")
    sleep(2)
    battle(tough)
  elif chance == 3:
    enemy = speed
    speed.hp = random.randint(40,60)
    speed.hp = speed.hp + healthBoost()
    print(Fore.GREEN + "This " + Fore.RED + "Zombie " + Fore.GREEN + "appears to be one of the faster ones!")
    sleep(2)
    battle(speed)

def randDam():
  sign = random.randint(1,2)
  extra = random.randint(1,3)
  if sign == 1:
    damage = 0 - extra
  else:
    damage = 0 + extra
  return damage 

#Flee flag
flee = 0
# Battle #
def battle(zombo):
  global flee 
  flee = 0
  while zombo.hp > 0 and myPlayer.hp > 0 and myPlayer.contamination < 100:
    reset()
    print(Fore.RED + zombo.name + ": " + str(zombo.hp) + " health")
    space()
    print(Fore.GREEN + "What do you want to do?")
    print(Fore.YELLOW + "[A]" + Fore.GREEN + " Attack")
    print(Fore.YELLOW + "[B]" + Fore.GREEN + " Flee")
    space() 
    choice = input(Fore.BLUE + ">> ")
    #ATTACK#
    if choice.upper() == 'A':
      reset() 
      print(Fore.BLUE + "You " + Fore.GREEN + "attack the zombie!")
      chance = random.randint(1,100)
      sleep(1)
      if chance <= 85:
        damage = myPlayer.attack + randDam()
        myPlayer.damageGiven = myPlayer.damageGiven + damage
        print(Fore.BLUE + "You " + Fore.GREEN + "hit the zombie!")
        sleep(1)
        print(Fore.BLUE + "You " + Fore.GREEN + "do " + Fore.YELLOW + str(damage) + Fore.GREEN + " damage!")
        zombo.hp = zombo.hp - damage
        sleep(2)
      else:
        print (Fore.BLUE + "You " + Fore.RED + "missed!")
        sleep(1)
        print (Fore.GREEN + "The " + Fore.RED + "Zombie " + Fore.GREEN + "snarls in retaliation! It looks hungry!")
        sleep(1)
      reset()
      if (zombo.hp <= 0):
        break
      else:
        zAttack(zombo)
        if myPlayer.hp <= 0: break
    elif choice.upper() == 'B':
      print(Fore.BLUE + "You" + Fore.GREEN + " attempt to flee!")
      fleeChance = random.randint(1,100)
      sleep(1)
      print("...")
      sleep(1)
      print("...")
      sleep(1)
      print("...")
      sleep(.5)
      if fleeChance <= 50:
        zombo.hp = 0
        print(Fore.BLUE + "You " + Fore.GREEN + "successfully flee!")
        sleep(2)
        flee = 1
        break
      else:
        print(Fore.BLUE + "You " + Fore.RED + "unsuccessfully " + Fore.GREEN + "flee!")
        zAttack(zombo)
        if myPlayer.hp <= 0: break
        sleep(2)
  # End conditoms #
  if myPlayer.hp == 0:
    gameOver()
  elif myPlayer.contamination >= 100:
    gameOver()
  elif zombo.hp <= 0 and flee == 1:
    reset()
    optionsHUD()
  elif zombo.hp <= 0:
    win()

def zAttack(z):
  attack = random.choice(zombieAttacks)
  if attack == 'bite':
    print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + " tries to " + Fore.YELLOW + "bite " + Fore.GREEN + "you!")
    sleep(1)
    chance = random.randint(1, 100)
    if z.name == "Quick Zombie": chance -= 20
    if (chance <= 65):
      damage = random.randint(8,17) + randDam()
      damage = damage + attackBoost()
      if z.name == 'Big Zombie': damage += 5
      damage = damage - myPlayer.armorStat
      if damage < 0: damage = 0
      myPlayer.damageTaken = myPlayer.damageTaken + damage
      print(Fore.GREEN + "You get " + Fore.RED + "bitten!")
      sleep(1)
      print(Fore.GREEN + "You take " + Fore.RED + str(damage) + " damage!")
      myPlayer.hp = myPlayer.hp - damage
      myPlayer.contamination = myPlayer.contamination + (damage)
      sleep(2)
    else:
      print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + "missed you! You escape the attack with no damage!") 
      sleep(2)
  if attack == 'scratch':
    print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + " tries to " + Fore.YELLOW + "scratch " + Fore.GREEN + "you!")
    sleep(1)
    chance = random.randint(1, 100)
    if z.name == "Quick Zombie": chance -= 20
    if (chance <= 85):
      damage = random.randint(8,17) + randDam()
      damage = damage + attackBoost()
      if z.name == 'Big Zombie': damage += 5
      damage = damage - myPlayer.armorStat
      if damage < 0: damage = 0
      myPlayer.damageTaken = myPlayer.damageTaken + damage
      print(Fore.GREEN + "You get " + Fore.RED + "scratched!")
      sleep(1)
      print(Fore.GREEN + "You take " + Fore.RED + str(damage) + " damage!")
      myPlayer.hp = myPlayer.hp - damage
      myPlayer.contamination = myPlayer.contamination + math.ceil(damage/2)
      sleep(2)
    else:
      print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + "missed you! You escape the attack with no damage!") 
      sleep(2)
  if attack == 'charge':
    print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + " tries to " + Fore.YELLOW + "charge " + Fore.GREEN + "at you!")
    sleep(1)
    chance = random.randint(1, 100)
    if z.name == "Quick Zombie": chance -= 20
    if (chance <= 90):
      damage = random.randint(3, 6) + randDam()
      damage = damage + attackBoost()
      if z.name == 'Big Zombie': damage += 5
      damage = damage - myPlayer.armorStat
      if damage < 0: damage = 0
      myPlayer.damageTaken = myPlayer.damageTaken + damage
      print(Fore.GREEN + "You get " + Fore.RED + "knocked over!")
      sleep(1)
      print(Fore.GREEN + "You take " + Fore.RED + str(damage) + " damage!")
      myPlayer.hp = myPlayer.hp - damage
      myPlayer.contamination = myPlayer.contamination + math.ceil(damage/5)
      sleep(2)
    else:
      print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + "missed you! You dodged the attack!") 
      sleep(2)
  if attack == 'spit':
    print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + " tries to " + Fore.YELLOW + "spit " + Fore.MAGENTA + "infectious blood " + Fore.GREEN + "at you!")
    sleep(1)
    chance = random.randint(1, 100)
    if z.name == "Quick Zombie": chance -= 20
    if (chance <= 55):
      damage = random.randint(2,4) + randDam()
      damage = damage + attackBoost()
      if z.name == 'Big Zombie': damage += 5
      damage = damage - myPlayer.armorStat
      if damage < 0: damage = 0
      myPlayer.damageTaken = myPlayer.damageTaken + damage
      print(Fore.GREEN + "You get " + Fore.RED + "splattered!")
      sleep(1)
      print(Fore.GREEN + "You take " + Fore.RED + str(damage) + " damage!")
      myPlayer.hp = myPlayer.hp - damage
      myPlayer.contamination = myPlayer.contamination + 10
      sleep(2)
    else:
      print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + "missed you! You escape splatter-free!") 
      sleep(2)
  if attack == 'yell':
    print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + " tries to " + Fore.YELLOW + "roar " + Fore.GREEN + "at you with a blood curdling shriek!")
    sleep(1)
    chance = random.randint(1, 100)
    if z.name == "Quick Zombie": chance -= 20
    if (chance <= 70):
      damage = random.randint(6,9) + randDam()
      damage = damage + attackBoost()
      if z.name == 'Big Zombie': damage += 5
      damage = damage - myPlayer.armorStat
      if damage < 0: damage = 0
      myPlayer.damageTaken = myPlayer.damageTaken + damage
      print(Fore.GREEN + "Your ears " + Fore.RED + "are viciuosly assualted!")
      sleep(1)
      print(Fore.GREEN + "You take " + Fore.RED + str(damage) + " damage!")
      myPlayer.hp = myPlayer.hp - damage
      myPlayer.contamination = myPlayer.contamination + math.ceil(damage/10)
      sleep(2)
    else:
      print(Fore.GREEN + "The " + Fore.RED + z.name + Fore.GREEN + "shrieks, but you cover your ears in time! You escape the attack with no damage!") 
      sleep(2)
# Game Over #
def gameOver():
  if myPlayer.hp <= 0:
    clear()
    print(Fore.RED + "You have died!")
    sleep(1)
    print(Fore.RED + "Better luck next time!")
    sleep(2)
    
  elif myPlayer.contamination >= 100:
    clear()
    print(Fore.RED + "You have been overcome with the virus! You have become one of the monsters you've been fighting!")
    sleep(1)
    print(Fore.RED + "Better luck next time!")
    sleep(2)
  
  checkStats()

# Win counter #
def win():
  clear()
  print(Fore.GREEN + "|--------" + Fore.BLUE + "You " + Fore.GREEN + "  have won!" + Fore.GREEN + "--------|")
  myPlayer.killed = myPlayer.killed + 1
  space()
  print(Fore.BLUE + "You " + Fore.GREEN + "have killed " + Fore.RED + myPlayer.killed + " zombies" + Fore.GREEN + "!")
  sleep(1)
  reset()
  optionsHUD()

# -- Difficulty Increaser -- #
# Health Boost #
def healthBoost():
  boost = myPlayer.killed * 2
  return boost
# If killed =+ 5
def attackBoost():
  boost = math.ceil(myPlayer.killed/3)
  return boost

# -- Show Map -- #
def showMap():
  reset()
  print(Fore.BLUE + " 'This is the rough map I found...' ")
  space()
  print(Fore.GREEN + "----------------------------------------------------")
  print(Fore.LIGHTYELLOW_EX + "Hive ----- Highway ----- Supply ----- Ruined Building")
  print(Fore.GREEN + "----------------------------------------------------")
  print(Fore.LIGHTYELLOW_EX + "Ruined Building - Highway - Traders Hub - Ruined Building")
  print(Fore.GREEN + "----------------------------------------------------")
  print(Fore.LIGHTYELLOW_EX + "Gun Shop ------ Highway ------ Hive ------ Hospital")
  print(Fore.GREEN + "----------------------------------------------------")
  print(Fore.LIGHTYELLOW_EX + "Highway ------ Highway ------ Highway ------ Highway")
  print(Fore.GREEN + "----------------------------------------------------")
  print(Fore.LIGHTYELLOW_EX + "Hive ------- Highway ------- Gun Shop ------- Supply")
  print(Fore.GREEN + "----------------------------------------------------")
  print(Fore.LIGHTYELLOW_EX + "Hospital ------- Highway ------- Supply ------- Hive")
  print(Fore.GREEN + "----------------------------------------------------")
  space() 
  print(Fore.GREEN + "Press any key to return")
  space() 
  choice = input(Fore.BLUE + ">> ")
  reset() 
  optionsHUD()


quest = 0
# Quest 1 #
def quest1():
  if quest == 1:
    clear()
    print(Fore.BLUE + "You")


def main():
  startGame()
  reset()
  optionsHUD()


main()