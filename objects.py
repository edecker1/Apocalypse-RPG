# -- This file will have all of the objects created from the classes -- #

# -- Import Moduels -- #
from battle import *
from character import *
from items import *
from shop import *
from travel import * 
from story import *

# || -- Item Objects -- || #
# Armor List #
# name, description, value, armor

casual = Armor('Casual Clothes', 'Just some casual streetwear clothes', 20, 1)
work = Armor("Worker's Clothes", 'Clothes with some padding, worn by those who do manual labor.', 40, 2)
leather = Armor('Reinforced Leather Clothes', 'Leather clothes with some reinforcement. Seems like it can take a hit.', 80, 4)
police = Armor('Police Armor', 'Heavy armor worn by police officers expecting trouble.', 140, 7)
army = Armor("Military Armor", 'Military grade armor', 200, 10)
shinobi = Armor("Jonin Uniform", 'Armor that looks straight from an anime!', 300, 15)
akatsuki = Armor("Akatsuki Robes", 'The legendary black robes covered in the signature red clouds...', 1000, 50)

# Weapon List #
# name, description, value, qDice, die, chance, action #
stick = Weapon('Sharp Stick', 'A sharpened stick that may do some damage, but not much.', 10, 2, 3, 85, 'stabs') # 2 - 6 damage
bbat = Weapon('Broken Bat', 'A wooden baseball bats thats been broken.', 12, 3, 2, 90, 'whacks') # 3 - 6 damage
bat = Weapon('Bat', 'A baseball bat that could be used to shatter some skulls.', 15, 3, 3, 85, 'whacks') # 3 - 9 damage
nbat = Weapon('Nailed Bat', 'A baseball bat with a large nail sticking out from it.', 20, 3, 4, 80, 'stabs') # 3 - 12 damage
crowb = Weapon('Crowbar', 'A crowbar found discarded by the wayside.', 20, 3, 4, 80, 'whacks') # 3 - 12 damage
hammer = Weapon('Hammer', 'A small household hammer.', 25, 3, 5, 90, 'smashes') # 3 - 15 damage
bow = Weapon('Longbow', 'A large bow straight from the Middle Ages!', 30, 3, 6, 80, 'shoots at') # 3 - 18 damage
axe = Weapon('Rusty Axe', 'An axe that has seen some time but still has its sharp edge', 30, 5, 3, 85, 'slashes') # 5 - 15 damage
knife = Weapon('Knife', 'A small sharpened knife perfect for cutting', 30, 5, 3, 95, 'stabs') # 5 - 15 damage
sword = Weapon('Sword', 'A sharp sword ready for slashing or cutting any enemy in the users path.', 40, 6, 3, 85, 'slashes') # 6 - 18 damage
xbow = Weapon('Crossbow', 'A hunting crossbow. Could be useful to take out some Zombie heads...', 45, 4, 5, 80, 'shoots at') # 4 - 20 damage
dagger = Weapon('Dagger', 'A dagger made for combat.',50, 5, 4, 95, 'stabs') # 5 - 20 damage
katana = Weapon('Katana', 'A sharpened sword made for cutting.', 60, 7, 3, 80, 'cuts') # 7 - 21 damage
kunai = Weapon('Kunai', 'A small blade commonly used by ninja.', 60, 7, 3, 100, 'slashes') # 7 - 21 damage
pistol = Weapon('Pistol', 'A standard pistol carried by most police officers.', 75, 5, 5, 77, 'shoots at') # 5 - 25 damage
de = Weapon('Desert Eagle', 'A large, flashy pistol capable of severe damage.', 85, 3, 10, 70, 'shoot at') # 3 - 30 damage
sledge = Weapon('Sledgehammer', 'A large sledgehammer that packs quite a punch.', 100, 5, 6, 85, 'smashes') # 5 - 30 damage
rifle = Weapon('Rifle', 'A standard hunting rifle.', 150, 5, 7, 75, 'shoots at') # 5 - 35 damage
smg = Weapon('Submachine Gun', 'A smaller, more mobile machine gun used by military personel.', 200, 5, 8, 75,'shoot at') # 5 - 40 damage
minato = Weapon('Flying Raijin Kunai', 'Kunai with the mark of the legendary Fourth Hokage on it.', 400, 20, 2, 80, 'stabs') # 20 - 40 damage
ar = Weapon('Assault Rifle', 'A deadly assault rife used by military personel.', 240, 5, 9, 70, 'shoot at') # 5 - 45 damage
xsaw = Weapon('Chainsaw', 'A chainsaw perfect for cutting through anything whether it be a tree or a zombie.', 350, 10, 5, 90, 'cuts through') # 10 - 50 damage
sasuke = Weapon('The Kusanagi', 'The famous blade used by Sasuke Uchiha. It is said to be a perfect conduit for lightning.', 700, 10, 5, 80, 'slashes') # 10 - 50 damage
plasma = Weapon('Plasma Sword', 'A futuristic sword capable of cutting through anything.', 1000, 10, 7, 90, 'slices through') # 10 - 70 damage
rocket = Weapon("RPG", "A large rocket launcher capable of destroying massive troves of zombies at once.", 2000, 20, 5, 70, 'blasts') # 20 - 100 damage




