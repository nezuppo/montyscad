#!/usr/bin/env python3

import numpy as np
from montyscad import monty_symbols as ms
from montyscad.ext.color_fields import ColorFields

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

def layers(layers, cfmode=None):
    union = ms.union()
    heights = 0

    for i in range(len(layers) - 1, -1, -1):
        height, symbol = layers[i]
        if isinstance(symbol, ColorFields):
            assert cfmode is not None
            symbol = symbol.get_symbol(height, cfmode)
        else:
            symbol = ms.linear_extrude(height).add_others(
                symbol
            )

        union.append(
            ms.translate([0, 0, heights]).add_others(
                symbol
            )
        )

        heights += height

    return union

def rcorner(r, quadrant):
    symbol = ColorFields(
        ms.square(np.array([1, 1]) * (r * 2)),
        [
            ms.translate([r, r])(ms.circle(r=r)),
            ms.translate([r, 0])(ms.square([r, r])),
            ms.translate([r, r])(ms.square([r, r])),
            ms.translate([0, r])(ms.square([r, r])),
        ],
    ).get_symbol(cf_mode=ColorFields.PLAIN)

    assert quadrant in [1, 2, 3, 4], quadrant
    rotate = (quadrant - 1) * 90
    if rotate:
        symbol = ms.rotate(rotate, [0, 0, 1])(
            symbol
        )

    return symbol


