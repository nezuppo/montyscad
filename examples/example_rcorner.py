#!/usr/bin/env python3

from montyscad import Scad
from montyscad import monty_symbols as ms
from montyscad.ext import rcorner

def example():
    scad = Scad()
    scad += [
        '$fn = 120;',
        ms.color('red')(
            ms.linear_extrude(1)(
                rcorner(5, 1)
            )
        ),
        ms.color('blue')(
            ms.linear_extrude(1)(
                rcorner(5, 2)
            )
        ),
        ms.color('yellow')(
            ms.linear_extrude(1)(
                rcorner(5, 3)
            )
        ),
        ms.color('green')(
            ms.linear_extrude(1)(
                rcorner(5, 4)
            )
        ),
    ]
    scad.write('example_rcorner.scad')

if __name__ == '__main__':
    example()
