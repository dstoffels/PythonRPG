from random import randint
import time
from combat.weapons import Weapon
from constants import TAUNTS
from entities.entity import Entity
import helpers
from locations.locations import LOCATIONS
import threading

class Player(Entity):
  def attack(self):
    if(self.isEnemyHere()):
      self.target = self.currentLocation.enemy
      print('COMBAT BEGINS!')
      threading.Thread(target=self._engageCombat).start()
      self.enemyEngagesPlayer()
    else:
      print('There are no opponents here to attack!\n')

  def displayCombatResults(self, ap):
      print(f'''
You hit {self.target.name} for {ap} damage with a {self.activeAttack.name} attack!
[Opponent HP: {self.target.currentHP} | Cooldown Time: {self.activeAttack.cooldown}] sec''')

  def displayFailedAttack(self):
    print('\nYour attack fails...')
  
  def die(self):
    print('\nYou have been defeated! Press return to continue...')
    self.gameState.endGame()
    self.target.resetHP()

  

  def enemyEngagesPlayer(self):
    self.target.target = self
    self.target.attack()

  def move(self, row, col):
    newCoords = helpers.changeCoordinates(row, col, self.currentLocation.coords)
    self.currentLocation = LOCATIONS[newCoords]
    self.currentLocation.displayDescription(LOCATIONS)
    threading.Thread(target=self.triggerTaunts).start()
  
  def triggerTaunts(self):
    if self.isEnemyHere():
      while self.isEnemyHere() and self.gameState.isActive:
        rand = randint(0, len(TAUNTS) - 1)
        print(f'\n{self.currentLocation.enemy.name} shouts, "{TAUNTS[rand]}"')
        time.sleep(5)

  def isEnemyHere(self):
    return self.currentLocation.enemy != None