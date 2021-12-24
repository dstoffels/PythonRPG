import threading
from InputHandling.commands import COMMANDS
from gameState import GameState

def handleUserInput(gameState: GameState):
  while gameState.isActive:
    prompt = gameState.commandPrompt()
    userInput = str.lower(input(prompt))
    try:
      COMMANDS[userInput](gameState)
    except:
      print('unknown command')

def runInputThread(gameState):
  # inputThread = threading.Thread(target= lambda : handleUserInput(gameState)).start()
  handleUserInput(gameState)
  
  