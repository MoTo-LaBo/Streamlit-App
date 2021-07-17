# Streamlit 基礎
- 今回使用する directory を作成
### 1.venv で仮想環境構築&仮想環境の中へ
    python -m venv venv

    # 仮想環境へ
    source venv/bin/activate
### 2. jupyter lab install & 起動
    pip install jupyterlab

    # jupyter lab 立ち上げ
    jupyter lab
### 3. Streamlit install
    pip install streamlit
### 4. デモを開く
    streamlit hello
- xcode や wached の install を促される
#### watchdog
     pip install watchdog
### 5. 必要なライブラリ main.py に import して runさせる
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
- requirements.txt に記述する
