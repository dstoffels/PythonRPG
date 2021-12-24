import threading
import time
from constants import WIN_GAME_MSG
from entities.entity import Entity
from random import randint
from locations.location import Location
from locations.locations import LOCATIONS

class Enemy(Entity):

  def attack(self): 
    threading.Thread(target= self._engageCombatWrapper).start()

  def _engageCombatWrapper(self):
    time.sleep(1)
    self._engageCombat(self.randomAttack)
  
  def randomAttack(self):
    rand = randint(0,2)
    self.selectAttack(rand)

  def displayCombatResults(self, ap):
      print(f'''
{self.name} hit you for {ap} damage with a {self.activeAttack.name} attack!
Your HP Remaining: {self.target.currentHP}
''', end='')

  def displayFailedAttack(self):
    print(f'\n{self.name} misses you like a storm trooper...')

  def die(self):
    self.upgradePlayerWeapon()
    self.removeEnemyFromMap()
    self.winGameCheck()
    self.target.resetHP()
  
  def upgradePlayerWeapon(self):
    self.target.weapon = self.weapon

  def removeEnemyFromMap(self):
    LOCATIONS[self.currentLocation].enemy = None

  def displayVictoryResults(self):
    print(f'\nYou have defeated {self.name} and aquired a {self.weapon.name}!')
    self.target.currentLocation.displayDescription(LOCATIONS)
  
  def winGameCheck(self):
    if(self.remainingEnemiesCheck()):
      self.displayVictoryResults()
    else:
      print(WIN_GAME_MSG)

  def remainingEnemiesCheck(self):
    for location in LOCATIONS.values():
      location : Location
      if(location.enemy != None):
        return True
    return False
    
