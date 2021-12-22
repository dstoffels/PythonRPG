from abc import ABC, abstractmethod
from locations.location import location

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

