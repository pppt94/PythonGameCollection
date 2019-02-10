from unittest import TestCase
from snake import Score


class TestScore(TestCase):

    def test_get_score_str(self):

        scr = Score()
        self.assertEqual(scr.get_score_str(), "Score: 0")

        scr.result = 2
        self.assertEqual(scr.get_score_str(), "Score: 2")
        self.assertNotEqual(scr.get_score_str(), "Score: 0")

    def test_get_score(self):

        scr = Score()
        self.assertEqual(scr.get_score(), 0)
        scr.result = 2
        self.assertNotEqual(scr.get_score(), 0)

    def test_update_score(self):

        scr = Score()
        self.assertEqual(scr.get_score(), 0)
        scr.update_score()
        self.assertEqual(scr.get_score(), 10)

    def test_update_score_special(self):

        scr = Score()
        self.assertEqual(scr.get_score(), 0)
        scr.update_score_special()
        self.assertNotEqual(scr.get_score(), 10)
        self.assertEqual(scr.get_score(), 20)
