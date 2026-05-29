#!/usr/bin/env python3

import numpy as np
from montyscad import monty_symbols as ms
from montyscad.ext.color_fields import Colors

class RoundedSquare:
    '''
    corners:
               01             11
                +-------------+
               /             /
              /             /
             /             /
            +-------------+
          00              10
            

    edges:
                       x1
                +-------------+
               /             /
         0y   /             / 1y
             /             /
            +-------------+
                  x0
    '''

    def __init__(self, r, size, is_color=False):
        def get_inner_one_size(one_size):
            assert r * 2 <= one_size, (r, one_size, size)
            return one_size - r * 2

        self.r = r
        self.is_color = is_color

        if isinstance(size, list):
            size = np.array(size)
        self.size = size

        self.inner_square_size = [get_inner_one_size(one_size) for one_size in size]
        self.is_no_inner = (self.inner_square_size[0] == 0 or self.inner_square_size[1] == 0)
        self._body = None

    def __post_process(self, symbol, is_add, is_color):
        if is_color or (is_color is None and self.is_color):
            symbol = ms.color(Colors.get_next_color())(
                symbol
            )

        if is_add:
            if self._body is None:
                self._body = ms.union()

            self._body.append(symbol)

        return symbol

    def inner_square(self, is_add=True, is_color=None):
        if self.is_no_inner:
            return None

        square = ms.translate(np.array([1, 1]) * self.r)(
            ms.square(self.inner_square_size)
        )

        return self.__post_process(square, is_add, is_color)
 
    def corner_00(self, is_add=True, is_color=None):
        corner = ms.translate(np.array([1, 1]) * self.r)(
            ms.circle(r=self.r)
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_01(self, is_add=True, is_color=None):
        if self.inner_square_size[1] == 0:
            return None

        corner_00 = self.corner_00(is_add=False, is_color=False)
        if corner_00 is None:
            return None

        corner = ms.translate([0, self.inner_square_size[1]])(
            corner_00
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_10(self, is_add=True, is_color=None):
        if self.inner_square_size[0] == 0:
            return None

        corner_00 = self.corner_00(is_add=False, is_color=False)
        if corner_00 is None:
            return None

        corner = ms.translate([self.inner_square_size[0], 0])(
            corner_00
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_11(self, is_add=True, is_color=None):
        if self.inner_square_size[0] == 0:
            return None
        if self.inner_square_size[1] == 0:
            return None

        corner_00 = self.corner_00(is_add=False, is_color=False)
        if corner_00 is None:
            return None

        corner = ms.translate([self.inner_square_size[0], self.inner_square_size[1]])(
            corner_00
        )

        return self.__post_process(corner, is_add, is_color)

    def edge_x0(self, is_add=True, is_color=None):
        if self.inner_square_size[0] == 0:
            return None

        edge = ms.translate([self.r, 0])(
            ms.square([self.inner_square_size[0], self.r])
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_x1(self, is_add=True, is_color=None):
        edge_x0 = self.edge_x0(is_add=False, is_color=False)
        if edge_x0 is None:
            return None

        edge = ms.translate([0, self.inner_square_size[1] + self.r])(
            edge_x0
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_0y(self, is_add=True, is_color=None):
        if self.inner_square_size[1] == 0:
            return None

        edge = ms.translate([0, self.r])(
            ms.square([self.r, self.inner_square_size[1]])
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_1y(self, is_add=True, is_color=None):
        edge_0y = self.edge_0y(is_add=False, is_color=False)
        if edge_0y is None:
            return None

        edge = ms.translate([self.inner_square_size[0] + self.r, 0])(
            edge_0y
        )

        return self.__post_process(edge, is_add, is_color)

    def get_body(self, center=False):
        if self._body is None:
            self._body = ms.hull()
            self.corner_00(is_color=False)
            self.corner_01(is_color=False)
            self.corner_10(is_color=False)
            self.corner_11(is_color=False)

            body = self._body
            if self.is_color:
                body = ms.color(Colors.get_next_color())(
                    body
                )
        else:
            body = self._body

        if center:
            body = ms.translate(self.size / -2)(
                body
            )

        return body

def _example():
    import os.path
    from decimal import Decimal
    from montyscad import (
        Scad,
        Symbol,
    )

    rsquare_full_body = RoundedSquare(
        Decimal('5.0'),
        [Decimal('50'), Decimal('40')],
        is_color=True
    )

    rsquare_parts = RoundedSquare(
        Decimal('5.0'),
        [Decimal('50'), Decimal('40')],
        is_color=True
    )
    rsquare_parts.inner_square()
    rsquare_parts.corner_00()
#   rsquare_parts.corner_01()
    rsquare_parts.corner_10()
#   rsquare_parts.corner_11()
    rsquare_parts.edge_x0()
#   rsquare_parts.edge_x1()
    rsquare_parts.edge_0y()
    rsquare_parts.edge_1y()

    scad = Scad()
    scad += [
        Symbol('echo', '=== start ==='),
        '$fn=60;',

        ms.translate([0, 0])(
            rsquare_full_body.get_body(center=True)
        ),
        ms.translate([60, 0])(
            rsquare_parts.get_body(center=True)
        )
    ]

    file = os.path.splitext(__file__)[0]
    file = os.path.basename(file)
    file = './__work/__' + file + '.scad'
    scad.write(file)

if __name__ == '__main__':
    _example()
