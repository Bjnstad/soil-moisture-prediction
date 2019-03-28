from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import load

# Delacare station variables
moisture_stations = []
weather_stations = []

# Load stations from static csv
load.moisture(moisture_stations)
load.weather(weather_stations)

coords = []
for station in moisture_stations:
    coords.append(
            [
                float(station['lat']),
                float(station['lng'])
            ]
    )

vor = Voronoi(coords)

ndarray = np.ndarray( shape=2, buffer=np.array(coords[0]) );

_bool = np.where(vor.point_region == coords[7])
# print(_bool)










ri = 0
for i, reg in enumerate(vor.regions):
    if len(reg) == 0: 
        continue

    print( 'Region:', i)
    print( 'Points:' )
    
    for point in reg:
        print(vor.vertices[point])
    
    print( 'Associated point:', coords[ri], '\n')
    ri += 1

