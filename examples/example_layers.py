#!/usr/bin/env python3

from montyscad.ext import layers

def _example():
    print(
        layers(
            (
                # layer3
                (
                    3,
                    ColorFields(
                        ms.Square(5, center=True),
                        ms.Circle(d=3)
                    )
                ),

                # layer2
                (2, ms.Circle(d=10)),

                # layer1
                (1, ms.Square(10, center=True))
            ),
            ColorFields.ALL
        )
    )

if __name__ == '__main__':
    _example()
