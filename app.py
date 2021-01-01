import streamlit as st
import numpy as np
import pandas as pd
import geocoder 
from math import cos, asin, sqrt
from geopy.geocoders import Nominatim


st.title('Safe places in Hanoi & HCM City:rotating_light:')
st.header('Choose your location')
#Chọn dataset khác
file = open('C:/Users/ACER/Desktop/SA/Safe places.csv', encoding="utf8")
data = pd.read_csv (file, encoding="utf8")  
df = pd.DataFrame(data, columns= ['dis','lat','lon','city','add','name_dvtc','sdt'])


### default: địa chỉ hiện tại; nếu chọn khu vực, địa chỉ hiện tại = False
if st.checkbox('Use your current location'):
	g = geocoder.ip('me')
	lat_ad=g.latlng[0]
	lon_ad=g.latlng[1]
	def distance(lat1, lon1, lat2, lon2):
		p = 0.017453292519943295
		a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
		return 12742 * asin(sqrt(a))
	def closest(data,v):
		return min(data, key=lambda p: distance(v['lat'],v['lon'],p['lat'],p['lon']))
	v = {'lat':float(lat_ad), 'lon':float(lon_ad)}
	check_des = v
	tmp = [{'lat': df['lat'][i], 'lon': df['lon'][i]} for i in range(len(df))]
	df_end = df[(df.lat == (closest(tmp, v)['lat'])) & (df.lon == closest(tmp, v)['lon'])]
	address = g.city
	check_des = address


else :
  city_now = st.selectbox('You are in ', df.city.unique())
  dis_now = st.selectbox('', df.dis.unique())
  df_end = df[(df.city == city_now) & (df.dis == dis_now)]
  check_des = [df_end.city, df_end.dis]

st.write('Safe places near you', df_end)
st.map(df_end)

st.write('Need help? Contact for ____')
st.write('Safety steps: ')

