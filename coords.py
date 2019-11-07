import urllib, json, datetime
import csv
import math
import os
import sys
import re
import numpy as np
import pandas as pd

class Coords:

  def load(self):

    station_csv = pd.read_csv("scan_stations.csv", sep=';')
    station_data = []
    all_data = []

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

coords = Coords()
coords.load()