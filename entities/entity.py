from abc import ABC, abstractmethod
from random import randint
from combat.attacks import ATTACKS, SWING, Attack
from combat.weapons import FISTS, Weapon
from locations.location import Location
import time

class Entity(ABC):
  def __init__(self, name='', currentLocation = Location(), maxHp = 100, activeAttack = SWING, weapon = FISTS, gameState = None):
    self.name = name
    self.currentLocation: Location = currentLocation
    self.maxHP: int = maxHp
    self.resetHP()
    self.activeAttack: Attack = activeAttack
    self.weapon: Weapon = weapon
    self.target: Entity = None
    self.isAlive = True
    self.isEngagedInCombat = False
    self.gameState = gameState

  @abstractmethod
  def attack(self):
    pass

  @abstractmethod
  def displayCombatResults(self, ap):
    pass

  @abstractmethod
  def die(self):
    pass

  def getAttackPower(self):
    return self.weapon.attackPower + self.activeAttack.APbonus

  def _engageCombat(self):
    self.isEngagedInCombat = True

    while self.target.isAlive and self.isAlive:
      ap = self.getAttackPower()
      self.target.takeDamage(ap)
      self.displayCombatResults(ap)
      time.sleep(self.activeAttack.cooldown)
    
    self.endCombat()


  def selectAttack(self, index) -> Attack:
    self.activeAttack = ATTACKS[index]
    return self.activeAttack

  def takeDamage(self, amt):
    self.currentHP -= amt
    if(self.currentHP < 1):
      self.isAlive = False

  def resetHP(self):
    self.currentHP = self.maxHP

  def endCombat(self):
    self.isEngagedInCombat = False
    if(not self.isAlive):
      self.die()
