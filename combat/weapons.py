class Weapon:
  def __init__(self, name: str = '', attackPower: int = 0):
      self.name = name
      self.attackPower = attackPower

FISTS = Weapon('Fists', 3)
GLADIUS = Weapon('Gladius', 5)
MJOLNIR = Weapon('Mjolnir', 7)
FALX = Weapon('Falx', 10)