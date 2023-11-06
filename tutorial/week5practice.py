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
st.title('Week 5 Practice')

# Define section titles
sectiontitles = ['Main Page', 'Spectra', 'Transit']

# Define section titles
def sectiontitle(number):
    return "{0}: {1}".format(number, sectiontitles[number-1])

# Define section
section = st.radio('Select section:', [1,2,3], format_func=sectiontitle)

# Write section headers
st.markdown("## {}".format(sectiontitle(section)))

if section==1:

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

    progress_bar.empty() # clear elements by calling them empty
    st.button("Re-run") # re-run animation

    st.markdown("Here is a sine wave")
    st.markdown("Sine waves are given by the equations: Asin(wt) where A is the ampltiude, w (omega) is the frequency and t is the time")

    # Get x values of the sine wave
    time = np.arange(0, 10, 0.1);

    # frequency slider
    frequency = st.slider("Value for frequency", 1, 100, 9)

    # Ampltiude of the sine wave is sine of a variable like time
    amplitude = np.sin(frequency*time)
    # Plot a sine wave using time and amplitude obtaine for the sine wave
    sinewave = plt.plot(time,amplitude)
    # savefig
    savefig = plt.savefig('sinewave.png')
    # use the non-interactive Agg backend to be more thread safe
    mpl.use("agg")
    from matplotlib.backends.backend_agg import RendererAgg
    #_lock = RendererAgg.lock

    # display the sine wave
    #with _lock:
    #    st.pyplot(sinewave)


if section==2:
    # spectra
    
    st.markdown("Here's the emission sectrum of k2-18b and several elements, match the overall spectrum to each element's spectra")

if section==3:
    # transit
    st.markdown("Here is a transit curve of k2-18b")
    st.markdown("Why is the bottom of a light curve important?")
    needhint = st.checkbox("Need a hint?", value=False)

    if needhint:
        st.markdown("Think about what the curve means, if the transit curve shows the exoplanet orbiting in front of the star")

    st.markdown("How can you see how far an exoplanet is away from its host star?")
    answer = st.checkbox("See the answer", value=False)

    if answer:
        st.markdown("You can the distance the exoplanet is from the host star if it has a long transit event. The longer the transit event, the further the exoplanet is from its host star!")
