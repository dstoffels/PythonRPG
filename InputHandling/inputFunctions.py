def handleQuit():
  userInput = str.lower(input('Are you sure you want to quit? All progress will be lost.\n> '))
  if(userInput == 'y' or userInput == 'yes'):
    exit()