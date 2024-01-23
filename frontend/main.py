import streamlit as st
import pandas as pd
import numpy as np

# Set page config (Shows on tab info)
st.set_page_config(
    page_title="꿀벌 농장",
    page_icon="🐝",
    layout="wide",
)

# main title
st.title('🐝 꿀벌 농장 🐝')

# chart data example1
chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

chart_data2 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

chart_data3 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


# 3 개의 열로 나누기
topic_col1, topic_col2, topic_col3 = st.columns(3)

with topic_col1:
    st.write('오늘의 꿀벌 총 양')
    st.line_chart(chart_data, x="col1", y="col2", color="col3")

with topic_col2:
    st.write('오늘의 기온')
    st.bar_chart(chart_data2)

with topic_col3:
    st.write('오늘의 오늘의 습도')
    st.area_chart(chart_data3)


# 2 개의 열로 나누기


import streamlit as st
import pydeck as pdk

# Map of South Korea
map_data = pd.DataFrame({'lat': [35.9078], 'lon': [127.7669]})
view_state = pdk.ViewState(latitude=map_data['lat'].mean(), longitude=map_data['lon'].mean(), zoom=6)

layer = pdk.Layer(
    "ScatterplotLayer",
    map_data,
    get_position='[lon, lat]',
    get_radius=50000,
    get_color=[200, 30, 0, 160],
    pickable=True,
    auto_highlight=True
)

map = pdk.Deck(map_style='mapbox://styles/mapbox/light-v9', initial_view_state=view_state, layers=[layer])

st.pydeck_chart(map)