Symbol クラスについて
------------------------------------

montyscad では OpenSCAD の circle や cube , linear_extrude, translate 等のことをシンボルと呼びます。

[:doc:`../introduction/main`] の `example.py` では Symbol クラスは直接使っておらず Symbol クラスから派生した
circle や cube , linear_extrude, translate 等のクラスを使用していますが、まずは基本の
Symbol クラスについて説明をします。

circle や cube , linear_extrude, translate 等のクラスについては
[:doc:`../monty_symbols_module/main`] を参照して下さい。

使用例 (子要素なし)
===========================

.. code-block::

    Symbol('cylinder', 15, r=10)

というように使用します。第一引数がシンボル名、第二引数以降がシンボルに渡される実際の引数です。これは以下のように
OpenSCAD スクリプトに変換されます。

.. code-block::

    cylinder(15, r=10);


使用例 (子要素あり)
===========================

Symbol クラスは list を継承しているので子要素に別のシンボルを追加できます。

.. code-block::

    symbol = Symbol('translate', [10, 20])
    symbol.append(
        Symbol('cylinder', 15, r=10)
    )
    symbol.append(
        Symbol('circle', 15)
    )

子要素がある場合、以下のように OpenSCAD スクリプトに変換されます。

.. code-block::

    translate([10, 20]) {
      cylinder(15, r=10);
      circle(15);
    }

シンボル名毎に子要素追加の可否判断はしていないので、どんなシンボルにも子要素を追加できてしまいます。

.. code-block::

    symbol = Symbol('cylinder', 15, r=10)
    symbol.append(
        Symbol('circle', 15)
    )

この例では cylinder に子要素として circle を追加しています。以下のように
OpenSCAD スクリプトに変換できてしまいますが実際は cylinder は子要素を取れないので
OpenSCAD で読み込んだ際にワーニングが出ます。

.. code-block::

    cylinder(15, r=10) {
      circle(15);
    }

子要素の追加方法
===================

Symbol クラスは list を継承しているので append() メソッドで子要素を追加できます。

.. code-block::

    symbol = Symbol('translate', [10, 20])
    symbol.append(
        Symbol('cylinder', 15, r=10)
    )
    symbol.append(
        Symbol('circle', 15)
    )


以下のように追加することもできます。(リストの追加)

.. code-block::

    symbol = Symbol('translate', [10, 20])
    symbol += [
        Symbol('cylinder', 15, r=10),
        Symbol('circle', 15)
    ]

また、Symbol クラスは __call__() メソッドで引数を子要素に追加するように実装しているので以下のようにもできます。
実際に montyscad でコードを書く場合はこれが最も手軽にコーディングできるのでおすすめです。

.. code-block::

    symbol = Symbol('translate', [10, 20])(
        Symbol('cylinder', 15, r=10),
        Symbol('circle', 15)
    )

引数に整数を指定
===================

引数に整数を指定する場合はそのまま整数を指定するだけです。

.. code-block::

    Symbol('circle', 10)

引数に小数を指定
===================

引数に小数を指定する場合は Decimal() で指定します。

.. code-block::

    from decimal import Decimal
    Symbol('circle', Decimal('10.5'))

OpenSCAD スクリプトにはそのまま小数として変換されます。

.. code-block::

    circle(10.5);

間違って、Decimal() を使わずにそのまま小数を指定した場合は
OpenSCAD スクリプトへの変換時に以下のように例外が発生します。

.. code-block::

    Symbol('circle', 10.5)

.. code-block::

    AssertionError: ('use Decimal instead of float', 10.5)

引数にブーリアン値を指定
=========================================

引数にブーリアン値 (True/False) を指定すると、OpenSCAD スクリプトの true/false に変換されます。

.. code-block::

    Symbol('circle', 10, center=True)

これは以下のように OpenSCAD スクリプトに変換されます。

.. code-block::

    circle(10, center=true);

引数に文字列を指定
=====================

引数に文字列を指定すると、OpenSCAD スクリプトに変換される際にダブルクォーテーションが付きます。

.. code-block::

    Symbol('text', 'hello')