# def __init__(self, name, description, value, attribute, benefit
# Usable Item List #
# Medical Health Supplies #
bandage = Usable('Bandage', 'A dirty bandage still clean enough for use.', 100, 'hp', 10)
bandaid = Usable('Barbie Bandaids', "A box of bandaids that are pink", 50, 'hp', 5)
pain = Usable('Pain Medicine', 'Over the counter pain medicine taht will help tolerate injuries.', 150, 'hp', 15)
pain2 = Usable('Pain Medicine X', "Namebrand pain medicine that is supposed to help with serious injuries and surgeries", 300, 'hp', 30)
surgery = Usable("Surgeon's Kit", "A kit used by surgeons.", 750, 'hp', 75)
firstAid = Usable('First Aid Kit', 'A first aid kit complete enough to patch up most wounds.', 250, 'hp', 25)
doctors = Usable("Doctor's Kit", 'Tools used by doctors. Capable of treating major wounds.', 500, 'hp', 50)
# Medical Disease Supplies #
virusOne = Usable('Virus Killer', 'A revolutionary drug made hastily to combat the virus', 200, 'c', 20)
virusTwo = Usable('Virus Killer X', 'The more advanced version of the Virus Killer which has proven more effective at preventing the virus.', 350, 'c', 35)
vac = Usable("Experimental Vaccine", 'One of the original attemots at making a vaccine for this virus.', 100, 'c', 10)
vac2 = Usable("Test Drug", 'One of the earlier prototypes of the Virus Killer drug.', 200, 'c', 15)
detox = Usable("Detox Kit", "A kit used to detox the system of the virus. Has little success.", 100, 'c', 5)
# -- Food items -- #
cheese = Usable('Cheese', 'A nice piece of cheese.', 10, 'hp', 4)
bread = Usable('Slice of Toast', 'A cold piece of toast', 5, 'hp', 2)
ham = Usable("Piece of Ham", "A warm piece of ham", 10, 'hp', 4)
sandwich = Usable("Ham Sandwich", "A basic ham sandwich", 25, 'hp', 10)
chicken = Usable("Chicken Tenders", "Some old chicken tenders", 20, "hp", 8)
pie = Usable("Pie", "A half eaten Apple Pie", 20, "hp", 8)
burrito = Usable("Burrito", "A bean burrito from Bell Taco", 35, 'hp', 14)
taco = Usable("Taco", "A chicken and cheese taco from Bell Taco", 10, 'hp', 4)
apple = Usable("Apple", "A delicious apple", 10, 'hp', 4)
crab = Usable("Crab Rangoon", "One fo the most delicious treats", 15, 'hp', 6)
frenchFries = Usable("French Fries", "A half empty box of french fries with some old ketchup", 10, 'hp', 4)
wrap = Usable("Caesar Wrap", "A nice, big chicken caesar wrap", 40, 'hp', 16)

# -- Shop Objects -- #
bazaar = Shop({bow : 3, bandage : 0, sword : 0, cheese : 10, virusOne : 1}, [bow, bandage, sword, cheese, virusOne])

# -- Attacks -- #

# || Zombie Attacks || #
# name, command, qDice, die, chance, infection #
scratch = Attack('Scratch', 'scratches', 3, 6, 80, 2)
bite = Attack('Bite', 'bites', 5, 6, 70, 10)
swing = Attack("Swing", 'swings at', 3, 4, 90, 3)
rottingFlesh = Attack("Throw Rotting Flesh", 'throws rotting flesh at', 2, 4, 75, 7)
plagueBite = Attack("Plague Bite", 'infectiously bites', 6, 8, 70, 20)
plagueScratch = Attack("Plague Scratch", 'infectiously scratches', 3, 8, 75, 10)
plagueSpit = Attack("Plague Spit", "spits infected blood at", 2, 4, 75, 30)
swat = Attack("Swat", "swats", 7, 4, 85, 2)
crush = Attack("Crush", 'crushes', 10, 6, 60, 2)
tackle = Attack("Tackle", 'tackles', 5, 8, 65, 5)
screech = Attack("Screech", 'screeches', 3, 10, 95, 0)
lick = Attack("Lick", 'licks', 1, 6, 60, 40)
pounce = Attack("Pounce", 'pounces', 4, 6, 85, 15)

