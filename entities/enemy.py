import threading
import time
import threading
from entities.entity import Entity
from random import randint

from locations.location import Location
from locations.locations import LOCATIONS
# from locations.locations import LOCATIONS


class Enemy(Entity):
  def attack(self): 
    time.sleep(2)
    self.selectAttack(randint(0,2))
    threading.Thread(target=self._engageCombat).start()

  def displayCombatResults(self, ap):
      print(f'''{self.name} hit you for {ap} damage with a {self.activeAttack.name} attack!
Your HP Remaining: {self.target.currentHP}
''')

  def die(self):
    self.upgradePlayerWeapon()
    self.removeEnemyFromMap()
    self.displayVictoryResults()
  
  def upgradePlayerWeapon(self):
    self.target.weapon = self.weapon

  def removeEnemyFromMap(self):
    LOCATIONS[self.currentLocation].enemy = None

  def displayVictoryResults(self):
    print(f'You have defeated {self.name} and aquired a {self.weapon.name}!')
    self.target.currentLocation.displayDescription(LOCATIONS)