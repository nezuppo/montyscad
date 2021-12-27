monty_symbols モジュールについて
----------------------------------

monty_symbols モジュールには OpenSCAD の circle や cube , linear_extrude, translate
等に対応したクラスが含まれています。

これらのクラスは Symbol クラスから派生しています。

含まれているクラス
========================

クラスは `monty_symbols.py` の `_symbol_names` で定義されています。2021/12/27 現在の定義は以下の通りです。(少しずつ追加していく予定です)

.. code-block::

    _symbol_names = [
        'circle',
        'color',
        'cube',
        'cylinder',
        'difference',
        'intersection',
        'linear_extrude',
        'import',
        'minkowski',
        'mirror',
        'offset',
        'projection',
        'rotate',
        'sphere',
        'square',
        'translate',
        'union',
    ]

ここに含まれていないものについては Symbol クラスを使います。[:doc:`../symbol_class/main`] を参照して下さい。

使い方を Symbol クラスと比較
==============================

translate、cube を例にとります。

まず Symbol クラスを使う場合は以下のようになります。

.. code-block::

    from montyscad import Symbol

    Symbol('translate', [1, 2, 3])(
        Symbol('cube', [10, 10, 10])
    )

同じことを monty_symbols を使う場合は以下のようになります。

.. code-block::

    from montyscad import monty_symbols as ms

    ms.translate([1, 2, 3])(
        ms.cube([10, 10, 10])
    )

このように monty_symbols を使うと Symbol クラスを使う場合と比べタイピング時の文字数が減り、
コーディングについても OpenSCAD スクリプトにより近いものとなります。
