from types import CellType
from entities.enemies import ENEMIES
from entities.player import Player
from locations.locations import LOCATIONS

STARTING_LOCATION = (1,6)

class GameState:
  def __init__(self):
    self.isActive = True
    self.player = Player('Hercules', LOCATIONS[STARTING_LOCATION])
    self.placeEnemiesOnMap()

  def placeEnemiesOnMap(self):
    for enemy in ENEMIES:
      LOCATIONS[enemy.currentLocation].placeEnemy(enemy)

  def commandPrompt(self):
    health = self.player.currentHP
    weapon = self.player.weapon.name
    attack = self.player.activeAttack.name
    attackPower = self.player.weapon.attackPower + self.player.activeAttack.APbonus
    return f'[HP: {health} | WEP: {weapon} | ATT: {attack} | AP: {attackPower}] > '
