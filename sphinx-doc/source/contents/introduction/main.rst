montyscad とは
--------------------

montyscad は 3D CAD モデルを Python で作成し OpenSCAD スクリプトを生成するための Python パッケージです。

サンプルプログラム
=========================

montyscad パッケージを使ったサンプルプログラムです。

.. literalinclude:: example.py
   :language: python
   :linenos:
   :caption:

OpenSCAD スクリプトを生成
===========================

[:doc:`../install/main`] を参考に montyscad パッケージがインストールされた状態で example.py を実行します。

.. code-block::

   $ python3 example.py

``example.py`` の最後の行で ``scad.write('/tmp/example.scad')`` としているので、この python プログラムを実行した時に OpenSCAD スクリプト ``/tmp/example.scad`` が生成されます。

.. literalinclude:: example.scad
   :linenos:
   :caption:

生成された ``example.scad`` を OpenSCAD で開き、作成した 3D CAD モデル の確認や STL ファイルへのエクスポート等を実施します。

.. image:: example.png

