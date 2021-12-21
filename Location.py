from locations import LOCATIONS

class Location:
  coordinates = [0, 0]
  roomDescription = ''

  def __init__(self, coords, description):
    self.coordinates = coords
    self.roomDescription = description
  
  def getAvailableDirectionsStr(self):
    directions = ''

    for coord in LOCATIONS.keys():
      if(coord[0] == self.coordinates[0] - 1):
        directions += 'North, '
      if(coord[1] == self.coordinates[1] + 1):
        directions += 'East, '
      if(coord[0] == self.coordinates[0] + 1):
        directions += 'South, '
      if(coord[1] == self.coordinates[1] - 1):
        directions += 'West.'

    return directions

  def displayDescription(self):
    return f'{self.roomDescription}\n{self.getAvailableDirectionsStr()}' 

