from altair.vegalite.v4.api import layer
from altair.vegalite.v4.schema.channels import Opacity, Y
import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk
import plotly.express as px


st.title('日本の賃金データDASH')

# ----- Data source -----
df_jp_ind = pd.read_csv('./analysis_jp_wage/csv_data/雇用_医療福祉_一人当たり賃金_全国_全産業.csv', encoding='shift_jis')
df_jp_category = pd.read_csv('./analysis_jp_wage/csv_data/雇用_医療福祉_一人当たり賃金_全国_大分類.csv', encoding='shift_jis')
df_pref_ind = pd.read_csv('./analysis_jp_wage/csv_data/雇用_医療福祉_一人当たり賃金_都道府県_全産業.csv', encoding='shift_jis')


# ----- DataFrame1 -----
st.header('・ 2019年 : 一人当たり平均賃金のヒートマップ')
# 県庁所在地：緯度・経度
jp_lat_lon = pd.read_csv('./analysis_jp_wage/pref_lat_lon.csv')
# en -> jp 列名の変更
jp_lat_lon = jp_lat_lon.rename(columns={'pref_name': '都道府県名'})

# 作成 -> 結合 -> 正規化処理(最小値0,最大値１とする)
# 正規化処理 -> Y = (X-Xmin)/(Xmax-Xmin)
# (相対値):の丸括弧は全角。半角だとpydeck の layer 設定で error
df_pref_map = df_pref_ind[(df_pref_ind['年齢'] == '年齢計') & (df_pref_ind['集計年'] == 2019)]
df_pref_map = pd.merge(df_pref_map, jp_lat_lon, on='都道府県名')
df_pref_map['一人当たり賃金（相対値）'] = ((df_pref_map['一人当たり賃金（万円）']-df_pref_map['一人当たり賃金（万円）'].min())/(df_pref_map['一人当たり賃金（万円）'].max()-df_pref_map['一人当たり賃金（万円）'].min()))


# ----- pydeck Heatmap -----
# 今回は大阪中心
view = pdk.ViewState(
    longitude=135.518992,
    latitude=34.686492,
    # longitude=139.691648,
    # latitude=35.689185,
    zoom=4,
    pitch=40.5,  # 見る角度
)

layer = pdk.Layer(
    "HeatmapLayer",                    # マップの種類
    data=df_pref_map,
    opacity=0.4,                       # 地図透明度
    get_position=['lon', 'lat'],       # 経度,緯度の順番
    threshold=0.3,                     # ヒートマップの場合にどこの値をしきい値にするのか
    get_weight='一人当たり賃金（相対値）'  # どこの列をとるか
)

layer_map = pdk.Deck(                 # Deck method : レンダリング (layer,view)を引数に入れる
    layers=layer,
    initial_view_state=view
)

st.pydeck_chart(layer_map)  # Streamlit での Map 表示

# check box の有無で DataFrame 表示させる
show_df = st.checkbox('Show DataFrame')
if show_df == True:
    st.write(df_pref_map)


# ----- DataFrame2 -----
st.header('・集計年別の一人当たり賃金（万円）の推移')

df_ts_mean = df_jp_ind[(df_jp_ind['年齢'] == '年齢計')]
df_ts_mean = df_ts_mean.rename(columns={'一人当たり賃金（万円）': '全国_一人当たり賃金（万円）'})

df_pref_mean = df_pref_ind[(df_pref_ind['年齢'] == '年齢計')]
pref_list = df_pref_mean['都道府県名'].unique()
option_pref = st.selectbox(
    '都道府県名',
    (pref_list)
)
df_pref_mean = df_pref_mean[df_pref_mean['都道府県名'] == option_pref]

# 上記の２つの DataFrame を結合する
# pandas method merge : 結合するものを引数に入れる, on=
df_mean_line = pd.merge(df_ts_mean, df_pref_mean, on='集計年')
df_mean_line = df_mean_line[['集計年', '全国_一人当たり賃金（万円）', '一人当たり賃金（万円）']]
df_mean_line = df_mean_line.set_index('集計年')
# 折れ線グラフで表示
st.line_chart(df_mean_line)


# ----- DataFrame3 Bubble chart -----
st.header('・年齢階級別の全国一人当たり平均賃金（万円）')

# 年齢を年齢計に絞る
df_mean_bubble = df_jp_ind[df_jp_ind['年齢'] != '年齢計']

# x:一人当たりの賃金. y:賞与. z(bubble):所定内給与額
fig = px.scatter(df_mean_bubble,                 # 最初の引数に DataFrame 指定
                 x='一人当たり賃金（万円）',
                 y='年間賞与その他特別給与額（万円）',
                 range_x=[150, 700],
                 range_y=[0, 150],
                 size='所定内給与額（万円）',
                 size_max=38,                    # 指定しなくても default で　scale 指定してくれる
                 color='年齢',
                 animation_frame='集計年',
                 animation_group='年齢'
                 )
# plotly express で表示
st.plotly_chart(fig)


# ----- DataFrame4  -----
st.header('・産業別の賃金推移')

# 列を集計年に集中させる -> selectbox で選択させる
year_list = df_pref_ind['集計年'].unique()
option_year = st.selectbox(
    '集計年',
    (year_list)
)

# 賃金の種類 -> list -> selectbox
wage_list = ['一人当たり賃金（万円）', '所定内給与額（万円）', '年間賞与その他特別給与額（万円）']
option_wage = st.selectbox(
    '賃金の種類',
    (wage_list)
)

# selectbox の情報を条件抽出する
df_mean_categ = df_jp_category[(df_jp_category['集計年'] == option_year)]

# 選択された賃金によって最大値を取得
# 選択された列の最大値を max_x に格納する事によって、自動で賃金種類によっての最大値が求まる
max_x = df_mean_categ[option_wage].max() + 50  # margin:見やすいように

# plotly bar:折れ線グラフ
fig = px.bar(df_mean_categ,         # 最初の引数に DataFrame 指定
             x=option_wage,         # selectbox で選択されたモノによって変わる
             y='産業大分類名',
             color='産業大分類名',
             animation_frame='年齢',
             range_x=[0, max_x],    # selectbox で選択されたモノによって変わる
             orientation='h',       # 横棒グラフ表示に設定するモノ
             width=800,             # 指定しない場合は default の値が入る
             height=500             # 指定しない場合は default の値が入る
             )
st.plotly_chart(fig)

# open data を使用する場合は data の出典もとは必ず記載する
st.text('出典：RESAS（地域経済分析システム）')
st.text('本結果はRESAS（地域経済分析システム）を加工して作成')
