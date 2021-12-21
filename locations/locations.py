from typing import Dict
from locations.Location import location

# FIXME: update to a list of locations with coords, title, description OR a dict with coords as key?
COORDS = [
    (1,5),
    (1,6),
    (1,7),
    (2,5),
    (2,6),
    (2,7),
    (3,2),
    (3,5),
    (3,9),
    (3,10),
    (4,2),
    (4,3),
    (4,4),
    (4,5),
    (4,10),
    (5,5),
    (5,10),
    (6,5),
    (6,7),
    (6,8),
    (6,9),
    (6,10),
    (7,5),
    (7,6),
    (7,7),
    (8,1),
    (8,2),
    (8,4),
    (8,5),
    (8,7),
    (9,2),
    (9,3),
    (9,4),
    (9,7),
    (9,9),
    (9,10),
    (10,7),
    (10,8),
    (10,9)
  ]

ROOM_DESCRIPTIONS = [
  '[Basilica Ulpia: West Wing]\nSconces on the walls dimly illuminate the limestone pillars to the south, which lead outside.',
  '[Basilica Ulpia: Gallery]\nThe beige limestone walls are covered in elaborate artwork. A huge stone archway on the south wall leads to the Basilica Courtyard.',
  '[Basilica Ulpia: East Wing]\nSconces on the walls dimly illuminate the limestone pillars to the south, which lead outside.',
  '[Outside The Basilica]\nCliffs to the south overlook the vast lands below. Off to the west, the orange glow of campfires can be seen in the distance.',
  '[Basilica, Courtyard]\nA winding path through the Basilica gardens leads northward to the gallery, while cliffs to the south overlook the vast lands below.',
  '[Outside The Basilica]\nCliffs to the south overlook the vast lands below. Clear signs of life can be seen and heard from the southeast',
  "[Baddie's Lair]\n",
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n',
  '[The Acropolis: East Wing]\n'
]

#returns a dict listing all possible locations by coordinate keys to descriptions to programatically produce locations on a 10x10 grid
def getLocations():
  locations = {}
  i = 0

  for coord in COORDS:
    # locations.update({coord: location(coord, ROOM_DESCRIPTIONS[i])})
    locations[coord] = location(coord, ROOM_DESCRIPTIONS[i])
    i += 1
  return locations