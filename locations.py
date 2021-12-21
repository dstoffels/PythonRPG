from Location import Location

#Dict listing all possible locations by coordinate keys to descriptions to programatically produce locations on a 10x10 grid
LOCATIONS = {
  [1,5]: '[The Acropolis: West Wing]\nSconces on the walls dimly illuminate the limestone pillars to the south.',
  [1,6]: '[The Acropolis: Central]\nSconces on the walls dimly illuminate the limestone pillars to the south.',
  [1,7]: '[The Acropolis: East Wing]\nSconces on the walls dimly illuminate the limestone pillars to the south.',
  [2,5]: '[Outside The Acropolis]\nCliffs to the south overlook the vast lands below. Off to the west, the orange glow of campfires can be seen in the distance.',
  [2,6]: '[Outside The Acropolis]\nCliffs to the south overlook the vast lands below.',
  [2,7]: '[Outside The Acropolis]\nCliffs to the south overlook the vast lands below. Clear signs of life can be seen and heard from the southeast',
  [3,2]: "[Baddie's Lair]\n",
  [3,5]: '[The Acropolis: East Wing]\n',
  [3,9]: '[The Acropolis: East Wing]\n',
  [3,10]: '[The Acropolis: East Wing]\n',
  [4,2]: '[The Acropolis: East Wing]\n',
  [4,3]: '[The Acropolis: East Wing]\n',
  [4,4]: '[The Acropolis: East Wing]\n',
  [4,5]: '[The Acropolis: East Wing]\n',
  [4,10]: '[The Acropolis: East Wing]\n',
  [5,5]: '[The Acropolis: East Wing]\n',
  [5,10]: '[The Acropolis: East Wing]\n',
  [6,5]: '[The Acropolis: East Wing]\n',
  [6,7]: '[The Acropolis: East Wing]\n',
  [6,8]: '[The Acropolis: East Wing]\n',
  [6,9]: '[The Acropolis: East Wing]\n',
  [6,10]: '[The Acropolis: East Wing]\n',
  [7,5]: '[The Acropolis: East Wing]\n',
  [7,6]: '[The Acropolis: East Wing]\n',
  [7,7]: '[The Acropolis: East Wing]\n',
  [8,1]: '[The Acropolis: East Wing]\n',
  [8,2]: '[The Acropolis: East Wing]\n',
  [8,4]: '[The Acropolis: East Wing]\n',
  [8,5]: '[The Acropolis: East Wing]\n',
  [8,7]: '[The Acropolis: East Wing]\n',
  [9,2]: '[The Acropolis: East Wing]\n',
  [9,3]: '[The Acropolis: East Wing]\n',
  [9,4]: '[The Acropolis: East Wing]\n',
  [9,7]: '[The Acropolis: East Wing]\n',
  [9,9]: '[The Acropolis: East Wing]\n',
  [9,10]: '[The Acropolis: East Wing]\n',
  [10,7]: '[The Acropolis: East Wing]\n',
  [10,8]: '[The Acropolis: East Wing]\n',
  [10,9]: '[The Acropolis: East Wing]\n'
}
