from models.Station import SCAN
from models.Voronoi import Voronoi
import load
from sys import stdout

for i in range(2000, 2100):
    stdout.write("!"+str(i)+",")

print("\nLoading scan data")
_scans = load.scan()
print("Loading weather data")
_weathers = load.weather()


print("Creating voronoi cells")
_voronoi = Voronoi( _scans, _weathers )

print(len( _voronoi._cells ))
