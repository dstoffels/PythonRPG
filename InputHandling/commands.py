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
  'l': execute.handleLook,
  'look': execute.handleLook,
  '1': lambda state : execute.handleSelectAttack(0, state),
  'swing': lambda state : execute.handleSelectAttack(0, state),
  '2': lambda state : execute.handleSelectAttack(1, state),
  'thrust': lambda state : execute.handleSelectAttack(1, state),
  '3': lambda state : execute.handleSelectAttack(2, state),
  'smash': lambda state : execute.handleSelectAttack(2, state),
}

