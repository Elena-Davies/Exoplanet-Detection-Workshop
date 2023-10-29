# Using data to create a table:

import streamlit as st
import pandas as pd
df = pd.DataFrame({'first column': [1,2,3,4],'second column':[10,20,30,40]})

df

# Write a data frame

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({'first column':[1,2,3,4],'second column':[10,20,30,40]}))

import numpy as np

dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

dataframe2 = pd.DataFrame(np.random.randn(10,20),columns=('col %d' % i for i in range(20)))

st.dataframe2(dataframe.style.highlight_max(axis=0))

dataframe3 = pd.DataFrame(np.random.randn(10,20),columns=('col %d' % i for i in range(20)))
st.table(dataframe3)

# Drawing a line chart

