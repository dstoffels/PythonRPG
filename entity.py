from abc import ABC, abstractmethod
from locations.location import location
from locations.locations import LOCATIONS

class Entity(ABC):
  name = ''
  currentLocation: location = None
  maxHP = 0
  currentHP = 0

  def __init__(self, name='', currentLocation: location = location(), maxHp = 100):
    self.name = name
    self.currentLocation = currentLocation
    self.maxHP = maxHp
    self.currentHP = self.maxHP
  
  @abstractmethod
  def attack(self):
    pass

class Baddie(Entity):
  def __init__(self, name='', currentLocation=(0, 0), maxHp=100):
      super().__init__(name=name, currentLocation=currentLocation, maxHp=maxHp)

  def attack(self): 
    print('baddie attacks') #FIXME: need list of different attacks, needs variable attack timer that attacks player only when player is in same location

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