# || Human Attacks || #
punch = Attack('Punch', 'punches', 2, 4, 90, 0)
kick = Attack('Kick', 'kicks', 2, 5, 85, 0)
slash = Attack('Slash', 'slashes', 4, 6, 80, 0)
stab = Attack('Stab', 'stabs', 5, 8, 80, 0)
shoot = Attack('Shoot', 'shoot', 10, 6, 80, 0)


# -- Enemies -- #
# name, hp, maxHp, attacks, loot, xp #

# || Zombie Enemies || #

# | Basic Zombies | #
zobM = Enemy("Zombie Man", 0, 15, [bite, swing], ["Nothing", "Nothing", "Credits"], 5)
zobM1 = Enemy("Zombie Man", 0, 15, [bite, swing], ["Nothing", "Nothing", "Credits"], 5)
zobM2 = Enemy("Zombie Man", 0, 15, [bite, swing], ["Nothing", "Nothing", "Credits"], 5)
zobW = Enemy("Zombie Woman", 0, 25, [scratch, bite, swing], ["Nothing", "Nothing", "Credits"], 7)
zobW1 = Enemy("Zombie Woman", 0, 25, [scratch, bite, swing], ["Nothing", "Nothing", "Credits"], 7)
zobW2 = Enemy("Zombie Woman", 0, 25, [scratch, bite, swing], ["Nothing", "Nothing", "Credits"], 7)
zobC = Enemy("Zombie Child", 0, 9, [bite], ["Nothing", "Nothing", "Credits"], 3)
zobC1 = Enemy("Zombie Child", 0, 9, [bite], ["Nothing", "Nothing", "Credits"], 3)
zobC2 = Enemy("Zombie Child", 0, 9, [bite], ["Nothing", "Nothing", "Credits"], 3)
zobD = Enemy("Zombie Dog", 0, 15, [bite, pounce, scratch], ["Nothing", "Nothing", "Credits"], 5)
zobD1 = Enemy("Zombie Dog", 0, 15, [bite, pounce, scratch], ["Nothing", "Nothing", "Credits"], 5)
zobD2 = Enemy("Zombie Dog", 0, 15, [bite, pounce, scratch], ["Nothing", "Nothing", "Credits"], 5)
zobDL = Enemy("Zombie Hound", 0, 30, [plagueBite, pounce, plagueScratch, lick, tackle], ["Nothing", "Nothing", "Credits"], 10)
zobDL1 = Enemy("Zombie Hound", 0, 30, [plagueBite, pounce, plagueScratch, lick, tackle], ["Nothing", "Nothing", "Credits"], 10)
zobDL2 = Enemy("Zombie Hound", 0, 30, [plagueBite, pounce, plagueScratch, lick, tackle], ["Nothing", "Nothing", "Credits"], 10)

# | Specialty Zombies | #
rottenZob = Enemy("Rotting Zombie", 0, 10, [swing, rottingFlesh], ["Nothing", "Nothing", "Credits"], 4)
plagueZob = Enemy("Plague Zombie", 0, 35, [plagueBite, plagueScratch, plagueSpit], ["Nothing", "Nothing", "Credits"], 10)
tankZob = Enemy("Zombie Tank", 0, 120, [swat, crush, tackle], ["Nothing", "Nothing", "Credits"], 15)
screamerZob = Enemy("Screamer", 0, 45, [screech, lick, swing], ["Nothing", "Nothing", "Credits"], 15)


# || Human Enemies || #
bandit = Enemy("Bandit", 0, 100, [punch, kick, slash, stab], [cheese], 8)
scout = Enemy("Bandit Scout", 0, 70, [punch, kick, slash, stab], [cheese], 6)
soldier = Enemy("Soldier Thug", 0, 150, [punch, kick, shoot], [cheese], 12)
guard = Enemy("Bandit Guard", 0, 150, [punch, kick, slash, stab, shoot], [cheese], 12)

