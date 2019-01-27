from unittest import TestCase
from pytris import Board, Block


class TestBoard(TestCase):

    def test_create_grid(self):

        board = Board()
        self.assertEqual(board.create_grid(), [[(0, 0, 0) for row in range(10)] for column in range(20)])
        board.blocks_positions = {(0, 17): (150, 75, 0)}
        self.assertNotEqual(board.create_grid(), [[(0, 0, 0) for row in range(10)] for column in range(20)])

    def test_check_space(self):

        board = Board()
        block = Block(5, 5)
        board.create_grid()
        self.assertTrue(board.check_space(block))
        board.grid = [[(1, 1, 1) for row in range(10)] for column in range(20)]
        self.assertFalse(board.check_space(block))

    def test_check_full(self):

        board = Board()
        board.blocks_positions = {(0, 5): (100, 100, 0)}
        self.assertFalse(board.check_full())
        board.blocks_positions = {(5, 0): (100, 100, 0)}
        self.assertTrue(board.check_full())

    def test_check_row(self):

        board = Board()
        board.create_grid()
        board.grid[0] = [(1, 1, 1) for row in range(10)]
        self.assertEqual(board.check_row(), 10)
        board.grid[1] = [(1, 1, 1) for row in range(10)]
        self.assertEqual(board.check_row(), 20)
