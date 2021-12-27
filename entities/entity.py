from abc import ABC, abstractmethod
from random import randint
import time

from combat.attacks import ATTACKS, SWING, Attack
from combat.weapons import FISTS, Weapon
from locations.location import Location

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

  @abstractmethod
  def displayFailedAttack():
    pass

  def getAttackPower(self):
    return self.weapon.attackPower + self.activeAttack.APbonus

  def _engageCombat(self, attackSelector = lambda : 0):
    self.startCombat()

    while self.target.isAlive and self.isAlive and self.gameState.isActive:
      attackSelector()
      self.critFailCheck(self.damageTargetAndDisplay)
      time.sleep(self.activeAttack.cooldown)
    
    self.endCombat()

  def startCombat(self):
    self.isEngagedInCombat = True

  def critFailCheck(self, damageTarget):
    d20 = randint(1, 20)
    if(d20 == 1):
      self.displayFailedAttack()
    elif (d20 == 20):
      self.displayCriticalHit()
      damageTarget(10)
    else:
      damageTarget()

  def damageTargetAndDisplay(self, critBonus = 0):
    ap = self.getAttackPower() + critBonus
    self.target.takeDamage(ap)
    self.displayCombatResults(ap)

  def endCombat(self):
    self.isEngagedInCombat = self.target.isEngagedInCombat = False
    if(not self.isAlive):
      self.die()

  def selectAttack(self, index) -> Attack:
    self.activeAttack = ATTACKS[index]
    return self.activeAttack

  def takeDamage(self, amt):
    self.currentHP -= amt
    if(self.currentHP < 1):
      self.isAlive = False

  def resetHP(self):
    self.currentHP = self.maxHP
    self.isAlive = True

  def displayCriticalHit(self):
    print('\nCRITICAL HIT!\r')

  def upgradeWeapon(self, weapon: Weapon):
    self.weapon = weapon if weapon.attackPower > self.weapon.attackPower else self.weapon