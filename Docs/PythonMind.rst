Python Mind
==========


class Types
----------

.. function:: fill_arrays(self)

  Fill game array with random elements.
  
.. function:: print_game_array(self)

  Print game array on the screen.
  
.. function:: check_change_colour(self, position, level)

  Check if player change colour of elements.
  
  :param position: actuall mouse position
  :param level: actuall game level
  
.. function:: change_colour(self, position, dimension_x, dimension_y, column)

  Change colour of the element in the game array.
  
  :param position: actuall mouse position
  :param dimension_x: value of cord x element in game array
  :param dimension_y: value of cord y element in game array
  :param column: number of column to change colour
  
.. function:: compare_array(self)

  Compare game array with player array, and create result array.
  
.. function:: print_result(self, level)

  Print the result of the level.
  
  :param level: actuall level of the game