# Locations #
# | name, description, clear, search, limit, enemy, loot, encounter,, maxE | #
store = Location("Abandoned Department Store", "A store that was ransacked by looters and zombies...", False, 0, 7, [zobM, zobM1, zobM2, zobW, zobW1, zobW2, zobC, zobC1, zobC2, zobD, zobD1, zobD2], [knife, bandage, bandaid, apple, bat, "Nothing", "Nothing", "Credits", "Credits"], 50, 3 )
store2 = Location("Abandoned Retail Store", "A store that once thrived left to the Undead...", False, 0, 7, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [cheese, bow, axe], 60, 4  )
supermarket = Location("Destroyed Supermarket", "A pillaged supermarket overflowing with dead bodies...", False, 0, 8, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [cheese, firstAid, bow, pistol], 50, 3 )
food = Location("Pillaged Restaurant", "A run down restaurant with some hungry Undead inside...", False, 0, 6, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [cheese, sword, dagger, knife], 35, 2 )
street = Location("Desolate Street", "A street now devoid of life and activity...", False, 0, 4, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [pistol, sword, axe, sasuke], 25, 5) 
street1 = Location("Destroyed Street", "A street once filled with life, now filled with carnage and death...", False, 0, 6, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [pistol, sword, axe, sasuke], 65, 5 )
alley = Location("Dark Alley", "An alleyway covered in bodies...", False, 0, 3, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [pistol, virusOne], 65, 2 )
highwayStart = Location("Highway Entrance", "The entrance to the highway...", False, 0, 4, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [firstAid, virusOne, virusTwo], 35, 5 )
highway = Location("Highway", "The highway is filled with destroyed cars and dead bodies...", False, 0, 7, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [pistol, sword], 70, 5 )
highway1 = Location("Highway", "The highway is filled with destroyed cars and dead bodies...", False, 0, 5, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [cheese, bandage], 65, 5 )
apartment = Location("Apartment Complex", "An apartment complex that seems a little too quiet...", False, 0, 12, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [bandage, cheese], 55, 3)
hospital = Location("Cordova Hospital", "What was once an elegant, beautiful hospital is now decrepid and littered with zombies...", False, 0, 15, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [bandage, firstAid, virusOne], 50, 3 )
garage = Location("Garage", "A dark parking garage. You can faintly hear something scraping against the ground deeper inside...", False, 0, 12, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [pistol, bandage], 20, 2 )
parking = Location("Parking Lot", "A depressing sight for what was once the parking lot that was used to be used for hospital parking...", False, 0, 6, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [bandage, cheese], 30, 2 )
smallHouse = Location("Small House", "A small one floor house...", False, 0, 5, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [bandage, cheese], 30, 2 )
mediumHouse = Location("House", "A small two floor house...", False, 0, 8, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [bandage, cheese], 40, 2)
house = Location("House", "A multi-floor house that could hold a relatively large family...", False, 0, 14, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [bandage, cheese], 40, 3 )
construction = Location("Construction Site", "A dangerous site that no longer follows the safety protocals...", False, 0, 12, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [cheese, bandage], 50, 4 )
military = Location("Military Outpost", "A failed attempt at exerting the military to take control of this virus...", False, 0, 8, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [de, ar, smg, pistol], 70, 5 )
police = Location("Police Station", "The remnants of what was once a corrupt police station...", False, 0, 6, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [bandage, pistol], 70, 3 )
postOffice = Location("Post Office", "A destroyed and picked over post office...", False, 0, 9, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [bandage, pistol], 20, 2 )
gunShop = Location("Gun Shop", "A gun shop that may still have some weaponry if it has not been looted completely...", False, 0, 3, [zobM, zobM1, zobM2, zobW, zobW1, zobW2], [ar], 80, 5 )
# Warzones # 
# name, description, clear, heads, enemy, prize #
bandit = Warzone("Bandit Hideout", "A hideout of survivors who are willing to kill you to survive...", False, random.randint(7, 15), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], rifle)
bandit1 = Warzone("Bandit Hideout", "A hideout of survivors who are willing to kill you to survive...", False, random.randint(7, 15), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], rifle)
horde = Warzone("Zombie Horde", "A horde of Zombies gathering!", False, random.randint(9, 60), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], smg)
horde1 = Warzone("Zombie Horde", "A horde of Zombies gathering!", False, random.randint(9, 60), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], smg)
horde2 = Warzone("Zombie Horde", "A horde of Zombies gathering!", False, random.randint(9, 60), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], smg)
horde3 = Warzone("Zombie Horde", "A horde of Zombies gathering!", False, random.randint(9, 60), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], smg)
horde4 = Warzone("Zombie Horde", "A horde of Zombies gathering!", False, random.randint(9, 60), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], smg)
hive = Warzone("Zombie Hive", "For some reason the zombies are gathering here... it is almost like an army!", False, random.randint(61, 150), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], xsaw)
hive1 = Warzone("Zombie Hive", "For some reason the zombies are gathering here... it is almost like an army!", False, random.randint(61, 150), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], xsaw)
hive2 = Warzone("Zombie Hive", "For some reason the zombies are gathering here... it is almost like an army!", False, random.randint(61, 150), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], xsaw)
crash = Warzone("Crash Site", "A multi car crash that has become the new home for zombies!", False, random.randint(20, 45), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], sasuke)
enclave = Warzone("Survivor Enclave", "An enclave of survivors! Unfortunately, their response to your greeting was to shoot their guns...", False, random.randint(15, 24), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], ar)
fortress = Warzone("Phoenix Fortress", "A fortress created by the hostile faction 'The Phoenix'. They live by the motto 'Kill or be Killed'.", False, random.randint(85, 105), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], sasuke)
outpost = Warzone("Outpost", "An outpost by the cruel, twisted faction known as 'The Grave Watchers'.", False, random.randint(12, 18), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], ar)
wall = Warzone("Wall", "This wall protects the base of 'The Grave Watchers'.", False, random.randint(30, 40), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], smg)
settlement = Warzone("The Grave Watchers", "The home base of the nefarious faction, 'The Grave Watchers'.", False, random.randint(100, 130), [zobM, zobM1, zobM2, zobW, zobW1, zobW2], ar)
# Friendly #
trading = Trader("Trading Spot", "A spot where fellow survivors will trade with credits for items of need.", bazaar)
start = Location("Placeholder", "Placeholder Descript", True, 1, 1, [], [], 0, 0)

