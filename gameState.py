from entities.enemy import Enemy
from entities.player import Player
from locations.locations import LOCATIONS

BANDIT = Enemy('Bandit', (3,2))
NEMEAN_LION = Enemy('Nemean Lion', (4,9))
LERNEAN_HYDRA = Enemy('Lernaean Hydra', (8,1))
CERBERUS = Enemy('Cerberus', (8,10))
STARTING_ENEMIES = []
STARTING_LOCATION = (1,6)

class GameState:
  isActive = False
  player = Player('Hercules', LOCATIONS[STARTING_LOCATION])

  def commandPrompt(self):
    health = self.player.currentHP
    weapon = self.player.weapon.name
    attack = self.player.activeAttack.name
    attackPower = self.player.weapon.attackPower + self.player.activeAttack.APbonus
    return f'[HP: {health} | WEP: {weapon} | ATT: {attack} | AP: {attackPower}] > '

  def __init__(self):
    self.isActive = True