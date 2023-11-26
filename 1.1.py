#Imports
import streamlit as st
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

#Import PyTransit and some key modules.
from pytransit import QuadraticModel # use this for the quadratic limb-darkening law
# from pytransit import UniformModel
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy import constants as const

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
    st.markdown("# What is the transit method?")
    st.write("When exoplanets (planets that orbit stars outside of our solar system) pass in front of their host star as seen from Earth, a portion of the star light is blocked out!")
    
    st.markdown("# Pros")
    st.write("A big advantage for using the transit method is that the size of the planet can be determined from a light curve (more about this in the light curve section!)")
    
    st.markdown("# Cons")
    st.write("However, the downside to the transit method is that it only works for star-planet systems that have orbits aligned that when we see it from Earth, the planet travels between us and the star.")
    
if section==3:
    # spectra
    
    st.markdown("Here's the emission spectrum of an exoplanet K2-18b")

if section==4:
    # transit curve
     st.markdown("Here is a transit curve of an exoplanet K2-18b")