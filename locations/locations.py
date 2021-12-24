from locations.location import Location

LOCATIONS = {
    (1,5): Location((1,5), 'Basilica Ulpia, West Wing', 'Sconces on the walls dimly illuminate the limestone pillars to the south, which lead outside.'),
    (1,6): Location((1,6), 'Basilica Ulpia, Gallery', 'The beige limestone walls are covered in elaborate artwork. A huge stone archway on the south wall leads to the Basilica Courtyard.'),
    (1,7): Location((1,7), 'Basilica Ulpia, East Wing', 'Sconces on the walls dimly illuminate the limestone pillars to the south, which lead outside.'),
    (1,10): Location((1,10), "Merchant's Road, The Iron Gates", "Huge iron gates block the northbound road here. Some signs of activity can be heard on the otherside and a lookout has been posted atop spires on either side of the gates. A sign posted before them reads: 'These gates shall open only for merchant caravans'"),
    (2,5): Location((2,5), 'Outside The Basilica', 'Cliffs to the south overlook the vast lands below. Off to the west, the orange glow of campfires can be seen in the distance and a steep trail leads you south down the escarpment.'),
    (2,6): Location((2,6), 'Basilica, Courtyard', 'A winding path through the Basilica gardens leads northward into the gallery, while cliffs to the south overlook the vast lands below.'),
    (2,7): Location((2,7), 'Outside The Basilica', 'Cliffs to the south overlook the vast lands below. Clear signs of life can be seen and heard from the southeast'),
    (2,10): Location((2,10), "Merchant's Road, Nemean Mountains", "The mountains rise up on either side of the road, where it is unusually flat. The mountainous valley opens to desert toward the south and close in to a massive iron gate far to the north."),
    (3,2): Location((3,2), 'Bandit Camp', 'Tall flames lick the skies all around you. Piles of human remains are randomly scattered between the fires.'),
    (3,5): Location((3,5), 'South Road, Escarpment', 'Atop the escarpment to the north, the Basilica Ulpia can be seen through the trees. A trail winds northward up the switchbacks to the Basilica and continues through the forest to the south.'),
    (3,9): Location((3,9), "Hidden Cave, Lion's Den", "This small cave is no more than a shallow cavity in mountainside. The bones of various creatures are scattered about at your feet. Other adventurer's have met their doom here, as corroded armor encasing long-dead warriors share the boney grounds."),
   (3,10): Location((3,10), "Merchant's Road, Nemean Mountains", "The road veers in close to the eastern side of the mountain range. Most likely an attempt to shield the passerby from at least half a day's desert sun. The mountains seem to spring up awkwardly from the perfectly flat desert around them."),
    (4,2): Location((4,2), 'Bandit Camp, Palisades', 'Fires rage beyond the palisades of the encampment, which are adorned with dozens of severed heads.'),
    (4,3): Location((4,3), 'Western Road, The Barrens', 'Clear signs of recent deforestation surround you. The scent of burnt flesh overwhelms your senses. Flame and smoke rise in the skies to the west and the forest thickens to the east.'),
    (4,4): Location((4,4), 'Western Road', 'There is a noticable silence in the woods as the air is missing the sound of bird, bug and beast.'),
    (4,5): Location((4,5), 'South Road, Clearing', 'The forest gives way to a clearing here, revealing a western fork in the road. Thick smoke can be seen rising to the west.'),
   (4,7): Location((4,7), "Ancient Polis, Ruins", "Inside the walls of this ancient city, only stone foundations poking up through tall grass and vines are all that remains of a once proud polis. Steep hills around the city's periphery provide excellent protection, but not enough to keep it safe from the invaders that evidently won the day sometime long ago."),
   (4,8): Location((4,8), "Old Road, Ancient Orchard", "Rows of unkempt fruit and berry trees stretch across the acres. Interrupted only by empty patches where old trees died or fell over. The equally unkempt path curves south through the orcahrd and west toward rotting wooden stockades against the hillside."),
   (4,10): Location((4,10), "Merchant's Road, Steppes", "The thin golden grass turns to spotty tufts as meadows beome desert. Dryness in the air begins to sap the moisture from your lips. The road continues north and south in a straight line between the Rocky Hills and the Nemean Mountains."),
    (5,5): Location((5,5), 'South Road, Omicron Forest', 'The road winds gently through the woods, over a modest hill. The Basilica Ulpia can be seen atop the escarpment north of here and the sheer cliffs are visible all around it.'),
    (5,8): Location((5,8), "Old Road, The Rocky Hills", "The hills here are smaller and support more plantlife than those to the south. Small boulders are scattered about between small trees and smatterings of patchy, flowery meadows. The ancient trail here is almost complete obscured by overgrowth."),
   (5,10): Location((5,10), "Merchant's Road, Steppes", "The land seems to stretch flat in all directions from here, with the Rocky Hills to the south and Nemean mountains to the north. Aside from the road, there is little of note between here and the distant peaks."),
    (6,5): Location((6,5), 'South Road, Omicron Forest', 'The trees of the forest give way to a sea of saplings toward the south and taller, older trees to the north.'),
    (6,8): Location((6,8), "Merchant's Road, The Rocky Hills", "The weathered trail wraps around the hills through the valley heading south and east. Small rodents dart back and forth between tufts of grass and rocks as you pass. An old overgrown trail branches away from the main road to the north."),
    (6,9): Location((6,9), "Merchant's Road, The Rocky Hills", "Here, the Merchant Road dips down into the lowest point of the valley, along side a shallow stream. River trees and assorted foliage clearly denote the path of the stream in an otherwise unforgiving climate."),
   (6,10): Location((6,10), "Merchant's Road, Steppes", "The Rocky Hills to the south transform into vast, wispy meadows to the north, where the road curves toward. In the distance, barren desert mountains' hazy silhouettes become visible on the northern horizon."),
    (7,2): Location((7,2), 'Cliffs Of Insanity, Top', "The steep climb quickly leads you to the edge of the cliff, where hundreds of feet below, the crashing waves attempt to scale the cliff face, almost as if trying to grab you and pull you down."),
    (7,3): Location((7,3), 'The Lonely Road', "Here the path leads you where the Omicron Forest meets the raging seas. There is a path leading to the cliff's edge, while the road veers off to the south, down to the sea."),
    (7,4): Location((7,4), 'The Lonely Road', 'The road steepens here with a large hill to the east and the rocky seaside off to the west'),
    (7,5): Location((7,5), 'South Road, Crossroads', 'Two roads meet atop a large, meadowed hill. To the north, lies the Omicron forest and escarpment; To the east, the Rocky Hills and the Nemean desert beyond; And to the west, the plains meet the sea cliffs. It would be a beautiful view if not for the skeletons left to rot in hanging cages.'),
    (7,6): Location((7,6), "Merchant's Road", "This well-traveled road descends into a valley between the Rocky Hills off to the east. There is little in the way of vegetation here, providing great visibility into the hills ahead."),
    (7,7): Location((7,7), "Merchant's Road", 'Long shadows blanket the area as the road further descends into the Rocky Hills to the east. A gap between the hills reveals a distant path that carves its way through a narrow canyon.'),
    (7,8): Location((7,8), "Merchant's Road, The Rocky Hills", "Tall barren hills, marred with large protruding boulders, rise up around you in every direction. You stand at the center of a wide valley, where the Merchant's Road winds northward and a crevice between the southern hills provides enough room to pass through."),
    (8,1): Location((8,1), 'The Aegean Sea, Stack', 'The swaying rope bridge creaks with the wind. The exploding waves below leave your skin tacky and mouth salty. Between the wind and the lack of even ground, the risk of falling victim to the sea is ever-present.'),
    (8,3): Location((8,3), 'The Lonely Road, Slope', 'Not so much a road as it is a steep, rocky series of boulders where the slightest misstep would send you head over heels to your death below.'),
    (8,5): Location((8,5), 'South Road, Plains', 'The open plains provide a great vantage to your surroundings. The waves of the sea can be seen crashing against the cliffs to the west and a bustling harbor to the south'),
    (8,8): Location((8,8), "Hades Gulch", "The narrow, rocky crevice winds between tall hills. The wind whistles gently above and the occasional squawks of a raven echo throughout."),
  (8,10): Location((8,10), "Dark Cave, The Red Gate", "The cave walls coalesce to reveal a huge stone gate, with glowing red cracks running along its exterior. Intense heat and a low rumbling emanate from behind the gate and there is a thick sulfuric odor making it hard to get a full breath of air."),
    (9,1): Location((9,1), 'Lernaean Cliffs', 'Here the road ends with sheer cliffs down into the violent waters below. A rope bridge leads to a series of stone columns protruding to the north where a eerie screeching sound can be heard emanating.'),
    (9,2): Location((9,2), 'The Lonely Road, Seaside', 'The sound of the wind and the waves is near deafening, forcing you to labor for your balance as you walk along the uneven and rocky path.'),
    (9,3): Location((9,3), 'The Lonely Road, Seaside', 'A steep slope takes you northward, giving way to a slightly more hospitable road leading west along the rocky shores.'),
    (9,5): Location((9,5), 'Ulpian Harbor', 'The south road concludes at the docks of the harbor. Sailors and merchants scurry back and forth with the loading and unloading of goods from the boats and tavern.'),
    (9,8): Location((9,8), "Hades Gulch, Split", "The narrow crevice opens up here to reveal two paths. The familiar sounds of the sea can be heard in the distance."),
    (9,9): Location((9,9), "Hades Gulch, Dead End", "Here the gulch meets its end to the east, with only a small opening in the rock face that does not appear inviting. Only the echoes of your own movements bouncing off the rocks can be heard, the wind is calm and not a creature in sight."),
   (9,10): Location((9,10), "Dark Cave", "What little light beams through the small mouth of the cave illuminates the room just enough to notice that it continues north between columns and stalagmites. The air is still and dank and the sound of trickling water reverberates from all around you."),
   (10,8): Location((10,8), "Hidden Beach", "The path widens and opens up to a long, golden beach. Waves gently oscillate upon the shoreline and merchant ships pepper the horizon in the warm sunlight."),
}