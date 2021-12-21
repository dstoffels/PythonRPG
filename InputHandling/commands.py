import InputHandling.inputFunctions as execute

# a dictionary of user commands as keys for the functions they execute, all functions must take a GameState object as an argument
COMMANDS = {
  'q': execute.handleQuit,
  'quit': execute.handleQuit,
  'exit': execute.handleQuit,
  'n': lambda state : execute.handleMove('n', state),
  'north': lambda state : execute.handleMove('n', state),
  's': lambda state : execute.handleMove('s', state),
  'south': lambda state : execute.handleMove('s', state),
  'e': lambda state : execute.handleMove('e', state),
  'east': lambda state : execute.handleMove('e', state),
  'w': lambda state : execute.handleMove('w', state),
  'west': lambda state : execute.handleMove('w', state),
}

