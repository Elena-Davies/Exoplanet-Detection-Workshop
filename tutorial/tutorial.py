# Using data to create a table:

import streamlit as st
import pandas as pd
df = pd.DataFrame({'first column': [1,2,3,4],'second column':[10,20,30,40]})

df

# run streamlit
st.run https://github.com/Elena-Davies/Exoplanet-Detection-Workshop/blob/tutorial/tutorial/tutorial.py

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
chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# plotting a map
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])

st.map(map_data)

# adding widgets
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

# using checkboxes to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])

    chart_data

# using a selectbox for options
df = pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]})

option = st.selectbox('Which number do you like best?',df['first column'])

'You selected: ', option

# Adding a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))

# Adding a slider to the sidebar:
add_slider = st.sidebar.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))