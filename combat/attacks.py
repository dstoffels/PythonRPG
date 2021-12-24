class Attack:
  def __init__(self, name, attackPowerBonus, cooldown):
      self.name = name
      self.APbonus = attackPowerBonus
      self.cooldown = cooldown

SWING = Attack('Swing', 0, 2)
THRUST = Attack('Thrust', 2, 3)
SMASH = Attack('SMASH!', 7, 7)
ATTACKS = [SWING, THRUST, SMASH]