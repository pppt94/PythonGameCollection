Snake
==================

class Snake
----------
.. function:: update_position(self, inc_x, inc_y, direction)

   Update the position of snake.
   
   :param inc_x: increase of x value
   :param inc_y: increase of y value
   :param direction: one of four direction

.. function:: get_head_direction(self)

   Change the graphic of the snake's head.

.. function:: get_body_direction(self, segment_idx)

   Change the graphic of the one segment of snake's body.
   
   :param segment_idx: segment index of the snake's body
   
.. function:: get_tail_direction(self, segment_idx)

   Change the graphic of the snake's tail.
   
   :param segment_idx: index of the last segment of snake's body before tail

.. function:: draw_snake(self)

   Draw all segments of snake's body on the screen.
   
.. function:: eating_food(self, food_x, food_y, bonus_food_x, bonus_food_y)

   Increase snake's body length, when snake eats food.
   
   :param food_x: x value of food
   :param food_y: y value of food
   :param bonus_food_x: x value of bonus food
   :param bonus_food_y: y value of bonus food
   
.. function:: check_collision(self)

   Check collision between snake's head and the rest of his body.
   
   :rtype: Boolean
   
class Food
----------

.. function:: generate(self, snake)

   Generate the coordinate (x, y) of the one piece of food.
   
   :param snake: object of Snake class which contains the coordinate of snake
   
.. function:: generate_bonus_food(self, snake)

   Generate the coordinate (x, y) of the one piece of bonus food.
   
   :param snake: object of Snake class which contains the coordinate of snake
   
.. function:: draw_food(self)

   Draw one piece of the food on screen.
   

.. function:: draw_bonus_food(self)

   Draw one piece of the bonus food on screen.
   
.. function:: snake_eating(self, snake_x, snake_y)

   Check if the snake has eaten food.
   
   :param snake_x: value of x coordinate of the snake's head
   :param snake_y: value of y coordinate of the snake's head
   
.. function:: snake_eating_bonus(self, snake_x, snake_y)

   Check if the snake has eaten bonus food.
   
   :param snake_x: value of x coordinate of the snake's head
   :param snake_y: value of y coordinate of the snake's head
   
     
