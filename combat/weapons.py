class Weapon:
  def __init__(self, name: str = '', attackPower: int = 0):
      self.name = name
      self.attackPower = attackPower

FISTS = Weapon('Fists', 3)
GLADIUS = Weapon('Gladius', 5)
BATTLE_AXE = Weapon('Battle Axe', 7)
FALX = Weapon('Falx', 10)