これは以下のように OpenSCAD スクリプトに変換されます。

.. code-block::

    text("hello");

引数にリストを指定
========================

引数にリストを指定することもできます。

.. code-block::

    Symbol('cube', [10, 20, 30])

これは以下のように OpenSCAD スクリプトに変換されます。

.. code-block::

    cube([10, 20, 30]);

リストの要素を小数とする場合も Decimal() を使います。

.. code-block::

    from decimal import Decimal
    Symbol('cube', [10, 20, Decimal('30.5')])

これは以下のように OpenSCAD スクリプトに変換されます。

.. code-block::

    cube([10, 20, 30.5]);

引数に numpy.ndarray を指定
============================

リスト同様に numpy.ndarray を指定することもできます。

.. code-block::

    import numpy
    v = numpy.array([10, 20, Decimal('30.5')])
    Symbol('translate', v)(
        Symbol('text', 'hello')
    )

これは以下のように OpenSCAD スクリプトに変換されます。

.. code-block::

    translate([10, 20, 30.5]) {
      text("hello");
    }

ベクトル計算をする場合に便利です。

.. code-block::

    import numpy
    v1 = numpy.array([10, 20, Decimal('30.5')])
    v2 = numpy.array([50, 60, 70])
    Symbol('translate', v1 - v2)(
        Symbol('text', 'hello')
    )

引数に `$fn` 等の `$` から始まる変数を指定する方法
==================================================

キーワード引数の引数名が `__` (アンダスコア 2個) で始まる場合は '$' に変換されます。

.. code-block::

    Symbol('circle', 10, __fn=120)

これは以下のように OpenSCAD スクリプトに変換されます。

.. code-block::

    circle(10, $fn=120);

引数名のチェックはしていません
===============================================

どんな引数名でも指定することができます。また、引数の数もチェックしていません。

.. code-block::

    Symbol('circle', gogoe=30)

この例では OpenSCAD 上では指定することができない引数名 'goegoe' を指定しています。以下のように
OpenSCAD スクリプトに変換できてしまいますが OpenSCAD で読み込んだ際にワーニングが出ます。

.. code-block::

    circle(gogoe=30);

シンボル名のチェックはしていません
========================================

どんなシンボル名でも指定することができます。

.. code-block::

    Symbol('goegoe', 10, 20)

この例では OpenSCAD 上では指定することができないシンボル名 'goegoe' を指定しています。以下のように
OpenSCAD スクリプトに変換できてしまいますが OpenSCAD で読み込んだ際にワーニングが出ます。

.. code-block::

    goegoe(10, 20);

Modifier Characters を付加
===================================

https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Modifier_Characters にも一応対応しています。

.. code-block::

    Symbol('cube', [10, 20, 30]).modify()

これは以下のように OpenSCAD スクリプトに変換されます。

.. code-block::

    #cube([10, 20, 30]);

modify() の引数に指定することにより `#` 以外も使用できます。

.. code-block::

    Symbol('cube', [10, 20, 30]).modify('%')

これは以下のように OpenSCAD スクリプトに変換されます。

.. code-block::

    %cube([10, 20, 30]);

おまけ (シンボルを print() に渡すと OpenSCAD スクリプトを出力)
===============================================================

使う機会は少ないと思いますが、Symbol クラスは __str__() メソッドで OpenSCAD
スクリプトに変換された文字列を返すので Symbol オブジェクトを
print() に渡すと変換された OpenSCAD スクリプトが表示されます。

.. code-block::

    >>> symbol = Symbol('union')()(
    ...   Symbol('difference')()(
    ...     Symbol('cube', size=30, center=True),
    ...     Symbol('sphere', r=20)
    ...   ),
    ...   Symbol('translate', [0, 0, 30])(
    ...     Symbol('cylinder', 40, r=10)
    ...   )
    ... )
    >>>
    >>> print(symbol)
    union() {
      difference() {
        cube(size=30, center=true);
        sphere(r=20);
      }
      translate([0, 0, 30]) {
        cylinder(40, r=10);
      }
    }
