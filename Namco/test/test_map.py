import unittest
from bosch_ASDIIE_Namco.Namco.map import Map


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


if __name__ == '__main__':
    unittest.main()
