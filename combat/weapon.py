class Weapon:
  name = ''
  attackPower = 0
  
  def __init__(self, name: str = '', attackPower: int = 0):
      self.name = name
      self.attackPower = attackPower