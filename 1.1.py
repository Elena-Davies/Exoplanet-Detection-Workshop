#Imports
import streamlit as st
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

# use the non-interactive Agg backend to be more thread safe
#mpl.use("agg")
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock

# adding pages
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# Title the app
st.title('A-Level Workshop: Transit Method')

# Define section titles
sectiontitles = ['Main Page', 'Transit Method', 'Spectra', 'Transit Curves']
# Define section titles function
def sectiontitle(number):
    return "{0}: {1}".format(number, sectiontitles[number-1])

# Define section
section = st.radio('Select section:', [1,2,3,4], format_func=sectiontitle)

# Write section headers
st.markdown("## {}".format(sectiontitle(section)))

if section==1:
#main page

    # Add text
    st.write("Transits are used to detect exoplanets. Exoplanets are a word scientists use to refer to extrasolar planets, or planets that orbit stars outside of our solar system. Click on the Transit Method section to learn more!")
    st.markdown("The transit method works by measuring the dimming effect that takes place when a planet passes in front of its host star. Scientists analyse this dimming effect in light curves which are graphs that show the light received over a period of time. Click on the light curve section to learn more about them!")
    st.write("Stars emit as blackbodies, meaning they emit all wavelengths. A star's and exoplanet's atmosphere can be discovered by analysing the emission spectra of the star as seen from Earth. Click on the Spectra section to find out more!")

if section==2:
    # transit method

    

if section==3:
    # spectra
    
    st.markdown("Here's the emission spectrum of an exoplanet K2-18b")