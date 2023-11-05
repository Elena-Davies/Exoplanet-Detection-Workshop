#Imports
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# adding pages
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.write("Here's a sin wave")

# Get x values of the sine wave
time = np.arange(0, 10, 0.1);

# Amplitude of the sine wave is sine of a variable like time
ampltiude = np.sin(time)

# Plot a sine wave using time and amplitude obtained for the sine wave
plt.plot(time, ampltiude)