from entities.entity import Entity
import helpers
from locations.locations import LOCATIONS
import threading

class Player(Entity):
  def attack(self):
    if(self.currentLocation.enemy != None):
      self.target = self.currentLocation.enemy
      threading.Thread(target=self._engageCombat).start()
      self.enemyEngagesPlayer()
    else:
      print('There are no opponents here to attack!\n')

  def displayCombatResults(self, ap):
      print(f'You hit {self.target.name} for {ap} damage!')

  def displayFailedAttack(self):
    print('Your attack fails...')
  
  def die(self):
    self.gameState.endGame()
    print('GAME OVER... You have been defeated! Press return to continue...')

  def move(self, row, col):
    newCoords = helpers.changeCoordinates(row, col, self.currentLocation.coords)
    self.currentLocation = LOCATIONS[newCoords]
    self.currentLocation.displayDescription(LOCATIONS)

  def enemyEngagesPlayer(self):
    self.target.target = self
    self.target.attack()