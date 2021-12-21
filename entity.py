from abc import ABC

class Entity(ABC):
  name = ''
  currentLocation = (0,0)
  maxHP = 100
  currentHP = 0

  def __init__(self, name, currentLocation):
    self.name = name
    self.currentLocation = currentLocation
    self.currentHP = self.maxHP

class Baddie(Entity):
  def randomAttack():
    return #FIXME: need list of different attacks, needs variable attack timer that attacks player only when player is in same location

class Player(Entity):
  def Attack(attackType):
    return #FIXME: 