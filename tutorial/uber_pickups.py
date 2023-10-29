import streamlit as st
import pandas as pd
import numpy as np

# add title
st.title('Uber pickups in NYC')

# run streamlit
st.run https://github.com/Elena-Davies/Exoplanet-Detection-Workshop/blob/tutorial/tutorial/uber_pickups.py

# Gather example data

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data