Scad クラスについて
--------------------

Scad クラスは拡張子が ``.scad`` の OpenSCAD で扱う scad ファイル をイメージしています。

3D オブジェクトや文字列を追加
==============================

拡張子が ``.scad`` の scad ファイルに 3D オブジェクトを書き込んでいくように
Scad オブジェクトに 3D オブジェクトを追加していきます。文字列を追加することもできます。

.. code-block::

    scad = Scad()
    scad += [
        '$fn=36;',
        ms.cube(size=30, center=True),
        ms.cylinder(40, r=10)
    ]

scad ファイルへの書き出し
==============================

write() メソッドの引数に scad ファイル名を指定して書き出します。scad
オブジェクトに追加された項目が書き出されます。

.. code-block::

    scad.write('test.scad')

Scad クラスは list 型から派生
===================================

Scad クラスは list 型から派生しているため、list の様々なメソッドを使用できます。

例えば、

.. code-block::

    scad += [
        '$fn=36;',
        ms.cube(size=30, center=True),
        ms.cylinder(40, r=10)
    ]

と同様に以下のように append() メソッドを使用して 3D オブジェクトを追加することもできます。

.. code-block::

    scad.append('$fn=36;')
    scad.append(ms.cube(size=30, center=True))
    scad.append(ms.cylinder(40, r=10))

利用する機会は少ないと思われますが、その他にも
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
で説明されている list の演算や clear(), copy() メソッドなども使えるはずです。
(試したことないですが、きっと使えます。。。)
