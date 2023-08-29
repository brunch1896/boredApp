import streamlit as st
import requests

st.title('🏀 双胖周末做什么？')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('双胖是谁'):
    st.write('很简单，就是乐胖和鸿胖~')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)

st.header('建议的活动')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='参与人数', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='活动类型', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='价格', value=suggested_activity['price'], delta='')
