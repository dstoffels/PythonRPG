from constants import HOW_TO_PLAY
from gameState import GameState
from helpers import tryMove
from locations.locations import LOCATIONS

def handleQuit(state: GameState):
  userInput = str.lower(input('Are you sure you want to quit? All progress will be lost. > '))
  if(userInput == 'y' or userInput == 'yes'):
    state.endGame()

def handleMove(direction, state: GameState):
  player = state.player
  if(state.player.isEngagedInCombat):
    print(f'{player.target.name} blocks your escape!\n')
  else:
    tryMove(player, direction)

def handleLook(gameState: GameState):
  gameState.player.currentLocation.displayDescription(LOCATIONS)

def handleSelectAttack(attackIndex, state: GameState):
  newAttack = state.player.selectAttack(attackIndex)
  print(f'Switching to {newAttack.name} attack.\n')

def handleAttack(state: GameState):
  player = state.player
  if(not player.isEngagedInCombat):
    player.attack()
  else:
    print('Already engaged in combat!\n')

def handleHelp(state: GameState):
  input(HOW_TO_PLAY)
