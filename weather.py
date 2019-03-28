#!/usr/local/bin/python3.7

import csv
import re

stations = []

coords = []
wcoords = []

with open('stations.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    first = True
    for row in csv_reader:
        if first:
            first = False
            continue


        if float(row[3]) < -126:
            continue
    
        length = len(row[0])

        try:
            ID = int(row[0][-5:-1])
            name = row[0][:-6]
        except:
            ID = int(row[0][-4:-1])
            name = row[0][:-5]
        station = {
            "id": ID,
            "name": name,
            "startDate": row[1],
            "lat": row[2],
            "lng": row[3],
        }
        stations.append(station)

        coords.append( [float(row[3]), float(row[2])] )


with open('weather_stations.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    first = True
    for row in csv_reader:
        try: 
            wcoords.append( [float(row[1]), float(row[2]) ])
        except:
            print(row[0])



# Plot coords
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(coords)

voronoi_plot_2d(vor, show_vertices=False, line_colors='black', line_width=.5, line_alpha=1, point_size=10)
for point in wcoords:
    plt.plot(point[1], point[0], '.y')
plt.show()
