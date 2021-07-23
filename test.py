from pydeck.bindings import layer
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import time
import pydeck as pdk

from streamlit.elements import layouts

# page layout
st.set_page_config(
    page_title="test",
    # page_icon="🧊",
    # layout="wide",
    initial_sidebar_state="auto",
)

# プログレスバー (import time)
# 空の要素を追加して、空の要素を latest_iteration に入れる (object思考:python)
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
st.write('start!!!')


# title, header, subheader, text
st.title('Streamlit 基礎')
st.header('streramlit での開発')
st.subheader('streamlit を実装しながら学ぶ')
st.text('「 think to build, build to think 」- つくるために考え・考えるためにつくる -')

"""
### (show Image) を チェックすると画像が表示されます
"""

# 画像を表示させる: pillo(上記でfrom PIL import する)
# インタラクティブなウィジェット
if st.checkbox('show Image'):
    img = Image.open('static/img/moto_ogp.png')
    st.image(img, caption='MoTo LaBo', use_column_width=True)

# checkbox にチェックが入っているかどうか(True or Falseを返す)
# check が入っていれば True. 入っていなければ False
# これを利用して画像を表示させるかどうかを判断させる
# if文を使用して利用できる

# radio button
option_radio = st.sidebar.radio(
    "好きな果物を教えて下さい",
    ('マスカット', '無花果', '桃', '枇杷', '梨')
)
st.write('あなたが選んだ果物は:', option_radio)


# select box
option = st.sidebar.selectbox(
    'あなたの好きな数字を教えて下さい',
    list(range(1, 11))
)
# write を使用しなくてもシングル or ダブルコーテーションで囲めば文字が記述できる
'あなたの好きな数字は', option, 'です'

# .sideber でサイド表示に移動できる
# text入力.スライダーによる動的変化
text = st.sidebar.text_input('あなたの趣味を教えて下さい')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味:', text,
'コンディション:', condition

# slider
values = st.slider(
    '数値の範囲を指定してください',
    0.0, 100.0, (25.0, 75.0))
st.write('values:', values)

# multiselect
options = st.multiselect(
    '興味ある言語を選択して下さい',
    ['Python', 'Go', 'JavaScript', 'Ruby', 'C', 'C++', 'R'],
    ['Python', 'Go'])


# expander:エクスパンダー
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# 2 colum で表示する場合
left_colmun, rigiht_column = st.beta_columns(2)
button = left_colmun.button('右カラムに文字表示')
# if文 もしボタンが(True)押されたら、右カラムに(write)を表示
if button:
    rigiht_column.write('ここは右カラムです')


# markdown,text
"""
# DataFrame
### ボタンが押されるとDataFrameが表示されます
"""

# button
option_button = st.button('ボタン')

if option_button == True:

    df = pd.DataFrame({
        '1列目': [1, 2, 3, 4],
        '2列目': [10, 20, 30, 40]
    })
    # write : 表サイズは変更できない
    st.write(df)

    # dataframe : 引数を指定する事によって表サイズを変更できる
    st.dataframe(df,  width=100, height=100)

    # .style.highlight_max(axis=0): 列もしくは行で最大のモノをハイライトしてくれる
    # axis=0 : 列 / axis=1 : 行
    st.dataframe(df.style.highlight_max(axis=0))

    # table で表を表示する事ができる
    st.table(df.style.highlight_max(axis=0))
else:
    st.write('ボタンを押してください')


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

# 東京県庁所在地 data plot : 緯度軽度を定義
"""
# 東京県庁所在地　付近
"""
tokyo_lat = 35.69  # 緯度:latitude
tokyo_lon = 139.69  # 経度:longitude

df_tokyo = pd.DataFrame(
    np.random.randn(1000, 2)/[50, 50]+[tokyo_lat, tokyo_lon],
    columns=['lat', 'lon']
)

df_tokyo

st.map(df_tokyo)

"""
# 3D Maping
"""
# 1. view の設定：地図上の場所(緯度・経度)、見る角度
view = pdk.ViewState(latitude=tokyo_lat, longitude=tokyo_lon, pitch=50, zoom=11)

# 2. Layer 設定 : どの可視化方法にするのかを指定
hexagon_layer = pdk.Layer('HexagonLayer',  # Layer 指定
                          data=df_tokyo,  # pd data
                          get_position=['lon', 'lat'],  # 位置情報を表す緯度経度の列名（lon,latの順番でないとerrorになる）
                          elevation_scale=6,  # extruded の scale の高さを変更できる
                          radius=100,  # extruded の半径指定
                          extruded=True  # 棒の高さ有無か
                          )

# 3. Deck : view,Layer 情報を引数に指定。 map にレンダンリングする
layer_map = pdk.Deck(layers=hexagon_layer, initial_view_state=view)  # 先に Layer

st.pydeck_chart(layer_map)
