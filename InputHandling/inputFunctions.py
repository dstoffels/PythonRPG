from gameState import GameState
from locations.locations import LOCATIONS

def handleQuit(gameState):
  userInput = str.lower(input('Are you sure you want to quit? All progress will be lost. > '))
  if(userInput == 'y' or userInput == 'yes'):
    gameState.isActive = False

def handleMove(direction, state: GameState):
  player = state.player
  paths = player.currentLocation.getPossibleDirections(LOCATIONS)

  if(paths.__contains__(direction)):
    match direction:
      case 'North':
        player.moveNorth()
      case 'South':
        player.moveSouth()
      case 'East':
        player.moveEast()
      case 'West':
        player.moveWest()
  else:
    print('You cannot go that direction')