from models.Station import SCAN
from models.Voronoi import Voronoi
import load

# Load stations 
_scans  = load.scan()
_weathers = load.weather()

# Create voronoi cell 
_voronoi = Voronoi( _scans, _weathers )

print(len( _voronoi._cells ))
