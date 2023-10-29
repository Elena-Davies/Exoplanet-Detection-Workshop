import streamlit as st
import pandas as pd
import numpy as np

# add title
st.title('Uber pickups in NYC')

# run streamlit
st.run https://raw.githubusercontent.com/Elena-Davies/Exoplanet-Detection-Workshop/tutorial/tutorial/uber_pickups.py

# Gather example data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/''streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

# inspecting the raw data
# add subheader
st.subheader('Raw data')
# print raw data
st.write(data)

# drawing histogram
#add subheader
st.subheader('Number of pickups by hour')

# using numpy to generate histogram that breaks down pickup times binned by hour:
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

# use streamlit barchart to draw the histogram
st.bar_chart(hist_values)

# plot data on a map
# add subheader
st.subheader('Map of all pickups')

# plotting the data
st.map(data)