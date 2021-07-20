# pip command 一覧
> https://gammasoft.jp/python/python-library-install/#version
- Pythonのスクリプトで使用されているパッケージ（ライブラリ）やモジュールのバージョン、および、環境にインストールされているパッケージのバージョンを確認する方法
## venv 使用時は、最初に使用する package をinstallする
### pip install < package >
    # upgrade
    pip install --upgrade pip

    # jupyter lab
    pip install jupyterlab

    # streamlit
    pip install streamlit

    # matplotlib
    pip install matplotlib
### インストール済パッケージの一覧表示
    pip list
  - pip listでは以下のオプションが使える
#### 表示フォーマット（columns, freeze, jsonなど）を設定
    --format <format-name>オプション
#### 最新でないパッケージのみ一覧表示
    -o, --outdatedオプション
#### 最新のパッケージのみ一覧表示
    -u, --uptodateオプション
### インストール済パッケージの一覧表示
    pip freeze
- インストールされているパッケージの名称とバージョン番号の一覧がfreeze形式で表示される
- freeze形式の出力をテキストファイルとして保存しておくと、パッケージを指定のバージョンで一括インストールできる
> https://note.nkmk.me/python-pip-install-requirements/
- このような用途ではpipなどのパッケージ管理ツールをリストアップする必要がないので、pip freezeではデフォルトで表示されないようになっている
### インストール済パッケージの個別詳細表示
    pip show
    pip show < package name >
- 一覧ではなく特定のパッケージの詳細情報を表示したい場合はpip show < package-name >コマンドを使う。
- バージョン情報のほか、依存パッケージやホームページなどの詳細情報が表示される
### pip 自体 upgrade
    pip install --upgrade pip
