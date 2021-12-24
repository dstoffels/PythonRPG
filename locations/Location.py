from constants import N, S, E, W

class Location:
  def __init__(self, coords = (0,0), title = '[Title]', description = 'Description'):
    self.coords = coords
    self.title = title
    self.roomDescription = description
    self.enemy = None

  def placeEnemy(self, enemy):
    self.enemy = enemy
  
  def getPossibleDirections(self, locations):
    possibleDirections = []

    for coord in locations.keys():
      if(coord == (self.coords[0] - 1, self.coords[1])):
        possibleDirections.append(N)
      if(coord == (self.coords[0] + 1, self.coords[1])):
        possibleDirections.append(S)
      if(coord == (self.coords[0], self.coords[1] + 1)):
        possibleDirections.append(E)
      if(coord == (self.coords[0], self.coords[1] - 1)):
        possibleDirections.append(W)

    return possibleDirections

  def obviousPathsStringBuilder(self, locations):
    outputStr = ''
    possibleDirections = self.getPossibleDirections(locations)

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
    
    return f'Obvious paths: {outputStr}'

  def presentEnemyStrBldr(self):
    if(self.enemy != None):
      return f'You also see: {self.enemy.name}\n'
    else:
      return ''
  
  def buildDescriptionStr(self, locations):
    return f'''
{self.title}
{self.roomDescription}
{self.obviousPathsStringBuilder(locations)}
{self.presentEnemyStrBldr()}'''

  def displayDescription(self, locations):
    description = self.buildDescriptionStr(locations)
    print(description)