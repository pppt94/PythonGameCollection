from unittest import TestCase
from Source.python_mind import Types

class TestTypes(TestCase):

    def test_fill_arrays(self):

        types = Types()
        types.fill_arrays()

        self.assertEqual(len(types.game_array), 4)

    def test_compare_array(self):

        types = Types()
        types.compare_array()

        self.assertEqual(types.player_array, [0, 0, 0, 0])
        self.assertEqual(len(types.result_array), 4)



