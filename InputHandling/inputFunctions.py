from gameState import GameState
from helpers import tryMove
from locations.locations import LOCATIONS

def handleQuit(gameState: GameState):
  userInput = str.lower(input('Are you sure you want to quit? All progress will be lost. > '))
  if(userInput == 'y' or userInput == 'yes'):
    gameState.endGame()

def handleMove(direction, state: GameState):
  player = state.player
  if(state.player.isEngagedInCombat):
    print(f'{player.target.name} blocks your escape!\n')
  else:
    tryMove(player, direction)

def handleLook(gameState: GameState):
  gameState.player.currentLocation.displayDescription(LOCATIONS)

def handleSelectAttack(attackIndex, gameState: GameState):
  newAttack = gameState.player.selectAttack(attackIndex)
  print(f'Switching to {newAttack.name} attack.\n')

def handleAttack(gameState: GameState):
  player = gameState.player
  if(not player.isEngagedInCombat):
    player.attack()
  else:
    print('Already engaged in combat!\n')