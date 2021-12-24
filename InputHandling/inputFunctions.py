from gameState import GameState
from locations.locations import LOCATIONS

def handleQuit(gameState: GameState):
  userInput = str.lower(input('Are you sure you want to quit? All progress will be lost. > '))
  if(userInput == 'y' or userInput == 'yes'):
    gameState.endGame()

def handleMove(direction, state: GameState):
  player = state.player
  paths = player.currentLocation.getPossibleDirections(LOCATIONS)

  if(paths.__contains__(direction)):
    match direction:
      case 'North': player.move(-1, 0)
      case 'South': player.move(1, 0)
      case 'East': player.move(0, 1)
      case 'West': player.move(0, -1)
  else:
    print('You cannot go that direction.\n')

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