#Imports
import streamlit as st
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Use Agg backend to be thread safe
mpl.use("agg")

# adding pages
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# Title the app
apptitle = 'Week 5 Practice'
st.title(apptitle)

st.write("Here's a sin wave")

# Plotting sine wave
# Get x values of the sine wave
time = np.arange(0, 10, 0.1);

# Create slider
timeslider = st.select_slider('Select a value for time', options=[time])
st.write('You selected', timeslider, 'as your value for time')
# Amplitude of the sine wave is sine of a variable like time
ampltiude = np.sin(time)
# Plot a sine wave using time and amplitude obtained for the sine wave
sinewave = plt.plot(time, ampltiude)
st.pyplot(sinewave)
# Give a title for the sine wave plot
plt.title('Sine wave')
# Give x axis label for the sine wave plot
plt.xlabel('Time (s)')
# Give y axis label for the sine wave plot
plt.ylabel('Ampltiude (m)')
# Make the plot look presentable
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
