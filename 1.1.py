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

    # Add text
    st.write("The transits are used to detect exoplanets. Exoplanets are a word scientists use to refer to extrasolar planets, or planets that orbit stars outside of our solar system.")