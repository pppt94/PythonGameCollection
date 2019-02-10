from unittest import TestCase
from Source.pytris import Block, shapes
import pygame

pygame.init()


class TestBlock(TestCase):


    def test_convert_shape(self):

        piece = Block(0, 0)
        piece.shape = shapes[0]
        self.assertEqual(piece.convert_shape(), [(0, -4), (0, -3), (0, -2), (0, -1)])
        piece.shape = shapes[1]
        self.assertEqual(piece.convert_shape(), [(-1, -2), (0, -2), (-1, -1), (0, -1)])
        piece.shape = shapes[2]
        self.assertEqual(piece.convert_shape(), [(0, -2), (1, -2), (-1, -1), (0, -1)])

        piece.x = 5
        piece.y = 5
        piece.shape = shapes[3]
        self.assertEqual(piece.convert_shape(), [(4, 3), (5, 3), (5, 4), (6, 4)])
        piece.shape = shapes[4]
        self.assertEqual(piece.convert_shape(), [(5, 2), (4, 3), (5, 3), (6, 3)])
        piece.shape = shapes[5]
        self.assertEqual(piece.convert_shape(), [(5, 2), (5, 3), (4, 4), (5, 4)])
        self.assertNotEqual(piece.convert_shape(), [(5, 2), (5, 5), (5, 5), (5, 5)])