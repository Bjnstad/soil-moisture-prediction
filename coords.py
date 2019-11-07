import urllib, json, datetime
import csv
import math
import os
import sys
import re
import numpy as np
import pandas as pd

class Coords:

  def load_scan(self):

    station_csv = pd.read_csv("scan_stations.csv", sep=';')
    station_data = []

    for index, row in station_csv.iterrows():

      stationid = str(row['Name'])

      cleanid = ''.join(i for i in stationid if i.isdigit())
      lat = float(row['Lat'])
      lng = float(row['Long'])

      station_data.append({
        "stationid": cleanid,
        "lat": lat,
        "lng": lng
      })
    
    print(station_data)



  def load_weather(self):

      station_csv = pd.read_csv("weather_stations.csv", sep=';')
      weather_station_data = []

      for index, row in station_csv.iterrows():

        weatherid = str(row[0])
        lat = row[2]
        lng = row[3]

        weather_station_data.append({
          "weatherStationid": weatherid,
          "lat": lat,
          "lng": lng
        })
      
      print(weather_station_data)




coords = Coords()
coords.load_weather()
# coords.load_scan()