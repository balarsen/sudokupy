import numpy as np
import pytest

from .. import cellIndToSquareInd


def test_cellIndToSquareInd():
    np.testing.assert_array_equal(cellIndToSquareInd(0, 0), [0, 0])
    np.testing.assert_array_equal(cellIndToSquareInd(0, 3), [0, 1])
    np.testing.assert_array_equal(cellIndToSquareInd(0, 4), [0, 1])
    np.testing.assert_array_equal(cellIndToSquareInd(0, 7), [0, 2])
    np.testing.assert_array_equal(cellIndToSquareInd(7, 7), [2, 2])
    np.testing.assert_array_equal(cellIndToSquareInd(6, 3), [2, 1])
    with pytest.raises(ValueError):
        cellIndToSquareInd(100, 0)
