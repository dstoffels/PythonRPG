import threading
from constants import MAIN_MENU, MAIN_MENU_ERR_MSG
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

def displayMainMenu():
  userInput = validateIntInput(MAIN_MENU)

  match userInput:
    case 1:
      runInputThread() #FIXME: need RunGame function that includes runInputThread
    case 2:
      print('game instructions here') #FIXME: need game instructions
    case 3:
      print('Until next time, hero')
      exit()
    case 0:
      print(locationMap[1,6].coordinates)
    case _:
      print(MAIN_MENU_ERR_MSG) #FIXME: need input validation


print(locationMap[1,6].displayDescription(locationMap))
# displayMainMenu()
