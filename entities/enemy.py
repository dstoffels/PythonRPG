import threading
import time
from constants import WIN_GAME_MSG
from entities.entity import Entity
from random import randint
from locations.location import Location
from locations.locations import LOCATIONS

TAUNT1 = 'I shall feast upon your bones, Hercules!'
TAUNT2 = 'Your death awaits...'
TAUNT3 = 'Hades is calling, demigod!'
TAUNT4 = 'Your father cannot save you now!'
TAUNT5 = 'Xena was better!'

TAUNTS = [TAUNT1, TAUNT2, TAUNT3, TAUNT4, TAUNT5]

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
      print(f'''{self.name} hit you for {ap} damage with a {self.activeAttack.name} attack!
Your HP Remaining: {self.target.currentHP}
''')

  def displayFailedAttack(self):
    print(f'{self.name} misses you like a storm trooper...')

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
    print(f'You have defeated {self.name} and aquired a {self.weapon.name}!')
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
    
