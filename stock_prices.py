import pandas as pd
from streamlit.util import index_
import yfinance as yf
import altair as alt
import streamlit as st

# page layout
st.set_page_config(
    page_title="stock prices",
    # page_icon="ð§",
    # layout="wide",
    initial_sidebar_state="auto",
)

st.title('ç±³å½æ ªä¾¡å¯è¦åApp')

st.sidebar.write("""
# GAFAæ ªä¾¡
ãã¡ãã¯æ ªä¾¡å¯è¦åãã¼ã«ã§ããä»¥ä¸ã®ãªãã·ã§ã³ããè¡¨ç¤ºæ¥æ°ãæå®ã§ãã¾ãã
""")

st.sidebar.write("""
## è¡¨ç¤ºæ¥æ°é¸æ
""")

days = st.sidebar.slider('æ¥æ°', 1, 50, 20)

st.write(f"""
### éå» **{days}æ¥é**ã®GAFAæ ªä¾¡
""")


@st.cache
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df


try:
    st.sidebar.write("""
    ## æ ªä¾¡ã®ç¯å²æå®
    """)
    ymin, ymax = st.sidebar.slider(
        'ç¯å²ãæå®ãã¦ä¸ãã',
        0.0, 4000.0, (0.0, 4000.0)
    )

    tickers = {
        'apple': 'AAPL',
        'facebook': 'FB',
        'google': 'GOOGL',
        'microsoft': 'MSFT',
        'netfilx': 'NFLX',
        'amazon': 'AMZN'
    }

    df = get_data(days, tickers)
    companies = st.multiselect(
        'ä¼ç¤¾åãé¸æãã¦ä¸ãã',
        list(df.index),
        ['google', 'amazon', 'facebook', 'apple']
    )

    if not companies:
        st.error('å°ãªãã¨ãä¸ç¤¾ã¯é¸ãã§ãã ãã')
    else:
        data = df.loc[companies]
        st.write('### æ ªä¾¡ (USD)', data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
            columns={'value': 'Stock Prices(USD)'}
        )

        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y('Stock Prices(USD):Q', stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color='Name:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)
except:
    st.error(
        "ã¨ã©ã¼ãèµ·ãã¦ããæ§ã§ã"
    )
