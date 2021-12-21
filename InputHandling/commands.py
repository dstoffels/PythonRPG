from helpers import validateYesOrNoInput
import InputHandling.inputFunctions as execute

# a dictionary of user commands as keys for the functions they execute
COMMANDS = {
  'q': execute.handleQuit,
  'quit': execute.handleQuit,
  'exit': execute.handleQuit,
}

