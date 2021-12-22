import InputHandling.inputFunctions as execute
from constants import N, S, E, W

# a dictionary of user commands as keys for the functions they execute, all functions must take a GameState object as an argument
COMMANDS = {
  'q': execute.handleQuit,
  'quit': execute.handleQuit,
  'exit': execute.handleQuit,
  'n': lambda state : execute.handleMove(N, state),
  'north': lambda state : execute.handleMove(N, state),
  's': lambda state : execute.handleMove(S, state),
  'south': lambda state : execute.handleMove(S, state),
  'e': lambda state : execute.handleMove(E, state),
  'east': lambda state : execute.handleMove(E, state),
  'w': lambda state : execute.handleMove(W, state),
  'west': lambda state : execute.handleMove(W, state),
}

