#Imports
import streamlit as st
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

# adding pages
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# Title the app
apptitle = 'Week 5 Practice'
st.title(apptitle)

st.write("Here's how a sine wave changes with time")

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

chart = st.line_chart(np.zeros(shape=(1,1)))
x = np.arange(0, 100*np.pi, 0.1)

for i in range(1,101):
    y = np.sin(x[i])
    status_text.text("%i%% Complete" % i)
    chart.add_rows([y])
    progress_bar.progress(i)
    time.sleep(0.05)

progress_bar.empty()