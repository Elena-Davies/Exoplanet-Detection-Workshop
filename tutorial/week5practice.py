#Imports
import streamlit as st
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

# adding pages
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# Configure the page
st.set_page_config(page_title='Main Page', page_icon=":eyeglasses:")

# Title the app
st.title('Week 5 Practice')

sectionnames = ['Main Page', 'Spectra', 'Transit']

# Add text
st.write("Here's how a sine wave changes with time")

# Add progress bar in sidebar
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Set up empty chart
chart = st.line_chart(np.zeros(shape=(1,1)))
# x values
x = np.arange(0, 100*np.pi, 0.1)

# Animation 
for i in range(1,101):
    y = np.sin(x[i]) # y values
    status_text.text("%i%% Complete" % i)
    chart.add_rows([y]) # add each value
    progress_bar.progress(i) # when progress bar is complete show "complete"
    time.sleep(0.05)

progress_bar.empty() # when progress bar is complete, progress bar disappears or becomes empty