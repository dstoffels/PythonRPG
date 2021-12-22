from entities.entity import Entity
from locations.locations import LOCATIONS

class Player(Entity):
  def attack(self, attackType=''):
    print('player attacks')

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