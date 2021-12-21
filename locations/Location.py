class location: #FIXME: change ctor to accept self, coords, title, description. Add currentEntities(). must also change locations list & getAvailableDirectionsStr
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
        directions += 'West, '

    return directions

  def displayDescription(self, locationMap):
    return f'\n{self.roomDescription}\nObvious paths: {self.getAvailableDirectionsStr(locationMap)}\n'