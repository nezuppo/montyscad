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
