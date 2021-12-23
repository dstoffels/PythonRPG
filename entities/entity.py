from abc import ABC, abstractmethod
from combat.attacks import ATTACKS, SWING, Attack
from combat.weapons import FISTS
from locations.location import location

class Entity(ABC):
  name = ''
  currentLocation: location = None
  maxHP = 0
  currentHP = 0
  activeAttack = SWING
  weapon = FISTS

  def __init__(self, name='', currentLocation: location = location(), maxHp = 100):
    self.name = name
    self.currentLocation = currentLocation
    self.maxHP = maxHp
    self.currentHP = self.maxHP
  
  @abstractmethod
  def attack(self):
    pass

  def selectAttack(self, index) -> Attack:
    self.activeAttack = ATTACKS[index]
    return self.activeAttack

  def takeDamage(self, amt):
    self.currentHP -= amt

