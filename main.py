from InputHandling.handleInput import runInputThread
from constants import MAIN_MENU, MAIN_MENU_ERR_MSG, NEW_GAME_INTRO
from helpers import validateIntInput
from locations.locations import LOCATIONS
from gameState import GameState

gameActive = True # will an entire game state need to be stored in a class object?
startingLocation = (1,6)

def Start():
  while True:
    displayMainMenu()

def RunGame():
  state = GameState()
  print(NEW_GAME_INTRO)
  print(LOCATIONS[startingLocation].displayDescription(LOCATIONS))
  runInputThread(state)

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
