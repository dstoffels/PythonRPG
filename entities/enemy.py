from entities.entity import Entity
from random import randint

class Enemy(Entity):
  def __init__(self, name='', currentLocation=(0, 0), maxHp=100):
      super().__init__(name=name, currentLocation=currentLocation, maxHp=maxHp)

  def attack(self): 
    self.selectAttack(randint(0,2))
    d20 = randint(1,20)
    match d20:
      case 1:
        print('Attack failed')
      case 20:
        print('Critical Hit!')
      case _:
        print('normal attack') #
    # print('baddie attacks') #FIXME: need list of different attacks, needs variable attack timer that attacks player only when player is in same location