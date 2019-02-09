from unittest import TestCase
from snake import Snake


class TestSnake(TestCase):

    def test_update_position(self):

        snake = Snake()
        snake.update_position(10, 10, "UP")

        self.assertEqual(snake.head_x, 450)
        self.assertEqual(snake.head_y, 370)
        self.assertEqual(snake.head_direction, "UP")

        snake.update_position(-10, -10, "DOWN")

        self.assertNotEqual(snake.head_direction, "UP")
        self.assertNotEqual(snake.head_x, 450)
        self.assertNotEqual(snake.head_y, 370)

    def test_eating_food(self):

        snake = Snake()
        self.assertEqual(snake.snake_length, 1)

        snake.head_x = 10
        snake.head_y = 10
        snake.eating_food(10, 10, 0, 0)
        self.assertEqual(snake.snake_length, 2)

        snake.eating_food(5, 15, 10, 10)
        self.assertEqual(snake.snake_length, 3)

        snake.eating_food(5, 15, 10, 15)
        self.assertNotEqual(snake.snake_length, 4)

    def test_check_colision(self):

        snake = Snake()

        snake.head_x, snake.head_y = 100, 100
        snake.snake_body = [(1, 1), (5, 5), (100, 100)]
        self.assertFalse(snake.check_collision())

        snake.snake_body = [(100, 100), (1, 1), (5, 5), (100, 100)]
        self.assertTrue(snake.check_collision())