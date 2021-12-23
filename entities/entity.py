from abc import ABC, abstractmethod
from combat.attacks import ATTACKS, SWING, Attack
from combat.weapons import FISTS
from locations.location import Location

class Entity(ABC):
  def __init__(self, name='', currentLocation=Location(), maxHp = 100, activeAttack = SWING, weapon = FISTS):
    self.name = name
    self.currentLocation = currentLocation
    self.maxHP = maxHp
    self.resetHP()
    self.activeAttack = activeAttack
    self.weapon = weapon
  
  @abstractmethod
  def attack(self):
    pass

  def selectAttack(self, index) -> Attack:
    self.activeAttack = ATTACKS[index]
    return self.activeAttack

  def takeDamage(self, amt):
    self.currentHP -= amt

  def resetHP(self):
    self.currentHP = self.maxHP