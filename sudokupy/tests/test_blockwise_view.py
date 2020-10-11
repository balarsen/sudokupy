# modified from https://github.com/ilastik/lazyflow/blob/master/tests/test_lazyflow/test_utility/test_blockwise_view.py
# huge thanks!

import numpy

from ..blockwise_view import blockwise_view


def test_2d():
    # Adapted from:
    # http://stackoverflow.com/a/8070716/162094
    n = 4
    m = 5
    a = numpy.arange(1, n * m + 1).reshape(n, m)

    sz = a.itemsize
    h, w = a.shape
    bh, bw = 2, 2
    shape = (h // bh, w // bw, bh, bw)

    strides = sz * numpy.array([w * bh, bw, w, 1])

    # This is our reference, copied straight from stackoverflow
    blocks = numpy.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

    view = blockwise_view(a, (bh, bw), require_aligned_blocks=False)

    assert view.shape == blocks.shape
    assert (view == blocks).all()

    # Prove that this was a view, not a copy
    view[:] = 0
    assert (a[0:4, 0:4] == 0).all(), "blockwise_view returned a copy, not a view!"


def test_3d():
    """
    Copy a 3D array block-by-block into a 6D array,
    and verify that the result matches blockwise_view()
    """
    orig_data = numpy.random.random((6, 9, 16))
    blockshape = (2, 3, 4)
    final_shape = tuple(numpy.array(orig_data.shape) // blockshape) + blockshape
    assert final_shape == (3, 3, 4, 2, 3, 4), final_shape

    blockwise_copy = numpy.zeros(final_shape)

    block_addresses = final_shape[0:3]
    for x in range(block_addresses[0]):
        for y in range(block_addresses[1]):
            for z in range(block_addresses[2]):
                block_start = numpy.array((x, y, z)) * blockshape
                block_stop = block_start + blockshape
                blockwise_copy[x, y, z] = orig_data[
                    block_start[0] : block_stop[0], block_start[1] : block_stop[1], block_start[2] : block_stop[2]
                ]

    view = blockwise_view(orig_data, blockshape)

    assert view.shape == blockwise_copy.shape
    assert (view == blockwise_copy).all()

    assert not view.flags["C_CONTIGUOUS"]

    c_order_copy = view.copy("C")
    assert c_order_copy.flags["C_CONTIGUOUS"]


def test_3d_aslist():
    """
    Verify that the blocks returned in the list format match the ones returned in the array format.
    """
    orig_data = numpy.random.random((6, 9, 16))
    blockshape = (2, 3, 4)
    final_shape = tuple(numpy.array(orig_data.shape) // blockshape) + blockshape
    assert final_shape == (3, 3, 4, 2, 3, 4), final_shape

    array_view = blockwise_view(orig_data, blockshape)
    block_list = blockwise_view(orig_data, blockshape, aslist=True)

    assert (numpy.array(block_list) == array_view.reshape((-1,) + blockshape)).all()

