import streamlit as st

view = [100, 150, 30]
st.write('#  Youtube view')
st.write('###  ※raw data')
st.write(view)

st.write('###  ※bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
st.write('###  ※This is pure data')
st.write(view)
st.write("""
### ※This is data processed by pandas
### &nbsp;&nbsp;&nbsp;[This is data that pandas processes]
""")
st.write(sview)