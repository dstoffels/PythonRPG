from InputHandling.handleInput import runInputThread
from constants import MAIN_MENU, MAIN_MENU_ERR_MSG, NEW_GAME_INTRO
from helpers import validateIntInput
from locations.locations import LOCATIONS
from gameState import GameState

def Start():
  while True:
    displayMainMenu()

def RunGame():
  state = GameState()
  
  print(NEW_GAME_INTRO)
  state.player.currentLocation.displayDescription(LOCATIONS)
  runInputThread(state)

def displayMainMenu():
  while True:
    userInput = validateIntInput(MAIN_MENU)
    match userInput:
      case 1:
        RunGame()
      case 2:
        print('game instructions here') #FIXME: need game instructions
      case 3:
        print('\nUntil next time, hero!\n')
        exit()
      case _:
        print(MAIN_MENU_ERR_MSG) #FIXME: need input validation

displayMainMenu()