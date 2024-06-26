# stream camera feeds
# import cv2 as cv
from streamlit_webrtc import webrtc_streamer
import streamlit as st
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

def map():
    # Initialize Nominatim API
    st.header("Map Visualization")
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode("Lagos")
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [location.latitude, location.longitude],
    columns=['lat', 'lon'])

    return st.map(map_data, size=5)


def camera_feeds():
    st.subheader("Camera feed")
    webrtc_streamer(key="streamer", sendback_audio=False)


left_col,right_col = st.columns(2)
with left_col:
    st.header("Sensor and Actuator feeds")
    camera_feeds()
    stats_view= st.container()
    stats_view.subheader("Components Stats")
    col1, col2, col3 = stats_view.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    col1,col2,col3 = stats_view.columns(3)
    col1.metric("Drone Speed", "10 m/s", "2%")
    col2.metric("Payload Volume", "10 kg", "-2%")
    col3.metric("Battery level", "90%", "-2%")


with right_col:
    map()


st.button("Deploy Parachute", type="primary")

# Get sensors stats

# Create dynamic Maps


# Host the app on streamlit






