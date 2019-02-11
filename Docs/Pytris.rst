Pytris
==========

class Block
----------

.. function:: convert_shape(self)

   Convert block from shape form into int array.

   :return: Array with converted position of block.
   :rtype: int array

class Board
----------

.. function:: create_grid(self)

   Create grid and fill it with black colour.

   :return: Matrix which represent game board.
   :rtype: int matrix
   
.. function:: draw_grid(self)

   Draw grid(line) on the screen.
   
.. function:: draw_board(self)

   Draw grid(content) on the screen.
   
.. function:: draw_next_shape(self, shape)

   Draw the next shape, near game board.

   :param shape: object of Block class
   
.. function:: check_space(self, shape)

   Check if the block could be move in that place of grid.

   :param shape: object of Block class
   :rtype: Boolean
   
.. function:: check_full(self)

   Check if the game board is full.
   
   :rtype: Boolean
   
.. function:: check_row(self)
   
   Check how many rows are full.
   
   :return: Number of full rows multipled by 10, what is score.
   :rtype: Intiger
