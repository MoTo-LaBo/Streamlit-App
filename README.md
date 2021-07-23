# Streamlit App devlopmente
### 成果 App URL
> app url
### 今回作成した prototype App 一覧
### 0. 機能の挙動確認・機能一覧 App URL ↓
> https://share.streamlit.io/moto-labo/streamlit-app/main/test.py
### 1. 株価可視化 App(stock_prices.py)
> https://share.streamlit.io/moto-labo/streamlit-app/main/stock_prices.py
### 2. 物体検出 App(object_detection)
> https://share.streamlit.io/moto-labo/streamlit-app/main/object_detection.py
## Streamlit を使用して App 作成から deploy
- 作成・実装しながら streamlit を理解し、今後の App devlopment に生かす
  - python だけで web app を制作できる
  - pandas の DataFrame やグラフ、図を埋め込むことができる
  - button, slidbarといった動的な web app も作成できる
  - Streamlit sharing service を使用する事簡単に deploy できる
    - ※ GitHub との連携は必須
- Streamlit
  > https://docs.streamlit.io/en/stable/index.html
- Streamlit sharing
  > https://streamlit.io/
- Matplotlib
  > https://matplotlib.org/
- pydeck
  > https://deckgl.readthedocs.io/en/latest/
-
### {JSON} Placeholder(test API)
- test 用 API
> https://jsonplaceholder.typicode.com/
## venv で仮想環境構築&仮想環境の中へ
    python -m venv venv

    # 仮想環境へ
    source venv/bin/activate
### jupyter lab install & 起動
    pip install jupyterlab

    # jupyter lab 立ち上げ
    jupyter lab
### Streamlit install
    pip install streamlit

    pip install streamlit --upgrade
### デモを開く
    streamlit hello
- xcode や wached の install を促される
#### watchdog
     pip install watchdog
### 必要なライブラリ main.py に import して runさせる
    streamlit run < 実行したいfile >.py
- 表示されている url クリック
## pandas 1.3.0 で error 発生
    st.dataframe(df.style.highlight_max(axis=0))
- 上記の code が最新の pandas の version に対応していない。 error が発生して highlight が使用できない
### 解決方法 downgrade
> https://discuss.streamlit.io/t/getiing-an-error-after-deployment-of-streamlit-c/14674
- バージョン1.3から1.2.5にダウングレードするこの問題を解決
>https://pypi.org/project/pandas/
## Streamlit document (ドキュメント)
> https://docs.streamlit.io/en/stable/api.html#
- API reference に詳しくはのっている
## web へ deploy
- streamlit sharing は GitHub との連携ありきで使用出来るモノ
- 簡単に app を deploy 出来る
### requirements.txt 作成
- requirements.txt に今回使用している外部ライブラリーを記述する
- deploy するにあたってどんなライブラリーが使用されているかを把握しておかないと,うまく deploy できない
### pip で streamlit の version 確認
    pip freeze| grep strea

    pip freeze| grep pandas

    pip freeze| grep numpy
- requirements.txt に記述する
## 1. 株価可視化 App(stock_prices.py)
- Yahooファイナンスから株価の情報を取得
- yfinance(python library:PyPi)
> https://pypi.org/project/yfinance/
  - API の登録がないのでかなり簡単
  - yfinance を使用
## 2. 物体検出 App(object_detecation.py)
   - Azure Computer Vision 使用
     - API の KEY, ENDPOINT 管理は要注意！！
     - .gitignore は必須
     - 開発中  API : secret.json
     - deploy API : [Secrets Management]
       - >(https://www.notion.so/Secrets-Management-730c82af2fc048d383d668c4049fb9bf)
       - >https://docs.streamlit.io/en/stable/deploy_streamlit_app.html#secrets-management
## 3. 日本の賃金 data 可視化 (RESAS)
- RESAS(リーサス): 地域経済分析システム
> https://resas.go.jp/#/13/13101
  - 国民一人あたりの賃金 data を使用する
