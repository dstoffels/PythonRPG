import threading
from InputHandling.handleInput import handleUserInput
from constants import MAIN_MENU, MAIN_MENU_ERR_MSG, NEW_GAME_INTRO
from helpers import validateIntInput
from locations.locations import getLocations

gameActive = True #global
locationMap = getLocations()
startingLocation = (1,6)

def runInputThread():
  def userInput():
    while gameActive:
      handleUserInput()

  threading.Thread(target= userInput).start()

def RunGame():
  print(NEW_GAME_INTRO)
  print(locationMap[startingLocation].displayDescription(locationMap))
  runInputThread()

def displayMainMenu():
  userInput = validateIntInput(MAIN_MENU)

  match userInput:
    case 1:
      RunGame()
    case 2:
      print('game instructions here') #FIXME: need game instructions
    case 3:
      print('Until next time, hero')
      exit()
    case _:
      print(MAIN_MENU_ERR_MSG) #FIXME: need input validation


displayMainMenu()
