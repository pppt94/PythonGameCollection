from unittest import TestCase
from Source.snake import Food, Snake, foods

class TestFood(TestCase):

    def test_generate(self):

        food = Food()
        snake = Snake(5)
        food.generate(snake)

        self.assertGreaterEqual(food.food_x, 0)
        self.assertLessEqual(food.food_x, 880)

        self.assertGreaterEqual(food.food_y, 0)
        self.assertLessEqual(food.food_y, 720)

        self.assertNotIn((food.food_x, food.food_y), snake.snake_body)

    def test_generate_bonus_food(self):

        food = Food()
        snake = Snake(5)
        food.generate_bonus_food(snake)

        self.assertGreaterEqual(food.bonus_food_x, 0)
        self.assertLessEqual(food.bonus_food_x, 880)

        self.assertGreaterEqual(food.bonus_food_y, 0)
        self.assertLessEqual(food.bonus_food_y, 720)

    def test_snake_eating(self):

        food = Food()
        food.food_x, food.food_y = 10, 10
        self.assertTrue(food.snake_eating(10, 10))
        self.assertFalse(food.snake_eating(20, 10))


    def test_snake_eating_bonus(self):

        food = Food()
        food.food_x, food.food_y = 10, 10
        self.assertTrue(food.snake_eating(10, 10))
        self.assertFalse(food.snake_eating(20, 10))
