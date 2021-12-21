class Entity:
  currentLocation = (0,0)
  maxHP = 100
  currentHP = 0

  def __init__(self, currentLocation):
      self.currentLocation = currentLocation
      self.currentHP = self.maxHP

class Baddie(Entity):
  

class Player(Entity):
  pass