#!/usr/bin/env python3

from decimal import Decimal
from montyscad import Scad
from montyscad import monty_symbols as ms

scad = Scad()

scad += [
  '$fn=36;',
  ms.union()(
    ms.difference()(
      ms.cube(size=30, center=True),
      ms.sphere(r=Decimal('20.1'))
    ),
    ms.translate([0, 0, 30])(
      ms.cylinder(40, r=10)
    )
  )
]

scad.write('/tmp/example.scad')
