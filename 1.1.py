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
    
    # Plot the planet around the star in a circular orbit
    # Constants
    G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
    M_star = 0.36*(2e3)  # Mass of the star (kg)
    M_planet = 0.0281*1.898e27  # Mass of the planet (kg)
    AU = 1.496e11  # Astronomical unit (m)

    # Initial conditions
    a = 0.143 * AU  # Semi-major axis (m)
    period = np.sqrt((4 * np.pi**2 * a**3) / (G * (M_star + M_planet)))  # Orbital period (s)
    eccentricity = 0.2  # Eccentricity of the orbit
    theta = np.linspace(0, 2 * np.pi, 1000)  # Angular positions

    # Orbital motion equations
    r = a * (1 - eccentricity**2) / (1 + eccentricity * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot the orbit
    with _lock:
        fig=plt.figure(figsize=(8, 8))
        orbit=plt.plot(x, y, label='Orbit')
        star=plt.scatter([0], [0], color='yellow', marker='o', label='Star')  # Star
        planet=plt.scatter([x[0]], [y[0]], color='red', marker='o', label='Planet')  # Initial position of the planet
        plt.title('K2-18 b Orbit')
        plt.xlabel('X-axis (m)')
        plt.ylabel('Y-axis (m)')
        plt.legend()
        plt.axis('equal')
        st.pyplot(fig)

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

    # Enter the parameters needed by the model
     rp = 14271000 #radius of planet in metres
     sma = 21380000000 #semi-major axis in metres
     rs = 0.41*696340000 #radius of star in metres
     t0 = 0.                        #time of inferior conjunction in days
     per = 32.9                     #orbital period in days
     rp_rs = rp/rs              #planet radius / stellar radius ratio
     ars = 74.947                    #semi-major axis / stellar radius ratio
     inc =  (89.58*u.deg).to(u.rad).value      #orbital inclination (in radians) using astropy to convert to radians
     ecc = 0.09                       #eccentricity
     w = (-5.70*u.deg).to(u.rad).value      #longitude of periastron (in radians)
     gamma = [1.6800, 1.1390]                 #limb darkening coefficients [u1, u2]
     t = np.linspace(-0.05, 0.05, 1000)  #times at which to calculate light curve (days)

     # Now instantiate an instance of the QuadraticModel class object, and enter the timegrid into the object
     tm = QuadraticModel() # a model that uses two limb-darkening coefficients
     tm.set_data(t)

    # Add progress bar in sidebar
     progress_bar = st.sidebar.progress(0)
     status_text = st.sidebar.empty()

# Set up empty chart
     chart = st.line_chart(np.zeros(shape=(1,1)))
    # x values
     x = np.arange(0, 100*np.pi, 0.1)

     # Plot light curve
     lc  = tm.evaluate(k=rp_rs, ldc=gamma, t0=t0, p=per, a=ars, i=inc, e=ecc, w=w)
     plt.figure('lc')
     plt.plot(t,lc, '-o')
     plt.grid(True)
     plt.ylabel('Relative signal')
     plt.xlabel('Time (days)')
     plt.show();

     # Animation 
     for i in range(1,101):
        y = lc # y values
        status_text.text("%i%% Complete" % i)
        chart.add_rows([y]) # add each value
        progress_bar.progress(i) # when progress bar is complete show "complete"
        time.sleep(0.05)

     progress_bar.empty() # clear elements by calling them empty
     st.button("Re-run") # re-run animation