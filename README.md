# montyscad

Generate SCAD script with Python

# install dependent module

``` bash
$ pipenv install numpy
```
# Usage

design 3d object in python

`example.py:`
``` python
#!/usr/bin/env python3

import montyscad as ms

cube = ms.Symbol('cube', size=30, center=True)
sphere = ms.Symbol('sphere', r=20)
cylinder = ms.Symbol('cylinder', h=40, r=10)

difference = ms.Symbol('difference')
difference.append(cube)
difference.append(sphere)

translate = ms.Symbol('translate', v=[0, 0, 30])
translate.append(cylinder)

union = ms.Symbol('union')
union.append(difference)
union.append(translate)

print(union)
```

generate scad file

``` bash
$ python3 example.py > example.scad
```

`example.scad:`
```
union() {
  difference() {
    cube(size=30, center=true);
    sphere(r=20);
  }
  translate(v=[0, 0, 30]) {
    cylinder(h=40, r=10);
  }
}
```

