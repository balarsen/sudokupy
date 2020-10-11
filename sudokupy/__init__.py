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


class Row(object):
    """
    Class for a row of the game board

    :ivar ind: :class:`int`, y index [0-8] of the Row
    :ivar cells: :class:`list`, cells in the Row
    """

    def __init__(self, ind, cells):
        """
        Setup a Row

        :param ind:  :class:`int`, the location 0-8 in Y
        :param cells: :class:`list`, the :class:`Cell`s in the Row
        """
        self.ind = ind
        self.cells = cells

    def process(self):
        """
        Loop over the cells, removing and from the cells that have answers
        """
        for c1 in self.cells:
            if c1.answer is not None:
                for c2 in self.cells:
                    print('c1', c1, 'c2', c2)
                    if c2 == c1:
                        continue
                    else:
                        c2.remove[c1.answer]

    def __repr__(self):
        return "<sudokupy.Row [{}]>".format(self.ind)


class Column(Row):
    """
    Class for a column of the game board

    :ivar ind: :class:`int`, x index [0-8] of the Column
    :ivar cells: :class:`list`, cells in the Row
    """

    def __init__(self, ind, cells):
        super().__init__(ind, cells)

    def __repr__(self):
        return "<sudokupy.Column [{}]>".format(self.ind)


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
