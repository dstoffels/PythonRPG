from entities.entity import Entity
from locations.locations import LOCATIONS
import threading

class Player(Entity):
  def attack(self):
    if(self.currentLocation.enemy != None):
      self.target = self.currentLocation.enemy
      print('COMBAT BEGINS!')
      threading.Thread(target=self._engageCombat).start()
      self.target.target = self
      self.target.attack()
    else:
      print('There are no opponents here to attack!\n')

  def displayCombatResults(self, ap):
      print(f'You hit {self.target.name} for {ap} damage!\n')
  
  def die(self):
    self.gameState.endGame()
    print('GAME OVER... You have been defeated! Press return to continue...')

  def moveNorth(self):
    newCoords =  self.changeCoordinates(-1)
    self.currentLocation = LOCATIONS[newCoords]
    self.currentLocation.displayDescription(LOCATIONS)

  def moveSouth(self):
    newCoords =  self.changeCoordinates(1)
    self.currentLocation = LOCATIONS[newCoords]
    self.currentLocation.displayDescription(LOCATIONS)

  def moveEast(self):
    newCoords =  self.changeCoordinates(0, 1)
    self.currentLocation = LOCATIONS[newCoords]
    self.currentLocation.displayDescription(LOCATIONS)
    1
  def moveWest(self):
    newCoords =  self.changeCoordinates(0, -1)
    self.currentLocation = LOCATIONS[newCoords]
    self.currentLocation.displayDescription(LOCATIONS)

  def changeCoordinates(self, row=0, col=0):
    coords = self.currentLocation.coords
    row = coords[0] + row
    col = coords[1] + col
    return (row, col)