from time import time
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pytz
import requests

'''
# TaxiFareModel front
'''

st.markdown('''Taxi Fare Prediction''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

date=st.date_input('insert the date')
time=st.time_input('Insert the time')
pickup_longitude=float(st.number_input('pick up longitude'))
pickup_latitude=float(st.number_input('pick up lattitude'))
dropoff_longitude=float(st.number_input('drop off longitude'))
dropoff_latitude=float(st.number_input('drop off lattitude'))
passenger_count=int(st.number_input('Number of Passengers'))

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://tfm-ugbzy5kqia-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

dictionary_params= {"pickup_datetime":str(date)+str(' ') +str(time),'pickup_longitude':pickup_longitude,
'pickup_latitude':pickup_latitude,'dropoff_longitude':dropoff_longitude,
'dropoff_latitude':dropoff_latitude,'passenger_count':passenger_count}


st.map(pd.DataFrame(dict(long=[pickup_longitude,dropoff_longitude]
lattitude=[pickup_latitude,dropoff_latitude])))


# 3. Let's call our API using the `requests` package...

response = requests.get(url,params=dictionary_params)






# 4. Let's retrieve the prediction from the **JSON** returned by the API...

response_from_json=response.json()

## Finally, we can display the prediction to the user

fare=response_from_json['fare']
st.write("The Fare is ",fare)