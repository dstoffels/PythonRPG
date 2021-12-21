import threading
from constants import MAIN_MENU
from helpers import validateIntInput


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
  userInput = validateIntInput(MAIN_MENU) #FIXME: need int validation

  match userInput:
    case 1:
      runInputThread() #FIXME: need RunGame function that includes runInputThread
    case 2:
      print('game instructions here') #FIXME: need game instructions
    case 3:
      print('Until next time, hero')
      exit()
    case _:
      print('ERROR! ERROR! ERROR!') #FIXME: need input validation


displayMainMenu()
