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
    # page_icon="ð§",
    # layout="wide",
    initial_sidebar_state="auto",
)

# ãã­ã°ã¬ã¹ãã¼ (import time)
# ç©ºã®è¦ç´ ãè¿½å ãã¦ãç©ºã®è¦ç´ ã latest_iteration ã«å¥ãã (objectæè:python)
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
st.write('start!!!')


# title, header, subheader, text
st.title('Streamlit åºç¤')
st.header('streramlit ã§ã®éçº')
st.subheader('streamlit ãå®è£ããªããå­¦ã¶')
st.text('ã think to build, build to think ã- ã¤ããããã«èãã»èããããã«ã¤ãã -')

"""
### (show Image) ã ãã§ãã¯ããã¨ç»åãè¡¨ç¤ºããã¾ã
"""

# ç»åãè¡¨ç¤ºããã: pillo(ä¸è¨ã§from PIL import ãã)
# ã¤ã³ã¿ã©ã¯ãã£ããªã¦ã£ã¸ã§ãã
if st.checkbox('show Image'):
    img = Image.open('static/img/moto_ogp.png')
    st.image(img, caption='MoTo LaBo', use_column_width=True)

# checkbox ã«ãã§ãã¯ãå¥ã£ã¦ãããã©ãã(True or Falseãè¿ã)
# check ãå¥ã£ã¦ããã° True. å¥ã£ã¦ããªããã° False
# ãããå©ç¨ãã¦ç»åãè¡¨ç¤ºããããã©ãããå¤æ­ããã
# ifæãä½¿ç¨ãã¦å©ç¨ã§ãã

# radio button
option_radio = st.sidebar.radio(
    "å¥½ããªæç©ãæãã¦ä¸ãã",
    ('ãã¹ã«ãã', 'ç¡è±æ', 'æ¡', 'ææ·', 'æ¢¨')
)
st.write('ããªããé¸ãã æç©ã¯:', option_radio)


# select box
option = st.sidebar.selectbox(
    'ããªãã®å¥½ããªæ°å­ãæãã¦ä¸ãã',
    list(range(1, 11))
)
# write ãä½¿ç¨ããªãã¦ãã·ã³ã°ã« or ããã«ã³ã¼ãã¼ã·ã§ã³ã§å²ãã°æå­ãè¨è¿°ã§ãã
'ããªãã®å¥½ããªæ°å­ã¯', option, 'ã§ã'

# .sideber ã§ãµã¤ãè¡¨ç¤ºã«ç§»åã§ãã
# textå¥å.ã¹ã©ã¤ãã¼ã«ããåçå¤å
text = st.sidebar.text_input('ããªãã®è¶£å³ãæãã¦ä¸ãã')
condition = st.sidebar.slider('ããªãã®ä»ã®èª¿å­ã¯ï¼', 0, 100, 50)

'ããªãã®è¶£å³:', text,
'ã³ã³ãã£ã·ã§ã³:', condition

# slider
values = st.slider(
    'æ°å¤ã®ç¯å²ãæå®ãã¦ãã ãã',
    0.0, 100.0, (25.0, 75.0))
st.write('values:', values)

# multiselect
options = st.multiselect(
    'èå³ããè¨èªãé¸æãã¦ä¸ãã',
    ['Python', 'Go', 'JavaScript', 'Ruby', 'C', 'C++', 'R'],
    ['Python', 'Go'])


# expander:ã¨ã¯ã¹ãã³ãã¼
expander = st.beta_expander('åãåãã')
expander.write('åãåããåå®¹ãæ¸ã')

# 2 colum ã§è¡¨ç¤ºããå ´å
left_colmun, rigiht_column = st.beta_columns(2)
button = left_colmun.button('å³ã«ã©ã ã«æå­è¡¨ç¤º')
# ifæ ãããã¿ã³ã(True)æ¼ãããããå³ã«ã©ã ã«(write)ãè¡¨ç¤º
if button:
    rigiht_column.write('ããã¯å³ã«ã©ã ã§ã')


# markdown,text
"""
# DataFrame
### ãã¿ã³ãæ¼ãããã¨DataFrameãè¡¨ç¤ºããã¾ã
"""

