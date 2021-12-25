from entities.enemies import ENEMIES
from entities.player import Player
from locations.locations import LOCATIONS

STARTING_LOCATION = (1,6)

class GameState:
  def __init__(self):
    self.isActive = True
    self.player = Player('Hercules', LOCATIONS[STARTING_LOCATION], gameState=self)
    self.spawnEnemies()

  def spawnEnemies(self):
    for enemy in ENEMIES:
      LOCATIONS[enemy.currentLocation].placeEnemy(enemy)
      enemy.gameState = self
      enemy.resetHP()

  def commandPrompt(self):
    health = self.player.currentHP
    weapon = self.player.weapon
    attack = self.player.activeAttack
    attackPower = self.player.weapon.attackPower + self.player.activeAttack.APbonus
    return f'STATUS: [HP: {health} | Weapon: {weapon.name} (AP: {weapon.attackPower}) | Attack: {attack.name} (AP: {attack.APbonus} - Cooldown: {attack.cooldown}) | Attack Power: {attackPower}]\n> '

  def endGame(self):
    self.isActive = False