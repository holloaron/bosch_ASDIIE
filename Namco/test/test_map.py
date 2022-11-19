import unittest
from bosch_ASDIIE_Namco.Namco.solid_version.map import Map


class MyTestCase(unittest.TestCase):
    # Unit testing for the _create_map_borders method
    def test_create_map_borders_whenMapIsGenerated_BorderOfMapIsWall(self):
        env = Map(map_size=10, agent_slot='0', restricted_slot='#',
                  award_slot='×', terminating_slot='X', empty_slot=' ')
        env._generate_map()
        self.assertTrue((env.map[0, :] == env.restricted_slot).all())
        self.assertTrue((env.map[-1, :] == env.restricted_slot).all())
        self.assertTrue((env.map[:, 0] == env.restricted_slot).all())
        self.assertTrue((env.map[:, -1] == env.restricted_slot).all())
        "When the map is generated all bordering tiles should be wall tiles"

    def test_create_map_borders_whenMapIsGenerated_BorderOfMapIsWallWithDifferentMarkings(self):
        env = Map(map_size=10, agent_slot='0', restricted_slot='¤',
                  award_slot='×', terminating_slot='X', empty_slot=' ')
        env._generate_map()
        self.assertTrue((env.map[0, :] == env.restricted_slot).all())
        self.assertTrue((env.map[-1, :] == env.restricted_slot).all())
        self.assertTrue((env.map[:, 0] == env.restricted_slot).all())
        self.assertTrue((env.map[:, -1] == env.restricted_slot).all())
        "When the map is generated all bordering tiles should be wall tiles" \
        "with the given symbol"

    def test_create_map_borders_whenMapIsGenerated_BorderOfMapIsWallWithDifferentMapSize(self):
        env = Map(map_size=15, agent_slot='0', restricted_slot='#',
                  award_slot='×', terminating_slot='X', empty_slot=' ')
        env._generate_map()
        self.assertTrue((env.map[0, :] == env.restricted_slot).all())
        self.assertTrue((env.map[-1, :] == env.restricted_slot).all())
        self.assertTrue((env.map[:, 0] == env.restricted_slot).all())
        self.assertTrue((env.map[:, -1] == env.restricted_slot).all())
        "When the map is generated all bordering tiles should be wall tiles" \
        "independent of the map size"

    # Unit testing for the _create_restricted_areas method
    def test_create_restricted_areas_whenMapIsGenerated_RestrictedAreasCannotBeNextToBorder(self):
        env = Map(map_size=10, agent_slot='0', restricted_slot='#',
                  award_slot='×', terminating_slot='X', empty_slot=' ')
        env._generate_map()
        self.assertFalse((env.map[1, 1:-2] == env.restricted_slot).all())
        self.assertFalse((env.map[-2, 1:-2] == env.restricted_slot).all())
        self.assertFalse((env.map[1:-2, 1] == env.restricted_slot).all())
        self.assertFalse((env.map[1:-2, -2] == env.restricted_slot).all())
        "When the inner walls are generated, no wall tile should be on the" \
        "neighboring position with the outer border"

if __name__ == '__main__':
    unittest.main()
