from combat.weapons import FALX, GLADIUS, BATTLE_AXE
from entities.enemy import Enemy

BANDIT = Enemy('Bandit', (3,2), 30, weapon=GLADIUS)
CERBERUS = Enemy('Cerberus', (8,10), 40, weapon=BATTLE_AXE)
LERNEAN_HYDRA = Enemy('Lernaean Hydra', (8,1), 70, weapon=FALX)
NEMEAN_LION = Enemy('Nemean Lion', (3,9), 100, weapon=FALX)

ENEMIES = [BANDIT, NEMEAN_LION, LERNEAN_HYDRA, CERBERUS]
