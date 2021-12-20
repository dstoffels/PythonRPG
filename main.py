from contextlib import ExitStack
import threading
import threading

MAIN_MENU = '''Welcome Hercules!
1) New Game
2) How To Play
3) Exit
'''

gameActive = True #global

def runInputThread():
  def userInput():
    global gameActive

    while gameActive:
      i = input('> ')
      if(i == 'q'):
        gameActive = False

  threading.Thread(target= userInput).start()

runInputThread()