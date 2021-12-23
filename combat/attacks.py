class Attack:
  name = ''
  APbonus = 0
  cooldown = 0

  def __init__(self, name, attackPowerBonus, cooldown):
      self.name = name
      self.APbonus = attackPowerBonus
      self.cooldown = cooldown

SWING = Attack('Swing', 0, 2)
THRUST = Attack('Thrust', 2, 3)
SMASH = Attack('SMASH!', 7, 10)
ATTACKS = [SWING, THRUST, SMASH]