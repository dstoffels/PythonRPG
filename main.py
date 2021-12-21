import threading
from constants import MAIN_MENU, MAIN_MENU_ERR_MSG, NEW_GAME_INTRO
from helpers import validateIntInput
from locations import getLocations

locationMap = getLocations()
gameActive = True #global

def runInputThread():
  def userInput():
    global gameActive

    while gameActive:
      i = input('> ')
      if(i == 'q'):
        gameActive = False

  threading.Thread(target= userInput).start()

def RunGame():
  print(NEW_GAME_INTRO)
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