# button
option_button = st.button('ãã¿ã³')

if option_button == True:

    df = pd.DataFrame({
        '1åç®': [1, 2, 3, 4],
        '2åç®': [10, 20, 30, 40]
    })
    # write : è¡¨ãµã¤ãºã¯å¤æ´ã§ããªã
    st.write(df)

    # dataframe : å¼æ°ãæå®ããäºã«ãã£ã¦è¡¨ãµã¤ãºãå¤æ´ã§ãã
    st.dataframe(df,  width=100, height=100)

    # .style.highlight_max(axis=0): åãããã¯è¡ã§æå¤§ã®ã¢ãããã¤ã©ã¤ããã¦ããã
    # axis=0 : å / axis=1 : è¡
    st.dataframe(df.style.highlight_max(axis=0))

    # table ã§è¡¨ãè¡¨ç¤ºããäºãã§ãã
    st.table(df.style.highlight_max(axis=0))
else:
    st.write('ãã¿ã³ãæ¼ãã¦ãã ãã')


# åçãªè¡¨ãä½¿ç¨ãããå ´åã¯ dataframe
# éçãªè¡¨ãä½¿ç¨ãããå ´åã¯ table
# ç¶æ³ã«ãã£ã¦ä½¿ãåãã

# ãã¸ãã¯ã³ãã³ã : markdown è¨æ³ãé©ç¨ããäºãã§ãã
"""
# Markdown è¨æ³ãä½¿ç¨ãããã¨ãã§ãã
##
    import streamlit as st
    import numpy as np
    import pandas as pd
"""

# Streamlit ãç¨æãã¦ããã°ã©ãé¢æ°(ãã£ã¼ããè¨è¿°)
df4 = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
df4
# æãç·ã°ã©ãã§ãã­ãããã
st.line_chart(df4)
# ä¼¼ããããªã¢ã(å¡ãã¤ã¶ã)
st.area_chart(df4)
# æ£ã°ã©ã
st.bar_chart(df4)

"""
# Matpltlib ãä½¿ç¨ããè¡¨ç¤º
"""
fig = plt.figure(figsize=(10, 5))
ax = plt.axes()
x = [105, 210, 301, 440, 500]
y = [10, 20, 30, 50, 60]
ax.plot(x, y)

st.pyplot(fig)

# æ±äº¬çåºæå¨å° data plot : ç·¯åº¦è»½åº¦ãå®ç¾©
"""
# æ±äº¬çåºæå¨å°ãä»è¿
"""
tokyo_lat = 35.69  # ç·¯åº¦:latitude
tokyo_lon = 139.69  # çµåº¦:longitude

df_tokyo = pd.DataFrame(
    np.random.randn(1000, 2)/[50, 50]+[tokyo_lat, tokyo_lon],
    columns=['lat', 'lon']
)

df_tokyo

st.map(df_tokyo)

"""
# 3D Maping
"""
# 1. view ã®è¨­å®ï¼å°å³ä¸ã®å ´æ(ç·¯åº¦ã»çµåº¦)ãè¦ãè§åº¦
view = pdk.ViewState(latitude=tokyo_lat, longitude=tokyo_lon, pitch=50, zoom=11)

# 2. Layer è¨­å® : ã©ã®å¯è¦åæ¹æ³ã«ããã®ããæå®
hexagon_layer = pdk.Layer('HexagonLayer',  # Layer æå®
                          data=df_tokyo,  # pd data
                          get_position=['lon', 'lat'],  # ä½ç½®æå ±ãè¡¨ãç·¯åº¦çµåº¦ã®ååï¼lon,latã®é çªã§ãªãã¨errorã«ãªãï¼
                          elevation_scale=6,  # extruded ã® scale ã®é«ããå¤æ´ã§ãã
                          radius=100,  # extruded ã®åå¾æå®
                          extruded=True  # æ£ã®é«ãæç¡ã
                          )

# 3. Deck : view,Layer æå ±ãå¼æ°ã«æå®ã map ã«ã¬ã³ãã³ãªã³ã°ãã
layer_map = pdk.Deck(layers=hexagon_layer, initial_view_state=view)  # åã« Layer

st.pydeck_chart(layer_map)
