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
        if num in self.possible:
            self.possible.remove(num)
        self.isComplete()

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
        return "<sudokupy.Cell ({},{}) {}>".format(self.x, self.y, self.possible)

    __str__ = __repr__


class Row(object):
    """
    Class for a row of the game board
    """


class Column(Row):
    """
    Class for a column of the gam board
    """


class Square(object):
    """
    Class for a 3x3 square of the board
    """


class Board(object):
    """
    The game board
    """

    @classmethod
    def emptyBoard(cls):
        """
        Create an empty game board

        A board has 9 :class:`Row` and 9 :class:`Column` and 9 :class:`Square`, create them all

        :return:
        """
