from constants import MAIN_MENU_ERR_MSG
from locations.locations import LOCATIONS

def aOrAn(word):
  VOWELS = ['a','e','i','o','u']

  for vowel in VOWELS:
    if(word[0] == vowel):
      return 'an'
  return 'a'

def validateYesOrNoInput(prompt):
  ACCEPTABLE_INPUTS = ['y', 'yes', 'n', 'no']
  userInput = str.lower(input(prompt)) 

  while True:
    for acceptableInput in ACCEPTABLE_INPUTS:
      if(userInput == acceptableInput):
        return userInput 
    userInput = str.lower(input("Please enter 'y' or 'n'."))

def validateIntInput(prompt):
  while True:
    try:
      response = int(input(prompt))
      return response
    except:
      prompt = MAIN_MENU_ERR_MSG

def changeCoordinates(row, col, coords):
  row = coords[0] + row
  col = coords[1] + col
  return (row, col)

def tryMove(player, direction):
  paths = player.currentLocation.getPossibleDirections(LOCATIONS)
  if(paths.__contains__(direction)):
    match direction:
      case 'North': player.move(-1, 0)
      case 'South': player.move(1, 0)
      case 'East': player.move(0, 1)
      case 'West': player.move(0, -1)
  else:
    print('You cannot go that direction.\n')

