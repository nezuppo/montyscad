インストール
----------------------

以下の環境で montyscad を使えるようにするためのインストール手順を記載します。

- Ubuntu 20.04.3 LTS
- Python 3.8.10

その他の環境では試していませんが、Ubuntu + Python3 系であれば同じ手順で問題ないかと思われます。

依存パッケージをインストール
==========================================

montyscad には numpy が必要なのでインストール ::

    $ sudo apt install python3-numpy

montyscad をインストール
====================================

montyscad リポジトリの中の montyscad ディレクトリ (Python パッケージ) を
python のモジュール検索パスが通っているディレクトリに置くだけです。

以下のようにカレントディレクトリに置く方法が簡単です。

GitHub の montyscad リポジトリをテンポラリなディレクトリに clone ::

    $ git clone https://github.com/nezuppo/montyscad.git ./tmp-montyscad-repo/

clone 先として ``./tmp-montyscad-repo/`` を指定しているので、このディレクトリに clone されます。 ::

    $ ls -la
    total 12
    drwxr-xr-x 3 test test 4096 Sep 24 21:51 .
    drwxr-xr-x 3 test test 4096 Sep 24 20:49 ..
    drwxr-xr-x 5 test test 4096 Sep 24 21:51 tmp-montyscad-repo

リポジトリの montyscad ディレクトリ (Python パッケージ) をカレントディレクトリにコピー ::

    $ cp -r tmp-montyscad-repo/montyscad ./

カレントディレクトリは以下の状態となります。 ::

    $ ls -la
    total 16
    drwxr-xr-x 4 test test 4096 Sep 24 21:53 .
    drwxr-xr-x 3 test test 4096 Sep 24 20:49 ..
    drwxr-xr-x 2 test test 4096 Sep 24 21:53 montyscad
    drwxr-xr-x 5 test test 4096 Sep 24 21:51 tmp-montyscad-repo

以上によりカレントディレクトリで montyscad パッケージが使えるようになるので
[:doc:`../introduction/main`] で紹介した example.py のように montyscad
を使った Python スクリプトで 3D CAD モデル を作成することができます。
