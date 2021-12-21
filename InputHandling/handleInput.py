import threading
from InputHandling.commands import COMMANDS
from gameState import GameState

prompt = '> '

def handleUserInput(gameState):
  userInput = str.lower(input(prompt))

  try:
    COMMANDS[userInput](gameState)
  except:
    print('unknown command')

def runInputThread(gameState):
  def userInput():
    while gameState.isActive:
      handleUserInput(gameState)

  threading.Thread(target= userInput).start()