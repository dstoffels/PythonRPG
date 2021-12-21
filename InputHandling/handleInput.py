from InputHandling.commands import COMMANDS

prompt = '> '

def handleUserInput():
  userInput = str.lower(input(prompt))

  try:
    COMMANDS[userInput]()
  except:
    print('unknown command')

