from combat.weapons import FALX, GLADIUS, BATTLE_AXE
from entities.enemy import Enemy

BANDIT = Enemy('Smoky the Bandit', (3,2), 70, weapon=GLADIUS)
CERBERUS = Enemy('Cerberus the three-headed dog', (8,10), 75, weapon=BATTLE_AXE)
LERNEAN_HYDRA = Enemy('The Lernaean Hydra', (8,1), 90, weapon=FALX)
NEMEAN_LION = Enemy('The Nemean Lion', (3,9), 100, weapon=FALX)

ENEMIES = [BANDIT, NEMEAN_LION, LERNEAN_HYDRA, CERBERUS]
# ENEMIES = [Enemy('Test', (1,6),1 ) ]