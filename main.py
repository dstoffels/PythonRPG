from contextlib import ExitStack
import threading
from constants import MAIN_MENU
import threading

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
  userInput = input(MAIN_MENU)

  match userInput:
    case 1:
      runInputThread()
    case 2:
      print('PLACEHOLDER: game instructions here') #FIXME: need game instructions
    case 3:
      print('Until next time, hero')
      exit()
    case _:
      print('PLACEHOLDER: ERROR! ERROR! ERROR!') #FIXME: need input validation



