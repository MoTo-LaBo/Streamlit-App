import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import time

from streamlit.elements import layouts

# page layout
st.set_page_config(
    page_title="test",
    # page_icon="🧊",
    # layout="wide",
    initial_sidebar_state="auto",
)

# title, header, subheader, text
st.title('Steamlit 基礎')
st.header('steramlit での開発')
st.subheader('strealit を実装しながら学ぶ')
st.text('「 think to build, build to think 」- つくるために考え・考えるためにつくる -')

# 画像を表示させる: pillo(上記でfrom PIL import する)
st.write('Display Image')
"""
#### 左のサイドバー(show Image) を チェック
"""

# プログレスバー (import time)
st.write('プレグレスバー')
'Start!!'

# 空の要素を追加して、空の要素を latest_iteration に入れる (object思考:python)
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)


# インタラクティブなウィジェット
if st.sidebar.checkbox('show Image'):
    img = Image.open('static/img/moto_ogp.png')
    st.image(img, caption='MoTo LaBo', use_column_width=True)

# checkbox にチェックが入っているかどうか(True or Falseを返す)
# check が入っていれば True. 入っていなければ False
# これを利用して画像を表示させるかどうかを判断させる
# if文を使用して利用できる

# select box
option = st.sidebar.selectbox(
    'あなたの好きな数字を教えて下さい',
    list(range(1, 11))
)
# write を使用しなくてもシングル or ダブルコーテーションで囲めば文字が記述できる
'あなたの好きな数字は', option, 'です'

# .sideber でサイド表示に移動できる
# text入力.スライダーによる動的変化
st.sidebar.write('Interactive Widgets')

text = st.sidebar.text_input('あなたの趣味を教えて下さい')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味:', text,
'コンディション:', condition

# 2 colum で表示する場合
left_colmun, rigiht_column = st.beta_columns(2)
button = left_colmun.button('右カラムに文字表示')
# if文 もしボタンが(True)押されたら、右カラムに(write)を表示
if button:
    rigiht_column.write('ここは右カラムです')

# expander:エクスパンダー
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# markdown,text
"""
# DataFrame
"""

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# 下記はどちらも表を表示してくれる

# write : 表サイズは変更できない
st.write(df)

# dataframe : 引数を指定する事によって表サイズを変更できる
st.dataframe(df,  width=100, height=100)

# .style.highlight_max(axis=0): 列もしくは行で最大のモノをハイライトしてくれる
# axis=0 : 列 / axis=1 : 行
st.dataframe(df.style.highlight_max(axis=0))

# table で表を表示する事ができる
st.table(df.style.highlight_max(axis=0))

# 動的な表を使用したい場合は dataframe
# 静的な表を使用したい場合は table
# 状況によって使い分ける

# マジックコマンド : markdown 記法を適用する事ができる
"""
# Markdown 記法を使用することができる
##
    import streamlit as st
    import numpy as np
    import pandas as pd
"""

# Streamlit が用意しているグラフ関数(チャートを記述)
df4 = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
df4
# 折れ線グラフでプロットする
st.line_chart(df4)
# 似たようなモノ(塗りつぶし)
st.area_chart(df4)
# 棒グラフ
st.bar_chart(df4)

"""
# Matpltlib を使用した表示
"""
fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
x = [105, 210, 301, 440, 500]
y = [10, 20, 30, 50, 60]
ax.plot(x, y)

st.pyplot(fig)

# map で表示させる
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
df3
st.map(df3)
