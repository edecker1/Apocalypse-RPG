# --- This is the module for all functions to use throughout the code --- #

# -- Imports -- #
from time import sleep
import os


# -- Waiting Function to simulate loading -- #
def waiting():
    space()
    sleep(1)
    print("...")
    space()
    sleep(1)
    print("...")
    sleep(1)
    space()
    print("...")
    space()
    sleep(0.5)


#-- Function to clear the screen -- #
def clear():
    os.system('cls')


#-- Space Function to space out --#
def space(x):
  for i in range(x):
    print("")

#-- Reset Function --#
def reset():
    clear()
    HUD()
    space()


def error():
  print(Back.RED + Fore.WHITE + "Error! Unrecognized")
  print(Style.RESET_ALL)
  sleep(0.5)
  reset()
  optionsHUD()