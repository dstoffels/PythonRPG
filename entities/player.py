from entities.entity import Entity
import helpers
from locations.locations import LOCATIONS
import threading

class Player(Entity):
  def attack(self):
    if(self.currentLocation.enemy != None):
      self.target = self.currentLocation.enemy
      print('COMBAT BEGINS!')
      threading.Thread(target=self._engageCombat).start()
      self.target.target = self
      self.target.attack()
    else:
      print('There are no opponents here to attack!\n')

  def displayCombatResults(self, ap):
      print(f'You hit {self.target.name} for {ap} damage!\n')
  
  def die(self):
    self.gameState.endGame()
    print('GAME OVER... You have been defeated! Press return to continue...')

  def move(self, row, col):
    newCoords = helpers.changeCoordinates(row, col, self.currentLocation.coords)
    self.currentLocation = LOCATIONS[newCoords]
    self.currentLocation.displayDescription(LOCATIONS)