# JOBS #
# self, name, description, strength, dexterity, endurance
normal = Job("Normal Person", "Just a normal person", 5, 5, 5)
bruiser = Job('Bruiser', "A strong person who excels in combat", 15, 5, 5)
scavenger = Job('Scavenger', "A quick person who excels in scavenging for supplies", 5, 15, 5)
insomniac = Job('Insomniac', 'A tough person who can endure more than a normal person', 5, 5, 15)
jobs = [bruiser, scavenger, insomniac]
# -- Main Objects -- #
levelCap = {
	1 : 100,
	2 : 145,
	3 : 175,
	4 : 210,
	5 : 250,
	6 : 300,
	7 : 360,
	8 : 430,
	9 : 515,
	10 : 620
}

battle = Battle([], [], 0, 0, 0)
# self, name, hp, maxHp, contamination, inventory, weapon, armor, credits, coordinates , level, cap, experience#
me = Player("Player", 100, 100, 0, [bandage, bandage], stick, casual, 25, 1, 1, levelCap, 0, normal, 5, 5, 5 )
story = Story()

"""
-------------
| Store | Supermarket | Food | Bandit| apartment | hospital | garage | parking lot |
-------------
| Street | Alley | Street | Horde | Highway Start | Highway | Highway | Crash |
-------------
| Trader | store | Horde | Hive | Horde | enclave | small house  | #Fortess |
-------------
| house | medium house | Horde | military | police | #outpost | post office  | gun shop |
-------------
| HomeBase | hive | hive | horde | Construction site | bandit | #thugs Wall  | #Settlement |
-------------
| Barber Shop | Sub Shop | Weapons Merchant | bank | Armor Merchant | coffee shop | Medical Supplies  | library |
-------------

"""

world = {
	1 : store,
	2 : supermarket,
	3 : food,
	4 : bandit,
	5 : apartment,
	6 : hospital,
	7 : garage,
	8 : parking,
	11 : street,
	12 : alley,
	13 : street1,
	14 : horde,
	15 : highwayStart,
	16 : highway,
	17 : highway1,
	18 : crash,
	21 : trading,
	22 : store2,
	23 : horde1,
	24 : hive,
	25 : horde2,
	26 : enclave,
	27 : smallHouse,
	28 : fortress,
	31 : house,
	32 : mediumHouse,
	33 : horde3,
	34 : military,
	35 : police,
	36 : outpost,
	37 : postOffice,
	38 : gunShop,
	41 : start,
	42 : hive1,
	43 : hive2,
	44 : horde4,
	45 : construction,
	46 : bandit1,
	47 : wall,
	48 : settlement
}

save = SaveSystem()
