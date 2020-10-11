


class Cell(object):
    """
    Class for each cell within the board
    """


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

