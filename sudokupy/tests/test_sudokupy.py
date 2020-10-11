import numpy as np
import pytest

from .. import indToSquare


def test_indToSquare():
    np.testing.assert_array_equal(indToSquare(0, 0), [0, 0])
    np.testing.assert_array_equal(indToSquare(0, 3), [0, 1])
    np.testing.assert_array_equal(indToSquare(0, 4), [0, 1])
    np.testing.assert_array_equal(indToSquare(0, 7), [0, 2])
    np.testing.assert_array_equal(indToSquare(7, 7), [2, 2])
    np.testing.assert_array_equal(indToSquare(6, 3), [2, 1])
    with pytest.raises(ValueError):
        indToSquare(100, 0)
