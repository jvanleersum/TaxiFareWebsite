import streamlit as st 
from datetime import datetime
import requests
import pandas as pd

st.markdown("# Taxi Fare Predictor")

st.markdown("## Let's see how much your ride will be!")

passenger_count = st.slider('Select the number of passengers', 1, 8, 2)
if passenger_count == 1:
    st.write("Just you?! Hopefully you are meeting some nice people at the dropoff")
elif passenger_count <5:
    st.write(f"{passenger_count} will easily fit in a regular taxi")
else:
    st.write(f"Woehoee, {passenger_count} is a party!")

date = st.date_input("When would you like to take the ride?")
show_date = date.strftime("%d %B, %Y")
st.write(f'Your ride will be on {show_date}')

time = st.time_input("What time will you depart?")
show_time = time.strftime('%H:%M')
st.write(f'Departure time is {show_time}')

st.markdown("### Now comes a bit of a hard part, fill in you pickup and dropoff coordinates")

pickup_longitude = st.number_input('What is the pickup longitude')
pickup_latitude = st.number_input('What is the pickup latitude')
st.write(f'The taxi will pick you up at {pickup_longitude}, {pickup_latitude}')

dropoff_longitude = st.number_input('What is the dropoff longitude')
dropoff_latitude = st.number_input('What is the dropofflatitude')
st.write(f'The taxi will pick you up at {dropoff_longitude}, {dropoff_latitude}')

st.markdown("## Alright then, let's predict the fare for this taxi ride!")

def predict_fare():
    pickup_datetime = datetime.combine(date, time)
    url = "https://taxifare.lewagon.ai/predict"
    params = {"pickup_datetime": pickup_datetime, 
              "pickup_longitude": pickup_longitude,
              "pickup_latitude": pickup_latitude,
              "dropoff_longitude": dropoff_longitude, 
              "dropoff_latitude":dropoff_latitude, 
              "passenger_count": passenger_count}
    response = requests.get(url, params=params).json()
    result = response["prediction"]
    return result

if st.button('Predict my taxi fare'):
    # print is visible in server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
    
    st.markdown("## Your taxi fare will be:")
    st.info(f"{round(predict_fare(),2)} euro's")
    
else:
    st.write('You did not click the button yet 😞')
    
    