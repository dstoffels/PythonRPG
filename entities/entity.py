from abc import ABC, abstractmethod
from combat.attacks import ATTACKS, SWING, Attack
from combat.weapons import FISTS, Weapon
from locations.location import Location

class Entity(ABC):
  def __init__(self, name='', currentLocation = Location(), maxHp = 100, activeAttack = SWING, weapon = FISTS):
    self.name = name
    self.currentLocation: Location = currentLocation
    self.maxHP: int = maxHp
    self.resetHP()
    self.activeAttack: Attack = activeAttack
    self.weapon: Weapon = weapon
  
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