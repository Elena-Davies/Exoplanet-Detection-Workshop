#Imports
import streamlit as st
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Use Agg
mpl.use("agg")

# adding pages
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.write("Here's a sin wave")

# Plotting sine wave
# Get x values of the sine wave
time = np.arange(0, 10, 0.1);
# Amplitude of the sine wave is sine of a variable like time
ampltiude = np.sin(time)
# Plot a sine wave using time and amplitude obtained for the sine wave
plt.plot(time, ampltiude)
# Give a title for the sine wave plot
plt.title('Sine wave')
# Give x axis label for the sine wave plot
plt.xlabel('Time (s)')
# Give y axis label for the sine wave plot
plt.ylabel('Amplitude = sin(time) (m)')
# Make the plot look presentable
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
#Display the sine wave
plt.show()