class Weapon:
  name = ''
  attackPower = 0
  
  def __init__(self, name: str = '', attackPower: int = 0):
      self.name = name
      self.attackPower = attackPower

FISTS = Weapon('Fists', 3)
GLADIUS = Weapon('Gladius', 5)
FALX = Weapon('Falx', 10)