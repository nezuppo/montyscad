#!/usr/bin/env python3

from decimal import Decimal
from montyscad import Scad
from montyscad import monty_symbols as ms

cube = ms.cube(size=30, center=True)
sphere = ms.sphere(r=Decimal('20.1'))
cylinder = ms.cylinder(40, r=10)

scad = Scad()
scad += [
  '$fn=36;',
  ms.union()(
    ms.difference()(
      cube,
      sphere
    ),
    ms.translate([0, 0, 30])(
      cylinder
    )
  )
]
scad.write('/tmp/example.scad')
