#!/usr/bin/env python3

import numpy as np
from montyscad import monty_symbols as ms
from montyscad.ext.color_fields import Colors

class RoundedCube:
    """
    corners:
              011 +-----+ 111
                 /     /|
                /     / |
               /     /  |
              /     /   |
             /     /    |
        001 +-----+     + 110
            |     |    /
            |     |   /
            |     |  /
            |     | /
            |     |/
            +-----+
         000      100


    edges:
                    x11
                  +-----+
                 /     /|
                /     / |
           0y1 /     /  | 11z
              /     /   |
             /     /    |
            +-----+     +
            | x01 |    /
            |     |   /
        00z |     |  / 1y0
            |     | /
            |     |/
            +-----+
              x00


    faces:
                  +-----+
                 /     /|
                /     / |
               / xy1 /  |
              /     /   | x1z
             /     /    |
            +-----+ 1yz +
            |     |    /
        0yz |     |   /
            | x0z |  /
            |     | / xy0
            |     |/
            +-----+
    """

    def __init__(self, r, size, center=False, is_color=False):
        def get_inner_one_size(one_size):
            assert r * 2 <= one_size, (r, one_size, size)
            return one_size - r * 2

        self.r = r
        self.center = center
        self.is_color = is_color

        if isinstance(size, list):
            size = np.array(size)
        self.size = size

        self.inner_cube_size = [get_inner_one_size(one_size) for one_size in size]
        self.is_no_inner = (self.inner_cube_size[0] == 0 or self.inner_cube_size[1] == 0 or self.inner_cube_size[2] == 0)
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

    def inner_cube(self, is_add=True, is_color=None):
        if self.is_no_inner:
            return None

        cube = ms.translate(np.array([1, 1, 1]) * self.r)(
            ms.cube(self.inner_cube_size)
        )

        return self.__post_process(cube, is_add, is_color)
        
    def corner_000(self, is_add=True, is_color=None):
        corner = ms.translate(np.array([1, 1, 1]) * self.r)(
            ms.sphere(r=self.r)
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_001(self, is_add=True, is_color=None):
        if self.inner_cube_size[2] == 0:
            return None

        corner_000 = self.corner_000(is_add=False, is_color=False)
        if corner_000 is None:
            return None

        corner = ms.translate([0, 0, self.inner_cube_size[2]])(
            corner_000
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_010(self, is_add=True, is_color=None):
        if self.inner_cube_size[1] == 0:
            return None

        corner_000 = self.corner_000(is_add=False, is_color=False)
        if corner_000 is None:
            return None

        corner = ms.translate([0, self.inner_cube_size[1]])(
            corner_000
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_011(self, is_add=True, is_color=None):
        if self.inner_cube_size[1] == 0:
            return None
        if self.inner_cube_size[2] == 0:
            return None

        corner_000 = self.corner_000(is_add=False, is_color=False)
        if corner_000 is None:
            return None

        corner = ms.translate([0, self.inner_cube_size[1], self.inner_cube_size[2]])(
            corner_000
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_100(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None

        corner_000 = self.corner_000(is_add=False, is_color=False)
        if corner_000 is None:
            return None

        corner = ms.translate([self.inner_cube_size[0], 0])(
            corner_000
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_101(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None
        if self.inner_cube_size[2] == 0:
            return None

        corner_000 = self.corner_000(is_add=False, is_color=False)
        if corner_000 is None:
            return None

        corner = ms.translate([self.inner_cube_size[0], 0, self.inner_cube_size[2]])(
            corner_000
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_110(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None
        if self.inner_cube_size[1] == 0:
            return None

        corner_000 = self.corner_000(is_add=False, is_color=False)
        if corner_000 is None:
            return None

        corner = ms.translate([self.inner_cube_size[0], self.inner_cube_size[1]])(
            corner_000
        )

        return self.__post_process(corner, is_add, is_color)

    def corner_111(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None
        if self.inner_cube_size[1] == 0:
            return None
        if self.inner_cube_size[2] == 0:
            return None

        corner_000 = self.corner_000(is_add=False, is_color=False)
        if corner_000 is None:
            return None

        corner = ms.translate(self.inner_cube_size)(
            corner_000
        )

        return self.__post_process(corner, is_add, is_color)

    def edge_x00(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None

        edge = ms.translate([self.r, self.r, self.r])(
            ms.rotate(90, [0, 1, 0])(
                ms.cylinder(self.inner_cube_size[0], r=self.r)
            )
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_x01(self, is_add=True, is_color=None):
        if self.inner_cube_size[2] == 0:
            return None

        edge_x00 = self.edge_x00(is_add=False, is_color=False)
        if edge_x00 is None:
            return None

        edge = ms.translate([0, 0, self.inner_cube_size[2]])(
            edge_x00
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_x10(self, is_add=True, is_color=None):
        if self.inner_cube_size[1] == 0:
            return None

        edge_x00 = self.edge_x00(is_add=False, is_color=False)
        if edge_x00 is None:
            return None

        edge = ms.translate([0, self.inner_cube_size[1], 0])(
            edge_x00
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_x11(self, is_add=True, is_color=None):
        if self.inner_cube_size[1] == 0:
            return None
        if self.inner_cube_size[2] == 0:
            return None

        edge_x00 = self.edge_x00(is_add=False, is_color=False)
        if edge_x00 is None:
            return None

        edge = ms.translate([0, self.inner_cube_size[1], self.inner_cube_size[2]])(
            edge_x00
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_0y0(self, is_add=True, is_color=None):
        if self.inner_cube_size[1] == 0:
            return None

        edge = ms.translate([self.r, self.r, self.r])(
            ms.rotate(-90, [1, 0, 0])(
                ms.cylinder(self.inner_cube_size[1], r=self.r)
            )
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_0y1(self, is_add=True, is_color=None):
        if self.inner_cube_size[2] == 0:
            return None

        edge_0y0 = self.edge_0y0(is_add=False, is_color=False)
        if edge_0y0 is None:
            return None

        edge = ms.translate([0, 0, self.inner_cube_size[2]])(
            edge_0y0
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_1y0(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None

        edge_0y0 = self.edge_0y0(is_add=False, is_color=False)
        if edge_0y0 is None:
            return None

        edge = ms.translate([self.inner_cube_size[0], 0, 0])(
            edge_0y0
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_1y1(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None
        if self.inner_cube_size[2] == 0:
            return None

        edge_0y0 = self.edge_0y0(is_add=False, is_color=False)
        if edge_0y0 is None:
            return None

        edge = ms.translate([self.inner_cube_size[0], 0, self.inner_cube_size[2]])(
            edge_0y0
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_00z(self, is_add=True, is_color=None):
        if self.inner_cube_size[2] == 0:
            return None

        edge = ms.translate([self.r, self.r, self.r])(
            ms.cylinder(self.inner_cube_size[2], r=self.r)
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_01z(self, is_add=True, is_color=None):
        if self.inner_cube_size[1] == 0:
            return None

        edge_00z = self.edge_00z(is_add=False, is_color=False)
        if edge_00z is None:
            return None

        edge = ms.translate([0, self.inner_cube_size[1], 0])(
            edge_00z
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_10z(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None

        edge_00z = self.edge_00z(is_add=False, is_color=False)
        if edge_00z is None:
            return None

        edge = ms.translate([self.inner_cube_size[0], 0, 0])(
            edge_00z
        )

        return self.__post_process(edge, is_add, is_color)

    def edge_11z(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None
        if self.inner_cube_size[1] == 0:
            return None

        edge_00z = self.edge_00z(is_add=False, is_color=False)
        if edge_00z is None:
            return None

        edge = ms.translate([self.inner_cube_size[0], self.inner_cube_size[1], 0])(
            edge_00z
        )

        return self.__post_process(edge, is_add, is_color)

    def face_xy0(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None
        if self.inner_cube_size[1] == 0:
            return None

        face = ms.translate(np.array([1, 1]) * self.r)(
            ms.cube([self.inner_cube_size[0], self.inner_cube_size[1], self.r])
        )

        return self.__post_process(face, is_add, is_color)

    def face_xy1(self, is_add=True, is_color=None):
        face_xy0 = self.face_xy0(is_add=False, is_color=False)
        if face_xy0 is None:
            return None

        face = ms.translate([0, 0, self.r + self.inner_cube_size[2]])(
            face_xy0
        )

        return self.__post_process(face, is_add, is_color)

    def face_x0z(self, is_add=True, is_color=None):
        if self.inner_cube_size[0] == 0:
            return None
        if self.inner_cube_size[2] == 0:
            return None

        face = ms.translate([self.r, 0, self.r])(
            ms.cube([self.inner_cube_size[0], self.r, self.inner_cube_size[2]])
        )

        return self.__post_process(face, is_add, is_color)

    def face_x1z(self, is_add=True, is_color=None):
        face_x0z = self.face_x0z(is_add=False, is_color=False)
        if face_x0z is None:
            return None

        face = ms.translate([0, self.r + self.inner_cube_size[1], 0])(
            face_x0z
        )

        return self.__post_process(face, is_add, is_color)

    def face_0yz(self, is_add=True, is_color=None):
        if self.inner_cube_size[1] == 0:
            return None
        if self.inner_cube_size[2] == 0:
            return None

        face = ms.translate([0, self.r, self.r])(
            ms.cube([self.r, self.inner_cube_size[1], self.inner_cube_size[2]])
        )

        return self.__post_process(face, is_add, is_color)

    def face_1yz(self, is_add=True, is_color=None):
        face_0yz = self.face_0yz(is_add=False, is_color=False)
        if face_0yz is None:
            return None

        face = ms.translate([self.r + self.inner_cube_size[0], 0])(
            face_0yz
        )

        return self.__post_process(face, is_add, is_color)

    def get_body(self, center=False):
        if self._body is None:
            self._body = ms.hull()

            self.corner_000(is_color=False)
            self.corner_001(is_color=False)
            self.corner_010(is_color=False)
            self.corner_011(is_color=False)
            self.corner_100(is_color=False)
            self.corner_101(is_color=False)
            self.corner_110(is_color=False)
            self.corner_111(is_color=False)

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

    rcube_full_body = RoundedCube(
        Decimal('5.0'),
        [Decimal('50'), Decimal('40'), Decimal('30')],
        is_color=True
    )

    rcube_parts = RoundedCube(
        Decimal('5.0'),
        [Decimal('50'), Decimal('40'), Decimal('30')],
        is_color=True
    )
    rcube_parts.inner_cube()
    rcube_parts.corner_000()
#   rcube_parts.corner_001()
    rcube_parts.corner_010()
#   rcube_parts.corner_011()
    rcube_parts.corner_100()
#   rcube_parts.corner_101()
    rcube_parts.corner_110()
#   rcube_parts.corner_111()
    rcube_parts.edge_x00()
#   rcube_parts.edge_x01()
    rcube_parts.edge_x10()
#   rcube_parts.edge_x11()
    rcube_parts.edge_0y0()
#   rcube_parts.edge_0y1()
    rcube_parts.edge_1y0()
#   rcube_parts.edge_1y1()
    rcube_parts.edge_00z()
    rcube_parts.edge_01z()
    rcube_parts.edge_10z()
    rcube_parts.edge_11z()
    rcube_parts.face_xy0()
#   rcube_parts.face_xy1()
    rcube_parts.face_x0z()
    rcube_parts.face_x1z()
    rcube_parts.face_0yz()
    rcube_parts.face_1yz()

    scad = Scad()
    scad += [
        Symbol('echo', '=== start ==='),
        '$fn=60;',

        ms.translate([0, 0])(
            rcube_full_body.get_body(center=True)
        ),
        ms.translate([60, 0])(
            rcube_parts.get_body(center=True)
        ),
    ]

    file = os.path.splitext(__file__)[0]
    file = os.path.basename(file)
    file = './__work/__' + file + '.scad'
    scad.write(file)

if __name__ == '__main__':
    _example()
