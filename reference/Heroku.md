# Heroku deploy
- streamlit だから必要な file もある
1. > https://docs.streamlit.io/en/stable/streamlit_faq.html?highlight=heroku
2. > https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83
- 5. Heroku deployment に詳細が載っている
3. > https://github.com/MaartenGr/streamlit_guide
- github に遷移する
- streamlit guide を作成してくれてる
- **全てはそこに記載してある**
## Heroku Command Line Interface (CLI)
> https://devcenter.heroku.com/ja/articles/heroku-cli
- install している必要がある
  - berw で登録済！！
### 1. heroku login
    heroku login
### 2. heroku ceate -a
    heroku ceate -a < app名 >
- 無料で 5つまで app を作成する事ができる
- name は一意にでないと登録できない
  - ２つ URL が表示される
  - git と heroku(git は次の登録で使用する)
### 3. git command 初期化 ~ git push
1. git int
2. git remote add heroku < 上記のgit url >
3. git add.
4. git commit -m 'first commit'
5. git push
6. git push heroku main
- 実際は github で repository を作成した時の操作方法に従う事
  - git url は heroku　登録時に表示されてものを使用
### 4. error が出た時は
    heroku logs
- まず log を見て何処でどんな error が起きているか確認する
- heroku の hp でも log は確認できる
## 必要 file
- requirements.txt
- setup.sh (shell file)
- Procfile
  - 実際には streamlit を使用しなければ、ある程度の場合では reu,Proc file だけで大丈夫
### 1. requirements.txt
- どのライブラリを使用するのかを明記する必要がある
  - pip で install するもの
  - ライブラリ名 == version
    - 何もしなければ最新版が入る(version が違うための error は出る)
### 2. setup.sh (shell file)
#### setup.sh code
    mkdir -p ~/.streamlit/

    echo "\
    [general]\n\
    email = \"your-email@domain.com\"\n\
    " > ~/.streamlit/credentials.toml

    echo "\
    [server]\n\
    headless = true\n\
    enableCORS=false\n\
    port = $PORT\n\
    " > ~/.streamlit/config.toml
- set up する為に必要な処理を記述するモノ
- email は herokuで登録したもの
### 3. Procfile
#### Procfile code
    web: sh setup.sh && streamlit run app.py
- sh setup.sh の処理を行うという意。その上で streamlit app を走らせる
- 何の file をどうやって実行すればいいのかを明記
- deploy した後に何を実行するかを記述
