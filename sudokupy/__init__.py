import itertools

import numpy as np

from .blockwise_view import blockwise_view


def cellIndToSquareInd(x, y):
    """
    Take a [0-8, 0-8] Cell index and make it a [0-2, 0-2] square index

    :param x:  :class:`int`, the location 0-8 in X
    :param y:  :class:`int`, the location 0-8 in Y
    :return: :class:`numpy.ndarray`, the square indices for the square the cell is in [0-2, 0-2]
    """
    # this can probably be done smarter, but not seeing it this second
    out = np.empty(2, dtype=int)
    if (x >= 0) and (x < 3):
        out[0] = 0
    elif (x >= 3) and (x < 6):
        out[0] = 1
    elif (x >= 6) and (x < 9):
        out[0] = 2
    else:
        raise (ValueError("invalid Cell index"))

    if (y >= 0) and (y < 3):
        out[1] = 0
    elif (y >= 3) and (y < 6):
        out[1] = 1
    elif (y >= 6) and (y < 9):
        out[1] = 2
    else:
        raise (ValueError("invalid Cell index"))
    return out


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
        :return: :class:`bool`, True if a number was removed, False otherwise
        """
        removed = False
        if self.answer == num:
            raise ValueError('Attempting to remove the answer from this Cell: {}'.format(self))
        if num in self.possible:
            self.possible.remove(num)
            removed = True
        self.isComplete()
        return removed

    @property
    def answered(self):
        """
        if the cell has answer set return True, False otherwise

        :return: :class:`bool`,  if the cell has answer set return True, False otherwise
        """
        return self.answer is not None

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

        :param cells: :class:`numpy.ndarray`, the :class:`Cell` of the board (9*9=81)
        """
        self.cells = np.require(cells, requirements=["C_CONTIGUOUS"])
        assert self.cells.shape == (9, 9)
        self.blocks = blockwise_view(self.cells, (3, 3))

    def processCell(self, x, y):
        """
        process the square, row, and columns for a particular cell

        :param x:  :class:`int`, the location 0-8 in X
        :param y:  :class:`int`, the location 0-8 in Y
        :return: :class:`int`, the number of cells changed
        """
        processed = 0
        processed += self.processRow(x)
        processed += self.processColumn(y)
        processed += self.processSquare(*cellIndToSquareInd(x, y))
        return processed

    @property
    def unfinished(self):
        """
        get the number of unfinished cells in the board

        :return: :class:`int`, the number of :class:`Cell` without answer
        """
        return np.product(self.cells.shape) - np.sum([v.answered for v in self.cells.ravel()])

    @classmethod
    def emptyBoard(cls):
        """
        Create an empty game board

        A board has 9 :class:`Row` and 9 :class:`Column` and 9 :class:`Square`, create them all

        """
        cells = np.empty((9, 9), dtype=object)
        # This might be faster with list comp or something, but there are just 81
        for ix, iy in np.ndindex(cells.shape):
            cells[ix, iy] = Cell(ix, iy)
        return Board(cells)

    def processRow(self, idx):
        """
        Process a row removing answers from each cell in the row

        :param idx: :class:`int`, the y index [0-8] of the Row
        :return: :class:`int`, the number of cells changed
        """
        processed = 0
        for c in self.cells[idx, :]:
            if c.answered:
                for c2 in self.cells[idx, :]:
                    if c == c2:
                        continue
                    else:
                        processed += int(c2.remove(c.answer))
        return processed

    def processColumn(self, idx):
        """
        Process a columns removing answers from each cell in the column

        :param idx: :class:`int`, the x index [0-8] of the Column
        :return: :class:`int`, the number of cells changed
        """
        processed = 0
        for c in self.cells[:, idx]:
            if c.answered:
                for c2 in self.cells[:, idx]:
                    if c == c2:
                        continue
                    else:
                        processed += int(c2.remove(c.answer))
        return processed

    def processSquare(self, x, y):
        """
        Process a square in a board given by x [0-2] and y [0-2]

        :param x: :class:`int`, the x index [0-2] of the Square
        :param y: :class:`int`, the y index [0-2] of the Square
        :return: :class:`int`, the number of cells changed
        """
        processed = 0
        _blocks = self.blocks[x, y].ravel()
        for c in _blocks:
            if c.answered:
                for c2 in _blocks:
                    if c == c2:
                        continue
                    else:
                        processed += int(c2.remove(c.answer))
        return processed

    def prettyStr(self):
        """
        Return a nice version of the board

        :return: :class:`str` the string that makes up the board
        """
        out = np.full((9, 9), '*')
        for x, y in itertools.product(range(9), range(9)):
            if self.cells[x, y].answered:
                out[x, y] = self.cells[x, y].answer
        return str(out)
