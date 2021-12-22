from entity import Player
from locations.locations import LOCATIONS

STARTING_LOCATION = (1,6)

class GameState:
  isActive = False
  player = Player('Hercules', LOCATIONS[STARTING_LOCATION])

  def __init__(self):
    self.isActive = True