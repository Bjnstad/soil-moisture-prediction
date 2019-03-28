#!/usr/local/bin/python3.7

import csv
import re

stations = []

coords = []


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

        coords.append([float(row[3]), float(row[2])])

print(stations[3])


from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(coords)


import matplotlib.pyplot as plt


voronoi_plot_2d(vor)
plt.show()
