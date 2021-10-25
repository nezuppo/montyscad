monty_symbols モジュールについて
----------------------------------

執筆中です。しばらくお待ち下さい。

.. ::

    monty_symbols モジュールには OpenSCAD の circle や cube , linear_extrude, translate
    等に対応したクラスが含まれています。

    これらのクラスは Symbol クラスから派生しています。

    含まれているクラス
    ========================

    クラスは `monty_symbols.py` の `_symbol_names` で定義されています。2021/10/23 現在の定義は以下の通りです。(少しずつ追加していく予定です)

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
