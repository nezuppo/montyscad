
montyscad
=====================

montyscad is python package for creating solid 3D CAD models with OpenSCAD

Install dependent package
==============================

.. sourcecode::

  $ pip install numpy

Usage
===================

create 3D models in python

example.py::

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

generate scad file

.. sourcecode::

  $ python3 example.py

/tmp/example.scad::

  $fn=36;
  union() {
    difference() {
      cube(size=30, center=true);
      sphere(r=20.1);
    }
    translate([0, 0, 30]) {
      cylinder(40, r=10);
    }
  }
