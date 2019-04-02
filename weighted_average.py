from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point
import numpy as np
import load

# Delacare station variables
moisture_stations = []
weather_stations = []

# Load stations from static csv
load.moisture(moisture_stations)
load.weather(weather_stations)

# Fetch all coords from stations
coords = []
for station in moisture_stations:
    coords.append(
            [
                float(station['lng']),
                float(station['lat'])
            ]
    )

# Voronoi 
vor = Voronoi(coords)

_iter = [] 
ri = 0
for i, reg in enumerate(vor.regions):
    if len(reg) == 0: continue

    _points = []
    for point in reg:
        _p = vor.vertices[point]
        _points.append((_p[1], _p[0]))
    
    _iter.append({
        'station': moisture_stations[ri],
        'points': _points
    })  
    
    ri += 1



from matplotlib import pyplot as plt
from shapely.geometry.polygon import Polygon
from descartes import PolygonPatch
import random

fig = voronoi_plot_2d(vor, show_vertices=False)
ax = fig.add_subplot(1, 1, 1)
for _s in _iter:
    # path = mpltPath.Path( _s['points'] )
    polygon = Polygon(_s['points'])

    # Create random color
    r = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (r(),r(),r())
    
    #    print(polygon.area)
    # Check if weather station is inside voronoi cell
    for _ws in weather_stations:
        point = Point(_ws['lat'], _ws['lng'])
        # _inside = path.contains_points([ [_ws['lat'], _ws['lng']] ])
        _inside = polygon.contains(point)
        if _inside:
            _distance = np.linalg.norm([ _s['station']['lat'], _s['station']['lng'] ] - [  _ws['lat'], _ws['lng'] ])
            print(_distance)
            #ax.plot(_ws['lng'], _ws['lat'], color=color, marker='o')


# fig.tight_layout()    
# plt.show()
