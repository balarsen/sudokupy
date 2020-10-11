sudokupy documentation
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Build
-----
.. code-block:: bash

    git clone git@github.com:balarsen/sudokupy.git
    cd sudokupy
    pip install -r requirements
    python setup.py install
    cd docs
    make html


Example
-------
.. image:: _static/Sudoku_Puzzle_by_L2G-example.png
  :width: 400
  :alt: Sudoku puzzle

.. code-block:: python

    import itertools
    import numpy as np
    from sudokupy import Board
    b = Board.emptyBoard()
    b.cells[0, 0].setAnswer(5)
    b.cells[0, 1].setAnswer(3)
    b.cells[0, 4].setAnswer(7)

    b.cells[1, 0].setAnswer(6)
    b.cells[1, 3].setAnswer(1)
    b.cells[1, 4].setAnswer(9)
    b.cells[1, 5].setAnswer(5)

    b.cells[2, 1].setAnswer(9)
    b.cells[2, 2].setAnswer(8)
    b.cells[2, 7].setAnswer(6)

    b.cells[3, 0].setAnswer(8)
    b.cells[3, 4].setAnswer(6)
    b.cells[3, 8].setAnswer(3)

    b.cells[4, 0].setAnswer(4)
    b.cells[4, 3].setAnswer(8)
    b.cells[4, 5].setAnswer(3)
    b.cells[4, 8].setAnswer(1)

    b.cells[5, 0].setAnswer(7)
    b.cells[5, 4].setAnswer(2)
    b.cells[5, 8].setAnswer(6)

    b.cells[6, 1].setAnswer(6)
    b.cells[6, 6].setAnswer(2)
    b.cells[6, 7].setAnswer(8)

    b.cells[7, 3].setAnswer(4)
    b.cells[7, 4].setAnswer(1)
    b.cells[7, 5].setAnswer(9)
    b.cells[7, 8].setAnswer(5)

    b.cells[8, 4].setAnswer(8)
    b.cells[8, 7].setAnswer(7)
    b.cells[8, 8].setAnswer(9)
    print(b.unfinished)
    print(b.prettyStr())

    for ix, iy in np.ndindex(b.cells.shape):
        b.processCell(ix, iy)
    print(b.unfinished)
    print(b.prettyStr())

    for ix, iy in np.ndindex(b.cells.shape):
        b.processCell(ix, iy)
    print(b.unfinished)
    print(b.prettyStr())

    """
    51
    [['5' '3' '*' '*' '7' '*' '*' '*' '*']
     ['6' '*' '*' '1' '9' '5' '*' '*' '*']
     ['*' '9' '8' '*' '*' '*' '*' '6' '*']
     ['8' '*' '*' '*' '6' '*' '*' '*' '3']
     ['4' '*' '*' '8' '*' '3' '*' '*' '1']
     ['7' '*' '*' '*' '2' '*' '*' '*' '6']
     ['*' '6' '*' '*' '*' '*' '2' '8' '*']
     ['*' '*' '*' '4' '1' '9' '*' '*' '5']
     ['*' '*' '*' '*' '8' '*' '*' '7' '9']]
    29
    [['5' '3' '*' '*' '7' '*' '*' '*' '*']
     ['6' '*' '*' '1' '9' '5' '*' '*' '*']
     ['1' '9' '8' '*' '4' '*' '*' '6' '*']
     ['8' '*' '*' '7' '6' '*' '*' '*' '3']
     ['4' '2' '6' '8' '5' '3' '7' '9' '1']
     ['7' '*' '*' '9' '2' '*' '*' '*' '6']
     ['9' '6' '1' '5' '3' '7' '2' '8' '4']
     ['2' '8' '7' '4' '1' '9' '6' '3' '5']
     ['3' '*' '*' '*' '8' '*' '1' '7' '9']]
    0
    [['5' '3' '4' '6' '7' '8' '9' '1' '2']
     ['6' '7' '2' '1' '9' '5' '3' '4' '8']
     ['1' '9' '8' '3' '4' '2' '5' '6' '7']
     ['8' '5' '9' '7' '6' '1' '4' '2' '3']
     ['4' '2' '6' '8' '5' '3' '7' '9' '1']
     ['7' '1' '3' '9' '2' '4' '8' '5' '6']
     ['9' '6' '1' '5' '3' '7' '2' '8' '4']
     ['2' '8' '7' '4' '1' '9' '6' '3' '5']
     ['3' '4' '5' '2' '8' '6' '1' '7' '9']]
    """



API
---


.. automodule:: sudokupy
   :members:
   :undoc-members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
