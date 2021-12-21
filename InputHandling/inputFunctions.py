def handleQuit(gameState):
  userInput = str.lower(input('Are you sure you want to quit? All progress will be lost.\n> '))
  if(userInput == 'y' or userInput == 'yes'):
    gameState.isActive = False