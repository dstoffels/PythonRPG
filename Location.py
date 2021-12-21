class location:
  coordinates = (0,0)
  roomDescription = ''

  def __init__(self, coords, description):
    self.coordinates = coords
    self.roomDescription = description
  
  def getAvailableDirectionsStr(self, locationMap):
    directions = ''

    for coord in locationMap.keys():
      if(coord == (self.coordinates[0] - 1, self.coordinates[1])):
        directions += 'North, '
      if(coord == (self.coordinates[0], self.coordinates[1] + 1)):
        directions += 'East, '
      if(coord == (self.coordinates[0] + 1, self.coordinates[1])):
        directions += 'South, '
      if(coord == (self.coordinates[0], self.coordinates[1] - 1)):
        directions += 'West.'

    return directions

  def displayDescription(self, locationMap):
    return f'{self.roomDescription}\n{self.getAvailableDirectionsStr(locationMap)}'