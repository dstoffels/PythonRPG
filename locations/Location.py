N = 'North'
S = 'South'
E = 'East'
W = 'West'

class location: #FIXME: change ctor to accept self, coords, title, description. Add currentEntities(). must also change locations list & getAvailableDirectionsStr
  coordinates = (0,0)
  title = ''
  roomDescription = ''

  def __init__(self, coords, title = '[Title]', description = 'Description'):
    self.coordinates = coords
    self.title = title
    self.roomDescription = description
  
  def getPossibleDirections(self, locationMap):
    possibleDirections = []

    for coord in locationMap.keys():
      if(coord == (self.coordinates[0] - 1, self.coordinates[1])):
        possibleDirections.append(N)
      if(coord == (self.coordinates[0] + 1, self.coordinates[1])):
        possibleDirections.append(S)
      if(coord == (self.coordinates[0], self.coordinates[1] + 1)):
        possibleDirections.append(E)
      if(coord == (self.coordinates[0], self.coordinates[1] - 1)):
        possibleDirections.append(W)

    return possibleDirections

  def obviousPathsStringBuilder(self, locationMap):
    outputStr = ''
    possibleDirections = self.getPossibleDirections(locationMap)

    def strHelper(dir, outputStr):
      if(possibleDirections.__contains__(dir)):
        if(outputStr == ''):
          return dir
        else:
          return f', {dir}'
      else: 
        return ''
      
    outputStr += strHelper(N, outputStr)
    outputStr += strHelper(S, outputStr)
    outputStr += strHelper(E, outputStr)
    outputStr += strHelper(W, outputStr)
    
    return outputStr
  
  def displayDescription(self, locationMap):
    return f'''
    {self.title}
    {self.roomDescription}
    {self.obviousPathsStringBuilder(locationMap)}
    '''