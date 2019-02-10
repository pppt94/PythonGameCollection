from unittest import TestCase
from snake import Game

class TestGame(TestCase):

    def test_start_game(self):

        game = Game()
        game.state = 2
        self.assertEqual(game.start_game(), None)


    def test_game_pause(self):

        game = Game()
        self.assertEqual(game.pause, 0)

