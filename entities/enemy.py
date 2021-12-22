from entities.entity import Entity

class Enemy(Entity):
  def __init__(self, name='', currentLocation=(0, 0), maxHp=100):
      super().__init__(name=name, currentLocation=currentLocation, maxHp=maxHp)

  def attack(self): 
    print('baddie attacks') #FIXME: need list of different attacks, needs variable attack timer that attacks player only when player is in same location