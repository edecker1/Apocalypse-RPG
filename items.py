# -- This file will house all of the items -- #
# -- Imports -- #
from colorama import Fore, Back, Style
import random, math

# -- Items -- #
#-- Basic Item Class --#
class Item:
  def __init__(self, name, description, value):
    self.name = name
    self.description = description
    self.value = value
  def __str__(self):
    text = Fore.GREEN + self.name + ": " + Fore.BLUE + self.description + Fore.YELLOW + "  || Worth: " + str(self.value) + " credits"
    return text
  def price(self):
    cost = self.value * 1.25
    return cost
  def showPrice(self, x):
    cost = self.value * 1.25
    text = Fore.BLUE + "||  " + str(x) + ". " + self.name + "  --  " + Fore.YELLOW + str(cost) + " credits" + Fore.BLUE + ""
    return text
  def sellPrice(self, x):
    text = Fore.BLUE + "||  " + str(x) + ". " + self.name + "  --  " + Fore.YELLOW + str(self.value) + " credits" + Fore.BLUE + "  ||" 
    return text


class Weapon(Item):
  def __init__(self, name, description, value, qDice, die, chance, action):
    super().__init__(name, description, value)
    self.qDice = qDice
    self.die = die
    self.chance = chance
    self.action = action
  def damage(self):
    total = 0
    for x in range(self.qDice):
      diceRoll = random.randint(1, self.die)
      total += diceRoll
    return total


class Usable(Item):
  def __init__(self, name, description, value, attribute, benefit):
    super().__init__(name, description, value)
    self.attribute = attribute
    self.benefit = benefit

class Armor(Item):
  def __init__(self, name, description, value, defense):
    super().__init__(name, description, value)
    self.defense = defense
