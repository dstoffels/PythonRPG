def handleQuit(gameState):
  userInput = str.lower(input('Are you sure you want to quit? All progress will be lost. > '))
  if(userInput == 'y' or userInput == 'yes'):
    gameState.isActive = False

def handleMove(direction, state): #FIXME: need a tryMove function to move player to new room or print fail message
  match direction:
    case 'n':
      print('moving north')
    case 's':
      print('moving south')
    case 'e':
      print('moving east')
    case 'w':
      print('moving west')

def TryMove(state):
  pass