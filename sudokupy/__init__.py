import numpy as np


class Cell(object):
    """
    Class for each cell within the board

    A Cell can one number 1-9 in it

    :ivar x: :class:`int`, x index [0-8] of the cell
    :ivar y: :class:`int`, y index [0-8] of the cell
    :ivar answer: :class:`int`, the value of the cell, None if not known
    :ivar possible: :class:`list`, possible values of the cell
    """

    def __init__(self, x, y):
        """
        Setup a Cell

        :param x:  :class:`int`, the location 0-8 in X
        :param y:  :class:`int`, the location 0-8 in Y
        """
        self.possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.answer = None
        self.x = x
        self.y = y

    def remove(self, num):
        """
        remove a number from self.possible

        :param num: :class:`int`, remove a number form possible
        """
        if self.answer == num:
            raise ValueError('Attempting to remove the answer from this Cell: {}'.format(self))
        if num in self.possible:
            self.possible.remove(num)
        self.isComplete()

    def setAnswer(self, num):
        """
        Set the answer for a Cell

        :param num: :class:`int`, remove a number form possible
        """
        self.answer = num
        self.possible = [num]

    def isComplete(self):
        """
        If there is only one possible left set it

        :return: :class:`bool`, True if complete, False if not
        """
        if len(self.possible) == 1:
            self.answer = self.possible[0]
            return True
        else:
            return False

    def __repr__(self):
        return "<sudokupy.Cell [{},{}] {}>".format(self.x, self.y, self.possible)

    __str__ = __repr__

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


class Board(object):
    """
    The game board

    :ivar cells: :class:`numpy.ndarray`, the :class:`Cell` of the board (9*9=27)
    """

    def __init__(self, cells):
        """
        The game board made up of cells

        :param cells: :class:`numpy.ndarray`, the :class:`Cell` of the board (9*9=27)
        """
        self.cells = cells

    @classmethod
    def emptyBoard(cls):
        """
        Create an empty game board

        A board has 9 :class:`Row` and 9 :class:`Column` and 9 :class:`Square`, create them all

        """
        cells = np.empty((9, 9), dtype=object)
        # This might be faster with list comp or something, but there are just 27
        for ix, iy in np.ndindex(cells.shape):
            cells[ix, iy] = Cell(ix, iy)
        return Board(cells)

    def prettyPrint(self):
        """
        print a nice version of the board

        :return: :class:`str` the string that makes up the board
        """
        raise NotImplementedError('still need to make this')
