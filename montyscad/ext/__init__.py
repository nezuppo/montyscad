#!/usr/bin/env python3

import numpy as np
from montyscad import monty_symbols as ms

def rotate_pos(a, v, pos, symbol):
    '''
    pos: center of rotation
    '''

    if not isinstance(pos, np.ndarray):
        pos = np.array(pos)

    return ms.translate(pos)(
        ms.rotate(a=a, v=v)(
            ms.translate(pos * -1)(
                symbol
            )
        )
    )

def rsquare(r, size, **kwargs):
    assert r * 2 < size[0], (r, size[0])
    assert r * 2 < size[1], (r, size[1])

    if not isinstance(size, np.ndarray):
        size = np.array(size)

    symbol = ms.offset(r=r)(
        ms.square(size=size - r * 2, **kwargs)
    )
    if 'center' not in kwargs or not kwargs['center']:
        symbol = ms.translate([r, r])(symbol)

    return symbol
