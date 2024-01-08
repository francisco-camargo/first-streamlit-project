'''
Run in terminal with
    streamlit run main.py
'''
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.header('my st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# Ex 1
st.write('Hello *World!* :sunglasses:')

# Ex 2
st.write(1234)

# Ex 3
df = pd.DataFrame(
    {
        'first col': [1, 23, 4, 2],
        'second col': [10, 40, 2, 1],
    }
)
st.write(df)

# Ex 4
st.write('below is df', df, 'above is df')

# Ex 5
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'],
)
chart = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
)
st.write(chart)
